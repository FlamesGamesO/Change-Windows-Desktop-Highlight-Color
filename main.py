import subprocess
import sys

def install_packages():
    required_packages = ["customtkinter"]
    for package in required_packages:
        try:
            __import__(package)  # Check if already installed
        except ImportError:
            print(f"Installing missing package: {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_packages()

import tkinter as tk
from tkinter import colorchooser, messagebox
import customtkinter as ctk
import winreg

def set_highlight_color(rgb_tuple):
    r, g, b = rgb_tuple
    color_value = f"{r} {g} {b}"

    try:

        key_path = r"Control Panel\Colors"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "Hilight", 0, winreg.REG_SZ, color_value)
            winreg.SetValueEx(key, "HotTrackingColor", 0, winreg.REG_SZ, color_value)
        
        messagebox.showinfo("Success", "Highlight color changed! Restart your PC to apply changes.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update the registry: {e}")

def pick_color():
    color_code = colorchooser.askcolor(title="Choose a Highlight Color")[0]  # Returns (r, g, b)
    if color_code:
        color_display.configure(fg_color=f"#{int(color_code[0]):02x}{int(color_code[1]):02x}{int(color_code[2]):02x}")
        set_highlight_color(color_code)

def restart_pc():
    subprocess.run("shutdown /r /t 0", shell=True)

ctk.set_appearance_mode("dark")  # Modern dark theme
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Desktop Highlight Color Changer")
app.geometry("400x300")

title_label = ctk.CTkLabel(app, text="Change Desktop Highlight Color", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

color_button = ctk.CTkButton(app, text="Pick a Color", command=pick_color, fg_color="#0078D7")
color_button.pack(pady=10)

color_display = ctk.CTkFrame(app, width=100, height=40, fg_color="white")
color_display.pack(pady=10)

restart_button = ctk.CTkButton(app, text="Restart PC", command=restart_pc, fg_color="red")
restart_button.pack(pady=20)

app.mainloop()
