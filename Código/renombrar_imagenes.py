import os, sys

def renombrar_imagenes(ruta): 
    clases = [f.path for f in os.scandir(ruta) if f.is_dir()]
    for clase in clases:
        nombre_clase = os.path.basename(clase)
        imagenes = [f.path for f in os.scandir(clase) if f.is_file()]
        for i, imagen in enumerate(imagenes): 
            ext = os.path.splitext(imagen)[1]
            try: 
                os.rename(imagen, f"{ruta}/{nombre_clase}/{i}{ext}")
            except: pass 
            
renombrar_imagenes(sys.argv[1])