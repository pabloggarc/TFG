import os, shutil, sys, random

def split_tt(ruta, porcentaje):
    clases = [f.path for f in os.scandir(ruta) if f.is_dir()]
    carpeta_train_general = os.path.join(ruta, "train")
    carpeta_test_general = os.path.join(ruta, "test")

    if not os.path.exists(carpeta_train_general):
        os.makedirs(carpeta_train_general)
    if not os.path.exists(carpeta_test_general):
        os.makedirs(carpeta_test_general)

    for clase in clases:
        nombre_clase = os.path.basename(clase)
        carpeta_train = os.path.join(carpeta_train_general, nombre_clase)
        carpeta_test = os.path.join(carpeta_test_general, nombre_clase)
        
        if not os.path.exists(carpeta_train):
            os.makedirs(carpeta_train)
        if not os.path.exists(carpeta_test):
            os.makedirs(carpeta_test)

        imagenes = [f.path for f in os.scandir(clase) if f.is_file()]
        
        imagenes_train = random.sample(imagenes, k = int(len(imagenes) * porcentaje))
        imagenes_test = list(set(imagenes) - set(imagenes_train))
        
        for imagen in imagenes_train:
            shutil.move(imagen, os.path.join(carpeta_train, os.path.basename(imagen)))
        for imagen in imagenes_test:
            shutil.move(imagen, os.path.join(carpeta_test, os.path.basename(imagen)))
        
        os.rmdir(clase)
            
split_tt(sys.argv[1], .8)