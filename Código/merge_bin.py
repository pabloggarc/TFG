import os, shutil

rutas_origen = [
    "../Datasets/tfg_dataset/train", 
    "../Datasets/tfg_dataset/test"
]

rutas_destino = [
    "../Datasets/tfg_dataset_bin_new/train/no_resto", 
    "../Datasets/tfg_dataset_bin_new/test/no_resto"
]

for ruta_origen, ruta_destino in zip(rutas_origen, rutas_destino): 
    for clase in [f.path for f in os.scandir(ruta_origen) if f.is_dir()]: 
        for imagen in [f.path for f in os.scandir(clase) if f.is_file()]:
            shutil.copy2(
                imagen, 
                os.path.join(ruta_destino, 
                    f"{os.path.basename(clase)}_{os.path.basename(imagen)}")
            )

rutas_origen = [
    "../Datasets/tfg_dataset_otros/train/resto", 
    "../Datasets/tfg_dataset_otros/test/resto"
]

rutas_destino = [
    "../Datasets/tfg_dataset_bin_new/train/resto", 
    "../Datasets/tfg_dataset_bin_new/test/resto"
]

for ruta_origen, ruta_destino in zip(rutas_origen, rutas_destino): 
    for imagen in [f.path for f in os.scandir(ruta_origen) if f.is_file()]:
        shutil.copy2(
            imagen, 
            os.path.join(ruta_destino, 
                f"resto_{os.path.basename(imagen)}")
        )