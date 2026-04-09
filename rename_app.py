import os
from pathlib import Path
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk

def change_name (old_name : str,
                 new_name : str, 
                 number : int):
    # Ruta actual del archivo
    old_file = old_name
   
    # Nuevo nombre para el archivo

    new_file = new_name + f"_{number}.txt"
    print(new_file)
    # Renombrar el archivo
    os.rename(old_file, new_file)

def iterator_files( folder_path, name_file:str):
    

    # Definir la carpeta
    #folder = Path(r'C:\Users\Usuario\Desktop\projects\projects_dev\dev\projects\rename_in_order\pruebas')
    folder = Path(folder_path)
    print  (folder)
    # Iterar sobre todos los archivos (sin incluir subcarpetas)
    for file_path in folder.iterdir():
        if file_path.is_file():  # Asegurarse de que es un archivo, no una carpeta
            print(f"Archivo encontrado: {file_path.name}")
            print(f"Ruta completa: {file_path}")
            # Aquí puedes abrir o procesar el archivo:

            # with open(file_path, 'r') as f: ...

           

            #ruta = '/ruta/a/tu/carpeta'
            # Cuenta solo archivos, ignorando directorios
            num_archivos = len([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])
            print(f"Archivos: {num_archivos}")

            change_name(old_name=file_path, number=num_archivos, new_name=name_file )

def get_folder():
    path_folder = filedialog.askdirectory(
    title="Select your folder"
    )
    if path_folder:
        print(f"Carpeta seleccionada: {path_folder}")
        return path_folder
def wrap():
    name = entry.get()
    folder_path = get_folder()
    print(folder_path)
    print(name)
    iterator_files(folder_path=folder_path, name_file=name)






root = tk.Tk()
#root.withdraw()
root.geometry("400x400")
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

textvariable = tk.StringVar() 
textvariable.set("Select name folder")

entry = ttk.Entry(master=frame,textvariable=textvariable)
entry.pack(side=tk.LEFT)
# Posicionarla en la ventana.

folder_path = ""
button= ttk.Button(master=frame ,text="Select your folder", command=get_folder)
button.pack(side=tk.LEFT, padx=5)


button2= ttk.Button(master=frame ,text="Change names", command = wrap )
button2.pack(side=tk.LEFT, padx=5) 


root.mainloop()