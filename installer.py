import os
import tkinter as tk
from tkinter import filedialog
import json

def check_file_exists(file_name):
    return os.path.isfile(file_name)

def save_settings():
    settings = {
        "ScreenWidth": 1280,
        "ScreenHeight": 720,
        "PathToImageStorage": image_folder_entry.get(),
        "PathToProjectStorage": project_folder_entry.get(),
        "GIMPpath": file_entry.get(),
        "ItemPerRow": 5
    }
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=4)

def select_image_folder():
    folder_path = filedialog.askdirectory()
    image_folder_entry.delete(0, tk.END)
    image_folder_entry.insert(0, folder_path)

def select_project_folder():
    folder_path = filedialog.askdirectory()
    project_folder_entry.delete(0, tk.END)
    project_folder_entry.insert(0, folder_path)

def select_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

# Usage
file_name = 'settings.json'
if check_file_exists(file_name):
    pass
else:
    root = tk.Tk()
    root.title("Folder and File Selector")

    image_folder_label = tk.Label(root, text="Select Image Storage Folder:")
    image_folder_label.grid(row=0, column=0, padx=5, pady=5)

    image_folder_entry = tk.Entry(root, width=50)
    image_folder_entry.grid(row=0, column=1, padx=5, pady=5)

    image_folder_button = tk.Button(root, text="Browse", command=select_image_folder)
    image_folder_button.grid(row=0, column=2, padx=5, pady=5)

    project_folder_label = tk.Label(root, text="Select Project Storage Folder:")
    project_folder_label.grid(row=1, column=0, padx=5, pady=5)

    project_folder_entry = tk.Entry(root, width=50)
    project_folder_entry.grid(row=1, column=1, padx=5, pady=5)

    project_folder_button = tk.Button(root, text="Browse", command=select_project_folder)
    project_folder_button.grid(row=1, column=2, padx=5, pady=5)

    file_label = tk.Label(root, text="Select GIMP Executable:")
    file_label.grid(row=2, column=0, padx=5, pady=5)

    file_entry = tk.Entry(root, width=50)
    file_entry.grid(row=2, column=1, padx=5, pady=5)

    file_button = tk.Button(root, text="Browse", command=select_file)
    file_button.grid(row=2, column=2, padx=5, pady=5)

    save_button = tk.Button(root, text="Save Settings", command=lambda: [save_settings(), root.destroy()])
    save_button.grid(row=3, column=1, padx=5, pady=5)

    root.mainloop()

import main
main.main()