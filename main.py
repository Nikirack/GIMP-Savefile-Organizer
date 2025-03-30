import tkinter as tk
from tkinter import ttk
import json
import os
from PIL import Image, ImageTk
import datetime
import subprocess

with open("settings.json", 'r') as f:
    settings = json.load(f)

screen_width = settings["ScreenWidth"]
screen_height = settings["ScreenHeight"]
GIMP_storage_projects = settings["PathToProjectStorage"]
GIMP_storage_exports = settings["PathToImageStorage"]
GIMP_path = settings["GIMPpath"]
ItemsPerRow = settings["ItemPerRow"]

def get_xcf_files(folder_path):
    return [item for item in os.listdir(folder_path) if item.endswith(".xcf")]

def get_export_image(file_name):
    image_path = f"{GIMP_storage_exports}/{file_name.split('.')[0]}.png"
    return image_path if os.path.exists(image_path) else None

def get_file_modification_time(file_path):
    return datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

def open_gimp():
    subprocess.Popen(GIMP_path)

def open_file(file_name):
    file_path = f"{GIMP_storage_projects}/{file_name}"
    os.startfile(file_path)

def on_mouse_scroll(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

def main():
    global canvas
    xcf_files = get_xcf_files(GIMP_storage_projects)
    
    xcf_files.sort(key=lambda f: get_file_modification_time(f"{GIMP_storage_projects}/{f}"), reverse=True)
    
    root = tk.Tk()
    root.title("GIMP Savefile Organizer")
    root.configure(background="#f0f0f0")
    root.geometry(f"{screen_width}x{screen_height}")
    root.resizable(True, True)

    header_label = tk.Label(root, text="GIMP Savefile Organizer", font=("Arial", 24), bg="#f0f0f0", fg="#333333")
    header_label.pack(pady=20)
    
    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(fill="both", expand=True)
    
    gimp_button = tk.Button(frame, text="+", width=20, height=5, bg="#bebebe", command=open_gimp)
    gimp_button.pack()
    gimp_label = tk.Label(frame, text="Open GIMP", wraplength=160, font=("Arial", 10), bg="#f0f0f0")
    gimp_label.pack()
    
    canvas = tk.Canvas(frame, bg="#f0f0f0")
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((screen_width // 2, 0), window=scrollable_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    canvas.bind_all("<MouseWheel>", on_mouse_scroll)
    
    for i, file in enumerate(xcf_files):
        row, col = divmod(i, ItemsPerRow)
        
        file_frame = tk.Frame(scrollable_frame, bg="#f0f0f0", padx=10, pady=10)
        file_frame.grid(row=row, column=col, padx=20, pady=10)
        
        image_path = get_export_image(file)
        if image_path:
            image = Image.open(image_path).resize((160, 90))
            photo = ImageTk.PhotoImage(image)
            button = tk.Button(file_frame, image=photo, command=lambda f=file: open_file(f))
            button.image = photo
        else:
            button = tk.Button(file_frame, text=f"{file}\nNo image available", width=20, height=5, bg="#bebebe", command=lambda f=file: open_file(f))
        
        mod_time = get_file_modification_time(f"{GIMP_storage_projects}/{file}")
        label = tk.Label(file_frame, text=f"{file}\nLast modified: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}", wraplength=160, font=("Arial", 10), bg="#f0f0f0")
        
        button.pack()
        label.pack()
    
    root.mainloop()

