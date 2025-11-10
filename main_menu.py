import tkinter as tk
import ttkbootstrap as ttk
import subprocess
import sys
from tkinter import messagebox 

class MainMenu(ttk.Window):
    """
    Main Menu window for JBSON Hardware applications.
    Allows the user to select which module to open.
    """
    def __init__(self):
        # Change 1: Switched theme to 'flatly' for a clean white background
        super().__init__(themename="flatly")
        # Change 3: Completed the company name in the title
        self.title("JBSON Global Enterprises - Main Menu")
        # Change 2: Increased size to 550x500 for a bigger window
        self.geometry("550x500") 
        self.resizable(False, False)
        self.center_window()
        self.create_widgets()

    def center_window(self):
        """Centers the window on the screen."""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        # --- Header Section (Increased padding and visual weight) ---
        main_label = ttk.Label(
            self, 
            # Change 3: Full company name
            text="JBSON GLOBAL ENTERPRISES HARDWARE MANAGEMENT SYSTEM", 
            # Adjusted bootstyle for light theme (primary/dark text on white)
            bootstyle="primary", 
            font=("Helvetica", 18, "bold")
        )
        main_label.pack(pady=(50, 15), padx=20) 

        # Increased padx for separator to match wider window
        ttk.Separator(self, orient='horizontal').pack(fill='x', padx=50, pady=10)


        # --- Main Action Frame (Groups the buttons visually) ---
        action_frame = ttk.Frame(self, padding=30, bootstyle="secondary")
        # Increased padx for action frame to match wider window
        action_frame.pack(pady=25, padx=60, fill="x")

        # 1. Inventory CRUD Button (Primary Action - Success/Green)
        ttk.Button(
            action_frame, 
            text="1. Open Inventory Item Control (CRUD)", 
            command=self.open_inventory_app, 
            bootstyle="success",
            width=40 # Increased width for better fit
        ).pack(pady=15, fill="x")

        # 2. Hardware Search Button (Secondary Action - Info/Blue)
        ttk.Button(
            action_frame, 
            text="2. Open Hardware Search", 
            command=self.open_search_app, 
            bootstyle="info", 
            width=40 # Increased width for better fit
        ).pack(pady=15, fill="x")

        # --- Exit Button (Separated from main actions) ---
        ttk.Button(
            self,
            text="Exit Application",
            command=self.quit,
            bootstyle="danger-outline",
            width=40 # Increased width to align with buttons in the frame
        ).pack(pady=40, padx=60, fill="x")

    def open_inventory_app(self):
        """Launches the add_item_view.py script using subprocess."""
        self.destroy() 
        try:
            subprocess.Popen([sys.executable, "add_item_view.py"])
        except Exception as e:
            messagebox.showerror("Launch Error", f"Could not launch add_item_view.py.\nError: {e}\n\nPlease ensure the file is in the same directory.")
            print(f"Error launching inventory app: {e}")
            MainMenu().mainloop()

    def open_search_app(self):
        """
        Launches the search_form.py script using subprocess.
        """
        self.destroy() 
        try:
            # Launches the correct file: search_form.py
            subprocess.Popen([sys.executable, "search_form.py"])
        except Exception as e:
            messagebox.showerror("Launch Error", f"Could not launch search_form.py.\nError: {e}\n\nPlease ensure the file is in the same directory.")
            print(f"Error launching search app: {e}")
            MainMenu().mainloop()


if __name__ == "__main__":
    menu_app = MainMenu()
    menu_app.mainloop()