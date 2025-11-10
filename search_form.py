import tkinter as tk
import ttkbootstrap as ttk
import subprocess
import sys
from tkinter import messagebox

class ProductSearchApp(ttk.Window):
    """
    Main application window for the Product Search Form.
    """
    def __init__(self):
        # Same theme as the login page
        super().__init__(themename="litera")

        # --- Window Configuration ---
        self.title("JBSON Hardware - Product Search")
        self.geometry("600x750") # Adjusted size
        self.resizable(False, False)
        
        self.center_window()

        # --- Main Frame ---
        main_frame = ttk.Frame(self, padding="20 20 20 20")
        main_frame.pack(fill="both", expand=True)

        # --- IMPORTANT: Column Configuration ---
        main_frame.columnconfigure(1, weight=1) # Let the controls expand

        # --- Form Controls (Widgets) ---
        
        # 1. Form Title (Label)
        title_label = ttk.Label(
            main_frame, 
            text="Product & Inventory Search", 
            font=("Helvetica", 18, "bold"),
            bootstyle="primary" 
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # --- Placeholder Helper ---
        def on_focus_in(event):
            widget = event.widget
            if widget.get() == widget.placeholder:
                widget.delete(0, tk.END)
                widget.config(foreground='black')

        def on_focus_out(event):
            widget = event.widget
            if not widget.get():
                widget.insert(0, widget.placeholder)
                widget.config(foreground='grey')

        # 1. Search Term (Textbox - The "Search Bar")
        search_label = ttk.Label(main_frame, text="Search Term:")
        search_label.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=10)
        
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(main_frame, textvariable=self.search_var, width=40, font=("Helvetica", 12))
        self.search_entry.placeholder = "Enter Product Name, ID, or Barcode"
        self.search_entry.widgetName = "searchEntry"
        self.search_entry.insert(0, self.search_entry.placeholder)
        self.search_entry.config(foreground='grey')
        self.search_entry.bind("<FocusIn>", on_focus_in)
        self.search_entry.bind("<FocusOut>", on_focus_out)
        self.search_entry.grid(row=1, column=1, sticky="we", padx=5, pady=10)

        # 2. Search By (Dropdown)
        search_by_label = ttk.Label(main_frame, text="Search By:")
        search_by_label.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)
        
        self.search_by_var = tk.StringVar()
        search_by_combo = ttk.Combobox(
            main_frame, 
            textvariable=self.search_by_var, 
            values=["Any (All Fields)", "Product Name", "Product ID", "Barcode", "Supplier"],
            state="readonly"
        )
        search_by_combo.current(0)
        search_by_combo.grid(row=2, column=1, sticky="we", padx=5, pady=5)

        # 3. Product Category (Dropdown)
        category_label = ttk.Label(main_frame, text="Category:")
        category_label.grid(row=3, column=0, sticky="e", padx=(0, 10), pady=5)
        
        self.category_var = tk.StringVar()
        category_combo = ttk.Combobox(
            main_frame, 
            textvariable=self.category_var, 
            values=["All Categories", "Hardware", "Electrical", "Plumbing", "Paint", "Tools"],
            state="readonly"
        )
        category_combo.current(0)
        category_combo.grid(row=3, column=1, sticky="we", padx=5, pady=5)

        # 4. 'In Stock Only' (Checkbox)
        stock_label = ttk.Label(main_frame, text="Filters:")
        stock_label.grid(row=4, column=0, sticky="e", padx=(0, 10), pady=5)
        
        self.in_stock_var = tk.BooleanVar(value=True)
        in_stock_check = ttk.Checkbutton(
            main_frame, 
            text="In Stock Only", 
            variable=self.in_stock_var,
            bootstyle="primary"
        )
        in_stock_check.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        # 5. 'Show Inactive' (Switch/Toggle)
        self.inactive_var = tk.BooleanVar(value=False)
        inactive_switch = ttk.Checkbutton(
            main_frame, 
            text="Show Inactive/Discontinued",
            variable=self.inactive_var,
            bootstyle="primary-round-toggle" # This makes it a switch
        )
        inactive_switch.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        # 6. Sort By (Radio Buttons)
        sort_label = ttk.Label(main_frame, text="Sort By:")
        sort_label.grid(row=6, column=0, sticky="e", padx=(0, 10), pady=5)
        
        self.sort_var = tk.StringVar(value="Relevance")
        
        sort_frame = ttk.Frame(main_frame)
        sort_frame.grid(row=6, column=1, sticky="w")

        sort_radio1 = ttk.Radiobutton(sort_frame, text="Relevance", variable=self.sort_var, value="Relevance", bootstyle="primary")
        sort_radio1.pack(side="left", padx=5)
        
        sort_radio2 = ttk.Radiobutton(sort_frame, text="Price", variable=self.sort_var, value="Price", bootstyle="primary")
        sort_radio2.pack(side="left", padx=5)
        
        sort_radio3 = ttk.Radiobutton(sort_frame, text="Name (A-Z)", variable=self.sort_var, value="Name", bootstyle="primary")
        sort_radio3.pack(side="left", padx=5)

        # 7. Hidden Field (for demonstration)
        self.hidden_session_id = "user_session_abc123"
        # (Control count: 7 visible + 1 hidden = 8)

        # --- Error Message Label ---
        self.error_label = ttk.Label(
            main_frame, 
            text="", 
            bootstyle="danger", 
            font=("Helvetica", 9)
        )
        self.error_label.grid(row=7, column=0, columnspan=2, pady=(10, 0))

        # --- Button Frame (8, 9, 10. Buttons) ---
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=8, column=0, columnspan=2, pady=15)

        submit_button = ttk.Button(
            button_frame, 
            text="Search", 
            command=self.validate_and_submit,
            bootstyle="primary"
        )
        submit_button.pack(side="left", padx=10, ipady=5)

        clear_button = ttk.Button(
            button_frame, 
            text="Clear Filters", 
            command=self.clear_form,
            bootstyle="secondary-outline"
        )
        clear_button.pack(side="left", padx=10, ipady=5)
        
        # 10. Back to Main Menu Button (NEWLY ADDED)
        back_button = ttk.Button(
            button_frame, 
            text="Back to Main Menu", 
            command=self.open_main_menu,
            bootstyle="danger-outline"
        )
        back_button.pack(side="left", padx=10, ipady=5)

        # --- Separator ---
        results_sep = ttk.Separator(main_frame, bootstyle="primary")
        results_sep.grid(row=9, column=0, columnspan=2, sticky="ew", pady=10)

        # --- Results Area ---
        results_label = ttk.Label(main_frame, text="Search Results:", font=("Helvetica", 12, "bold"))
        results_label.grid(row=10, column=0, columnspan=2, sticky="w", pady=5)
        
        # 11. Results Display (Textarea)
        self.results_text = tk.Text(
            main_frame, 
            height=10, 
            width=40, 
            font=("Helvetica", 10),
            wrap="word" # Wrap text
        )
        self.results_text.grid(row=11, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        # Start in a "disabled" state so user can't type
        self.results_text.config(state="disabled", foreground="black")


    def center_window(self):
        """Centers the window on the screen."""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    # --- (B) Form Validation and Functionality ---

    def validate_and_submit(self):
        """
        Performs validation and then "handles" the data.
        """
        self.error_label.config(text="") 
        
        # --- 1. Get all data ---
        search_term = self.search_var.get()
        search_by = self.search_by_var.get()
        category = self.category_var.get()
        in_stock = self.in_stock_var.get()
        show_inactive = self.inactive_var.get()
        sort_by = self.sort_var.get()

        # --- 2. Validation ---
        
        # Required field validation
        if search_term == "" or search_term == self.search_entry.placeholder:
            self.error_label.config(text="Error: Search term is required.")
            return

        # Format validation (e.g., length)
        if len(search_term) < 2:
            self.error_label.config(text="Error: Search term must be at least 2 characters.")
            return

        # --- 3. Functionality (Data Handling & UI Update) ---
        # If all validation passes, we "handle" the data.
        
        print("--- SEARCH QUERY (SUCCESS) ---")
        print(f"  Session ID: {self.hidden_session_id}")
        print(f"  Search Term: {search_term} (Searching in: {search_by})")
        print(f"  Category: {category}")
        print(f"  In Stock Only: {in_stock}")
        print(f"  Show Inactive: {show_inactive}")
        print(f"  Sort By: {sort_by}")
        print("---------------------------------")
        
        # --- Reflect results in UI ---
        # We enable the Text widget, write to it, then disable it again
        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END) # Clear previous results
        
        # Create mock results based on the search
        mock_results = f"Searching for '{search_term}' (Category: {category}, In Stock: {in_stock})...\n\n"
        mock_results += "Found 3 matching products:\n\n"
        mock_results += "1. [Hardware] Claw Hammer, 16oz\n"
        mock_results += "  ID: HW-0012\n"
        mock_results += "  Stock: 42 (Manila), 18 (Quezon City)\n"
        mock_results += "  Price: ₱350.00\n\n"
        
        mock_results += "2. [Tools] Hammer Drill, 18V Kit\n"
        mock_results += "  ID: TL-0004\n"
        mock_results += "  Stock: 8 (Manila)\n"
        mock_results += "  Price: ₱4,200.00\n\n"
        
        if not in_stock:
             mock_results += "3. [Hardware] Sledge Hammer, 8lb\n"
             mock_results += "  ID: HW-0045\n"
             mock_results += "  Stock: 0 (Out of Stock)\n"
             mock_results += "  Price: ₱875.00\n"

        self.results_text.insert("1.0", mock_results)
        self.results_text.config(state="disabled") # Make read-only


    def clear_form(self):
        """
        Resets all form controls to their default state.
        """
        # Reset StringVars/IntVars
        self.search_by_var.set("Any (All Fields)")
        self.category_var.set("All Categories")
        self.in_stock_var.set(True)
        self.inactive_var.set(False)
        self.sort_var.set("Relevance")
        
        # Reset search bar
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, self.search_entry.placeholder)
        self.search_entry.config(foreground='grey')
        
        # Clear results area
        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END)
        self.results_text.config(state="disabled")
        
        self.error_label.config(text="")
        
        # Put focus back on the first field
        self.search_entry.focus_set()

    def open_main_menu(self):
        """
        Closes the current window and launches the main menu application
        via a new subprocess, ensuring clean separation.
        """
        self.destroy() # Close the search window
        try:
            # Launch the main menu file (main_menu.py)
            subprocess.Popen([sys.executable, "main_menu.py"])
        except Exception as e:
            # Note: This error message will likely be missed as the window is closed,
            # but it is good practice to include it for debugging.
            print(f"Error launching main_menu.py: {e}")
            # If the launch fails, we can't show an error box easily, but we'll print to console.


# --- Main execution ---
if __name__ == "__main__":
    app = ProductSearchApp()
    app.mainloop()