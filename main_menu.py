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
        self.geometry("400x300")
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
        
        main_label = ttk.Label(
            self, 
            text="JBSON Hardware Management System", 
            bootstyle="primary", 
            font=("Helvetica", 14, "bold")
        )
        main_label.pack(pady=40, padx=20)
        
        # Button to launch the Inventory CRUD module
        ttk.Button(
            self, 
            text="Open Inventory Item Control (CRUD)", 
            command=self.open_inventory_app, 
            bootstyle="success"
        ).pack(pady=10, padx=20, fill="x")

        # Exit button
        ttk.Button(
            self,
            text="Exit Application",
            command=self.quit,
            bootstyle="danger-outline"
        ).pack(pady=10, padx=20, fill="x")

    def open_inventory_app(self):
        """Launches the add_item_view.py script using subprocess."""
        # 1. Close the current (menu) window
        self.destroy() 
        
        # 2. Launch the new script
        try:
            # NOTE: Updated to reference the user-specified file name: add_item_view.py
            subprocess.Popen([sys.executable, "add_item_view.py"])
        except Exception as e:
            # Show error message to the user and re-open the main menu
            messagebox.showerror("Launch Error", f"Could not launch add_item_view.py.\nError: {e}\n\nPlease ensure the file is in the same directory.")
            print(f"Error launching inventory app: {e}")
            MainMenu().mainloop()


if __name__ == "__main__":
    # If this is the file that is run first, show the Main Menu
    menu_app = MainMenu()
    menu_app.mainloop()