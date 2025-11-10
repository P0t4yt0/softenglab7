import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from tkinter import Toplevel, Listbox
import uuid 
import subprocess
import sys 

class App(ttk.Window):

    def __init__(self):

        super().__init__(themename="litera")


        self.title("JBSON Hardware - Inventory Item Control (CRUD)")
        self.geometry("650x700")
        self.resizable(False, False)
        
        self.inventory_data = {
            "SKU001": {"name": "Hammer (Claw)", "qty": 150, "price": 12.99, "desc": "Standard 16oz claw hammer."},
            "SKU002": {"name": "Screwdriver Set", "qty": 80, "price": 24.50, "desc": "6-piece mixed precision set."},
            "SKU003": {"name": "Wood Screws (Box)", "qty": 300, "price": 5.99, "desc": "Box of 100 2-inch wood screws."}
        }
        self.selected_sku = None

        self.center_window()
        self.create_widgets()
        self.update_listbox()

    def center_window(self):

        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')


    def return_to_main_menu(self):

        self.destroy()
        
  
        try:
            subprocess.Popen([sys.executable, "main_menu.py"])
        except Exception as e:
            print(f"ERROR: Could not launch main_menu.py. Error: {e}")

            
    def create_widgets(self):
        header_frame = ttk.Frame(self)
        header_frame.pack(fill="x", padx=30, pady=(10, 0))
        
        ttk.Button(
            header_frame,
            text="← Back to Main Menu",
            command=self.return_to_main_menu,
            bootstyle="secondary"
        ).pack(side="left", padx=5, pady=5)
        
        main_frame = ttk.Labelframe(self, text="Item Details", padding="20 15 20 20", bootstyle="primary")
        main_frame.pack(fill="x", padx=30, pady=20)

        main_frame.columnconfigure(1, weight=1)

        self.sku_var = tk.StringVar(value="[Auto-Generated for New Item]")
        self.name_var = tk.StringVar()
        self.qty_var = tk.StringVar()
        self.price_var = tk.StringVar()


        self._create_label_entry(main_frame, "Item Name:", self.name_var, 0)

        sku_label = ttk.Label(main_frame, text="SKU / Item Code:")
        sku_label.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=7)
        self.sku_entry = ttk.Entry(main_frame, textvariable=self.sku_var, width=40, font=("Helvetica", 10), bootstyle="secondary")
        self.sku_entry.config(state='readonly') 
        self.sku_entry.grid(row=1, column=1, sticky="we", padx=5, pady=7)

        self._create_label_entry(main_frame, "Stock Quantity:", self.qty_var, 2)

        self._create_label_entry(main_frame, "Unit Price (₱):", self.price_var, 3)

        desc_label = ttk.Label(main_frame, text="Description:")
        desc_label.grid(row=4, column=0, sticky="ne", padx=(0, 10), pady=7)
        
        self.desc_text = tk.Text(main_frame, width=40, height=3, font=("Helvetica", 10), wrap="word")
        self.desc_text.grid(row=4, column=1, sticky="we", padx=5, pady=7)
        
        self.error_label = ttk.Label(
            main_frame, 
            text="", 
            bootstyle="danger", 
            font=("Helvetica", 9)
        )
        self.error_label.grid(row=5, column=0, columnspan=2, pady=10)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        ttk.Button(
            button_frame, 
            text="Add New Item", 
            command=self.add_item,
            bootstyle="success"
        ).pack(side="left", padx=10, ipady=5)
        
        ttk.Button(
            button_frame, 
            text="Edit Selected Item", 
            command=self.edit_item,
            bootstyle="warning"
        ).pack(side="left", padx=10, ipady=5)
        
        ttk.Button(
            button_frame, 
            text="Remove Item", 
            command=self.remove_item,
            bootstyle="danger"
        ).pack(side="left", padx=10, ipady=5)

        ttk.Button(
            button_frame, 
            text="Clear Form", 
            command=self.clear_form,
            bootstyle="secondary-outline"
        ).pack(side="left", padx=10, ipady=5)
        
        list_frame = ttk.Labelframe(self, text="Current Inventory List (Select to Edit/Remove)", padding="10 10 10 10")
        list_frame.pack(fill="both", expand=True, padx=30, pady=(0, 20))
        
        self.item_listbox = Listbox(list_frame, height=10, font=("Helvetica", 10))
        self.item_listbox.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.item_listbox.bind('<<ListboxSelect>>', self.load_selected_item)
        
    def _create_label_entry(self, parent, label_text, textvariable, row_num):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row_num, column=0, sticky="e", padx=(0, 10), pady=7)
        entry = ttk.Entry(parent, textvariable=textvariable, width=40, font=("Helvetica", 10))
        entry.grid(row=row_num, column=1, sticky="we", padx=5, pady=7)
        return entry

    def update_listbox(self):
        self.item_listbox.delete(0, tk.END)
        for sku, item in self.inventory_data.items():
            display_text = f"[{sku}] {item['name']} | Qty: {item['qty']} | Price: ₱{item['price']:.2f}"
            self.item_listbox.insert(tk.END, display_text)

    def load_selected_item(self, event):
        self.clear_error()
        try:
            selected_indices = self.item_listbox.curselection()
            if not selected_indices:
                return
            
            list_item_text = self.item_listbox.get(selected_indices[0])
            sku = list_item_text.split("]")[0].strip("[")
            
            if sku in self.inventory_data:
                item = self.inventory_data[sku]
                self.selected_sku = sku
                
                self.sku_entry.config(state='normal')
                self.sku_var.set(sku)
                self.sku_entry.config(state='readonly')
                
                self.name_var.set(item['name'])
                self.qty_var.set(str(item['qty']))
                self.price_var.set(f"{item['price']:.2f}")
                
                self.desc_text.delete('1.0', tk.END)
                self.desc_text.insert('1.0', item['desc'])
                
                self.error_label.config(text=f"Item {sku} loaded for editing.")
            
        except Exception as e:
            print(f"Error loading item: {e}")
            self.error_label.config(text="Error loading item details.")
            
    def validate_inputs(self):
        name = self.name_var.get().strip()
        qty_str = self.qty_var.get().strip()
        price_str = self.price_var.get().strip()
        desc = self.desc_text.get('1.0', tk.END).strip()
        
        if not name:
            self.show_error("Error: Item Name is required.")
            return None
            
        if not qty_str:
            self.show_error("Error: Quantity is required.")
            return None

        if not price_str:
            self.show_error("Error: Unit Price is required.")
            return None
        
        try:
            qty = int(qty_str)
            if qty < 0: raise ValueError
        except ValueError:
            self.show_error("Error: Quantity must be a non-negative whole number.")
            return None
            
        try:
            price = float(price_str)
            if price <= 0: raise ValueError
        except ValueError:
            self.show_error("Error: Unit Price must be a positive number.")
            return None

        # Return sanitized data
        return {
            "name": name,
            "qty": qty,
            "price": price,
            "desc": desc
        }

    def clear_error(self):
        self.error_label.config(text="")

    def show_error(self, message):
        self.error_label.config(text=message)

    def clear_form(self):
        self.clear_error()
        self.selected_sku = None
        self.sku_var.set("[Auto-Generated for New Item]")
        self.sku_entry.config(state='readonly')
        self.name_var.set("")
        self.qty_var.set("")
        self.price_var.set("")
        self.desc_text.delete('1.0', tk.END)
        self.name_var.get() 

    def add_item(self):
        validated_data = self.validate_inputs()
        if not validated_data:
            return
            
        new_sku = "SKU" + str(uuid.uuid4())[:8].upper().replace('-', '')
        
        while new_sku in self.inventory_data:
            new_sku = "SKU" + str(uuid.uuid4())[:8].upper().replace('-', '')

        self.inventory_data[new_sku] = validated_data
        
        messagebox.showinfo(
            "Success", 
            f"Item successfully ADDED:\nSKU: {new_sku}\nName: {validated_data['name']}\nQty: {validated_data['qty']}"
        )
        print(f"[Activity Log]: Added new item {new_sku}.")
        self.clear_form()
        self.update_listbox()
        
    def edit_item(self):
        """Mocks editing the selected item in the inventory."""
        if not self.selected_sku or self.selected_sku not in self.inventory_data:
            self.show_error("Error: Select an item from the list or clear the form to add a new one.")
            return
            
        validated_data = self.validate_inputs()
        if not validated_data:
            return
            
        old_data = self.inventory_data[self.selected_sku]
        self.inventory_data[self.selected_sku] = validated_data
        
        messagebox.showwarning(
            "Update Successful", 
            f"Item '{validated_data['name']}' ({self.selected_sku}) updated.\nOld Qty: {old_data['qty']} -> New Qty: {validated_data['qty']}"
        )
        print(f"[Activity Log]: Updated item {self.selected_sku}. Old data: {old_data}, New data: {validated_data}.")
        self.clear_form()
        self.update_listbox()

    def remove_item(self):
        if not self.selected_sku or self.selected_sku not in self.inventory_data:
            self.show_error("Error: Select an item from the list to remove it.")
            return
            
        item_name = self.inventory_data[self.selected_sku]['name']
        
        confirm_window = Toplevel(self)
        confirm_window.title("Confirm Removal")
        confirm_window.geometry("300x150")
        confirm_window.transient(self)
        confirm_window.grab_set()
        
        self.update_idletasks()
        main_x = self.winfo_rootx()
        main_y = self.winfo_rooty()
        main_width = self.winfo_width()
        main_height = self.winfo_height()
        
        confirm_window_width = 300
        confirm_window_height = 150
        
        x = main_x + (main_width - confirm_window_width) // 2
        y = main_y + (main_height - confirm_window_height) // 2
        confirm_window.geometry(f'{confirm_window_width}x{confirm_window_height}+{x}+{y}')

        ttk.Label(confirm_window, text=f"Are you sure you want to REMOVE '{item_name}'?", wraplength=280, font=("Helvetica", 10, "bold")).pack(pady=15, padx=10)
        
        button_frame = ttk.Frame(confirm_window)
        button_frame.pack(pady=10)
        
        def do_remove():
            del self.inventory_data[self.selected_sku]
            
            messagebox.showerror(
                "Removed", 
                f"Item '{item_name}' ({self.selected_sku}) has been REMOVED from inventory."
            )
            print(f"[Activity Log]: Removed item {self.selected_sku} ({item_name}).")
            
            confirm_window.destroy()
            self.clear_form()
            self.update_listbox()

        def cancel():
            confirm_window.destroy()

        ttk.Button(button_frame, text="Yes, Remove", command=do_remove, bootstyle="danger").pack(side="left", padx=10)
        ttk.Button(button_frame, text="Cancel", command=cancel, bootstyle="secondary-outline").pack(side="left", padx=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()