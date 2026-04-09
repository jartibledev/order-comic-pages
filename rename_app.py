
from pathlib import Path
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk



def iterator_files( folder_path, name_file:str):
    folder = Path(folder_path)
    count = 0
    for file_path in folder.iterdir():
        if file_path.is_file():  
            count += 1
            new_file_path = file_path.with_name(f"{name_file}{count}.txt")
            file_path.rename(new_file_path)
           

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
    iterator_files(folder_path=folder_path, name_file=name)






root = tk.Tk()
root.geometry("400x400")
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

textvariable = tk.StringVar() 
textvariable.set("Untitle")

entry = ttk.Entry(master=frame,textvariable=textvariable)
entry.pack(side=tk.LEFT)

button= ttk.Button(master=frame ,text="Select your folder", command=get_folder)
button.pack(side=tk.LEFT, padx=5)


button2= ttk.Button(master=frame ,text="Change names", command = wrap )
button2.pack(side=tk.LEFT, padx=5) 


root.mainloop()