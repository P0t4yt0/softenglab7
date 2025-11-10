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
        super().__init__(themename="litera")
        self.title("JBSON Hardware - Main Menu")
        self.geometry("450x350")
        self.resizable(False, False)
        # Configure a custom style for the header to enforce black text
        # We also slightly increase the font size for emphasis.
        self.style.configure("BlackHeader.TLabel", 
                             foreground="black", 
                             font=("Helvetica", 18, "bold")) 
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
        
        # Use the custom style to make the text (including "JBSON") black
        main_label = ttk.Label(
            self, 
            text="JBSON Hardware", 
            style="BlackHeader.TLabel"
        )
        main_label.pack(pady=40, padx=20)
        
        # --- Main Actions Frame ---
        # Using a frame to manage button layout nicely
        action_frame = ttk.Frame(self)
        action_frame.pack(pady=10, padx=40, fill="x")

        # 1. Inventory CRUD Button
        ttk.Button(
            action_frame, 
            text="1. Open Inventory Item Control (CRUD)", 
            command=self.open_inventory_app, 
            bootstyle="success-outline"
        ).pack(pady=8, fill="x")

        # 2. Hardware Search Button (NEWLY ADDED)
        ttk.Button(
            action_frame, 
            text="2. Open Hardware Search", 
            command=self.open_search_app, 
            bootstyle="info-outline" 
        ).pack(pady=8, fill="x")

        # Exit button
        ttk.Button(
            self,
            text="Exit Application",
            command=self.quit,
            bootstyle="danger" 
        ).pack(pady=20, padx=40, fill="x")

    def open_inventory_app(self):
        """Launches the add_item_view.py script using subprocess."""
        self.destroy() 
        try:
            # This file will handle the CRUD interface
            subprocess.Popen([sys.executable, "add_item_view.py"])
        except Exception as e:
            messagebox.showerror("Launch Error", f"Could not launch add_item_view.py.\nError: {e}\n\nPlease ensure the file is in the same directory.")
            print(f"Error launching inventory app: {e}")
            MainMenu().mainloop()

    def open_search_app(self):
        """Launches the search_form.py script using subprocess."""
        self.destroy() 
        try:
            # This file will handle the search interface
            subprocess.Popen([sys.executable, "search_form.py"])
        except Exception as e:
            messagebox.showerror("Launch Error", f"Could not launch search_form.py.\nError: {e}\n\nPlease ensure the file is in the same directory.")
            print(f"Error launching search app: {e}")
            MainMenu().mainloop()


if __name__ == "__main__":
    menu_app = MainMenu()
    menu_app.mainloop()