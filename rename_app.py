
from pathlib import Path
from tkinter import filedialog

import tkinter as tk
import customtkinter as ctk



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

root = ctk.CTk()
root.geometry("800x400")

ctk.set_appearance_mode("dark")

frame = ctk.CTkFrame(root)
frame.pack()


label_entry = ctk.CTkLabel(master = frame, text= "Write the new name of your files")
label_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
textvariable = ctk.StringVar() 
textvariable.set("Untitled")
entry = ctk.CTkEntry(master=frame,textvariable=textvariable)
entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")


label_entry = ctk.CTkLabel(master = frame, text= "Rename your files")
label_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
button2= ctk.CTkButton(master=frame ,text="Change names", command = wrap, hover_color="#8d8d8d", fg_color= "#3B3B3B" )
button2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

label_entry = ctk.CTkLabel(master = frame, text= "Select the order of your elements")
label_entry.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

button_odd= ctk.CTkButton(master=frame ,text="All odds",  hover_color="#8d8d8d", fg_color= "#3B3B3B", command = odd  )
button_odd.grid(row=1, column=2, padx=10, pady=10, sticky="ew")


button_evens= ctk.CTkButton(master=frame ,text="All evens", command = evens, hover_color="#8d8d8d", fg_color= "#3B3B3B"  )
button_evens.grid(row=2, column=2, padx=10, pady=10, sticky="ew") 

root.mainloop()