import numpy as np
import matplotlib.pyplot as plt

from scipy.special import lambertw
from keras import *

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"]
})

x_train = np.linspace(-.35, 100, 1000)
y_train = lambertw(x_train).real
x_test = np.random.uniform(low = -.2, high = 100, size = 200)
y_test = lambertw(x_test).real

red = Sequential([
    layers.Dense(100, input_dim = 1, activation = "relu"),
    layers.Dense(100, activation = "relu"),
    layers.Dense(1)
])

epocas = 250
red.compile(optimizer = "adam", loss = "mean_squared_error")
entrenamiento = red.fit(x_train, y_train, 
                        epochs = epocas, validation_split = .25, 
                        verbose = 1
                    )

red.save("rnn.keras")

y_hat = red.predict(x_test)
recorte_epocas = int(np.floor(epocas - .9 * epocas))

plt.subplot(1, 2, 1)
plt.xlim(recorte_epocas, epocas)
plt.ylim(0, max(max(entrenamiento.history['loss'][recorte_epocas:]), max(entrenamiento.history['val_loss'][recorte_epocas:])))
plt.plot(entrenamiento.history['loss'], label = "$\\mathrm{MSE}_{\\mathrm{train}}$")
plt.plot(entrenamiento.history['val_loss'], label = "$\\mathrm{MSE}_{\\mathrm{val}}$")
plt.title("Error durante el entrenamiento")
plt.xlabel("Número de épocas")
plt.ylabel("MSE")
plt.legend()
plt.subplot(1, 2, 2)
plt.title("$W(x)$ vs $\\hat{W}(x)$, $\\mathrm{MSE}_{\\mathrm{test}}$ = " + f"{np.mean((y_test - y_hat)**2):.3f}")
plt.plot(x_train, y_train, label = "$W(x)$")
plt.plot(x_test, y_hat, 'o', label = "$\hat{W}(x)$")
plt.legend()
plt.show()