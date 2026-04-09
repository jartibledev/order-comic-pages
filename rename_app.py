
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
            
            new_file_path = file_path.with_name(f"{name_file}{count}{file_path.suffix}")
            file_path.rename(new_file_path)

def iterator_files_all_odds( folder_path, name_file:str):
    folder = Path(folder_path)
    count = -1
    
    for file_path in folder.iterdir():
        if file_path.is_file():  
            count += 2
            odd_count = count if  count%2 != 0  else count + 1
            
            new_file_path = file_path.with_name(f"{name_file}{odd_count}{file_path.suffix}")
            file_path.rename(new_file_path)

def iterator_files_all_evens( folder_path, name_file:str):
    folder = Path(folder_path)
    count = 0
    
    for file_path in folder.iterdir():
        if file_path.is_file():  
            count += 2
            odd_count = count  if  count%2 == 0 else count + 1
            
            new_file_path = file_path.with_name(f"{name_file}{odd_count}{file_path.suffix}")
            file_path.rename(new_file_path)

def iterator_files_evens( folder_path, name_file:str):
    folder = Path(folder_path)
    count = 0
    
    for file_path in folder.iterdir():
        if file_path.is_file():  
            count += 1
            if count % 2 == 0:
                new_file_path = file_path.with_name(f"{name_file}{count}{file_path.suffix}")
                file_path.rename(new_file_path)  

def iterator_files_odd( folder_path, name_file:str):
    folder = Path(folder_path)
    count = 0
    
    for file_path in folder.iterdir():
        if file_path.is_file():  
            count += 1
            if count % 2 != 0:
                new_file_path = file_path.with_name(f"{name_file}{count}{file_path.suffix}")
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

def odd():
    name = entry.get()
    folder_path = get_folder()
    iterator_files_all_odds(folder_path=folder_path, name_file=name)

def evens():
    name = entry.get()
    folder_path = get_folder()
    iterator_files_all_evens(folder_path=folder_path, name_file=name)

root = tk.Tk()
root.geometry("800x400")
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

textvariable = tk.StringVar() 
textvariable.set("Untitled")

entry = ttk.Entry(master=frame,textvariable=textvariable)
entry.pack(side=tk.LEFT)

button= ttk.Button(master=frame ,text="Select your folder", command=get_folder)
button.pack(side=tk.LEFT, padx=5)


button2= ttk.Button(master=frame ,text="Change names", command = wrap )
button2.pack(side=tk.LEFT, padx=5)

button_odd= ttk.Button(master=frame ,text="All odds", command = odd  )
button_odd.pack(side=tk.LEFT, padx=5) 

button_evens= ttk.Button(master=frame ,text="All evens", command = evens  )
button_evens.pack(side=tk.LEFT, padx=5) 

root.mainloop()