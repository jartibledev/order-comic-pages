import os
from pathlib import Path


def change_name (old_name : str , 
                 new_name : int):
    # Ruta actual del archivo
    old_file = old_name

    # Nuevo nombre para el archivo

    new_file = f"Page{new_name}.txt"

    # Renombrar el archivo
    os.rename(old_file, new_file)

def iterator_files():
    

    # Definir la carpeta
    folder = Path(r'C:\Users\Usuario\Desktop\projects\projects_dev\dev\projects\rename_in_order\pruebas')

    # Iterar sobre todos los archivos (sin incluir subcarpetas)
    for file_path in folder.iterdir():
        if file_path.is_file():  # Asegurarse de que es un archivo, no una carpeta
            print(f"Archivo encontrado: {file_path.name}")
            print(f"Ruta completa: {file_path}")
            # Aquí puedes abrir o procesar el archivo:

            # with open(file_path, 'r') as f: ...

           
            name_file = Path(file_path).name  # Resultado: 'archivo.txt'

            #ruta = '/ruta/a/tu/carpeta'
            # Cuenta solo archivos, ignorando directorios
            num_archivos = len([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])
            print(f"Archivos: {num_archivos}")

            change_name(old_name=file_path, new_name=num_archivos)
           

iterator_files()