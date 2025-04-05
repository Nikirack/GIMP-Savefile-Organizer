# GIMP Savefile Organizer 💾

**GIMP Savefile Organizer** is a tool designed to help you organize your GIMP savefiles, which can often become scattered or difficult to manage. Since GIMP doesn't have a built-in savefile organizer, this tool was created to fill that gap and make your file management smoother.
![Screenshot of the app](https://github.com/Nikirack/GIMP-Savefile-Organizer/blob/main/public/Skjermbilde%202025-04-05%20111731.png)

---

## Features ✨
- **Organize GIMP savefiles**: Sort your GIMP projects by time edited, with images to show what project it is.
- **Image Preview**: Render image thumbnails for better visual management using **Pillow**.
- **Simple Interface**: Built with **Tkinter** for a lightweight, easy-to-use graphical interface.
- **Cross-platform**: Works on Windows, macOS, and Linux, the pebuilt binary made by pyinstaller is only for windows.

---

## Tech Stack ⚙️
- **Python** : The main programming language.
- **Tkinter**: For building the graphical user interface (GUI).
- **Pillow**: For rendering image previews and handling image operations.

---

## Installation 🚀

1. **Clone the repository**:
```bash
git clone https://github.com/Nikirack/GIMP-Savefile-Organizer.git
```
2. Navigate into the project directory:
```bash
cd gimp-savefile-organizer
```
3. Install dependencies:
You can install the required Python packages via pip:
```bash
pip install -r requirements.txt
```
4. Run the application:
```bash
python installer.py
```
## Usage 🖱️

After launching the application, you'll be greeted with a screen where you put in your GIMP projects folder, and your exports frolder, then you need to put the path to your GIMP binary (The image-rendering only works if the name of the image is the same as the project).
After that, every time you'll see a simple window where you can see your GIMP savefiles and run them.
When you want to launch the app after the settup, you just need to run the installer.py, and it will put you right in to the app.
    
