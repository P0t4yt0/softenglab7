import tkinter as tk
# Import ttkbootstrap instead of tkinter.ttk
import ttkbootstrap as ttk
from tkinter import messagebox
# In a real app, you'd import bcrypt
# import bcrypt 

class App(ttk.Window): # Inherit from ttk.Window
    """
    Main application window for the Login Form.
    """
    def __init__(self):
        # Use super() with a theme
        # Other good themes: "superhero" (dark), "pulse", "cosmo"
        super().__init__(themename="litera")

        # --- Window Configuration (Aligned with Scope) ---
        self.title("JBSON Hardware - POS & Inventory System") # Changed Title
        self.geometry("500x550")
        self.resizable(False, False)
        
        # Call the new centering function
        self.center_window()

        # --- Main Frame ---
        main_frame = ttk.Frame(self, padding="20 20 20 20")
        main_frame.pack(fill="both", expand=True)

        # --- IMPORTANT: Column Configuration ---
        main_frame.columnconfigure(1, weight=1)

        # --- Form Controls (Widgets) ---
        
        # 1. Form Title (Label)
        title_label = ttk.Label(
            main_frame, 
            text="System Login", 
            font=("Helvetica", 18, "bold"),
            bootstyle="primary" 
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # --- Helper Text (Placeholder) Logic ---
        # (This logic is excellent and unchanged)
        def on_focus_in(event):
            """Called when the widget gets focus."""
            widget = event.widget
            if widget.get() == widget.placeholder:
                widget.delete(0, tk.END)
                widget.config(foreground='black')
                if widget.widgetName == "passwordEntry":
                    widget.config(show="*")

        def on_focus_out(event):
            """Called when the widget loses focus."""
            widget = event.widget
            if not widget.get():
                if widget.widgetName == "passwordEntry":
                    widget.config(show="")
                widget.insert(0, widget.placeholder)
                widget.config(foreground='grey')

        # 2. Username (Label)
        username_label = ttk.Label(main_frame, text="Username (Email):")
        username_label.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)

        # 3. Username (Textbox / Entry)
        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(main_frame, textvariable=self.username_var, width=40, font=("Helvetica", 10))
        self.username_entry.placeholder = "e.g., employee@jbson.com" # Changed placeholder
        self.username_entry.widgetName = "usernameEntry"
        self.username_entry.insert(0, self.username_entry.placeholder)
        self.username_entry.config(foreground='grey')
        self.username_entry.bind("<FocusIn>", on_focus_in)
        self.username_entry.bind("<FocusOut>", on_focus_out)
        self.username_entry.grid(row=1, column=1, sticky="we", padx=5, pady=5)

        # 4. Password (Label)
        password_label = ttk.Label(main_frame, text="Password:")
        password_label.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)

        # 5. Password (Password / Entry)
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(main_frame, textvariable=self.password_var, width=40, font=("Helvetica", 10))
        self.password_entry.placeholder = "Must be at least 8 characters"
        self.password_entry.widgetName = "passwordEntry"
        self.password_entry.insert(0, self.password_entry.placeholder)
        self.password_entry.config(foreground='grey', show="")
        self.password_entry.bind("<FocusIn>", on_focus_in)
        self.password_entry.bind("<FocusOut>", on_focus_out)
        self.password_entry.grid(row=2, column=1, sticky="we", padx=5, pady=5)

        # 6. "Remember Me" (Checkbox)
        self.remember_var = tk.BooleanVar(value=False)
        remember_check = ttk.Checkbutton(
            main_frame, 
            text="Remember me for 30 days", 
            variable=self.remember_var,
            bootstyle="primary" 
        )
        remember_check.grid(row=3, column=1, sticky="w", padx=5, pady=10)

        # 7. & 8. Role Selection (Radio Buttons) - MODIFIED FOR SCOPE
        role_label = ttk.Label(main_frame, text="Login As:")
        role_label.grid(row=4, column=0, sticky="e", padx=(0, 10), pady=5)
        
        # Scope defines "Administrator" and "Employee"
        self.role_var = tk.StringVar(value="Employee") # Changed default
        
        role_frame = ttk.Frame(main_frame)
        role_frame.grid(row=4, column=1, sticky="w")

        # Changed to "Employee"
        user_radio = ttk.Radiobutton(role_frame, text="Employee", variable=self.role_var, value="Employee", bootstyle="primary")
        user_radio.pack(side="left", padx=5)
        
        # Changed to "Administrator"
        admin_radio = ttk.Radiobutton(role_frame, text="Administrator", variable=self.role_var, value="Administrator", bootstyle="primary")
        admin_radio.pack(side="left", padx=5)

        # 9. Location (Dropdown / Select / Combobox)
        location_label = ttk.Label(main_frame, text="Store Location:")
        location_label.grid(row=5, column=0, sticky="e", padx=(0, 10), pady=5)
        
        self.location_var = tk.StringVar()
        location_combo = ttk.Combobox(
            main_frame, 
            textvariable=self.location_var, 
            values=["Manila Branch", "Quezon City Branch", "Remote (Home)"],
            state="readonly"
        )
        location_combo.current(0)
        location_combo.grid(row=5, column=1, sticky="we", padx=5, pady=5)

        # --- Error Message Label ---
        self.error_label = ttk.Label(
            main_frame, 
            text="", 
            bootstyle="danger", 
            font=("Helvetica", 9)
        )
        self.error_label.grid(row=6, column=0, columnspan=2, pady=10)

        # --- Button Frame ---
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=20)

        # 10. Submit Button
        submit_button = ttk.Button(
            button_frame, 
            text="Login Securely", 
            command=self.validate_and_submit,
            bootstyle="primary" 
        )
        submit_button.pack(side="left", padx=10, ipady=5)

        # 11. Reset/Clear Button
        clear_button = ttk.Button(
            button_frame, 
            text="Clear Form", 
            command=self.clear_form,
            bootstyle="secondary-outline" 
        )
        clear_button.pack(side="left", padx=10, ipady=5)

    
    def center_window(self):
        """Centers the window on the screen."""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')


    # --- (B) Form Validation and Functionality (Modified for Scope) ---

    def validate_and_submit(self):
        """
        Performs validation and then "handles" the data.
        """
        self.error_label.config(text="") 
        
        username = self.username_var.get()
        password = self.password_var.get()
        remember_me = self.remember_var.get()
        role = self.role_var.get()
        location = self.location_var.get()

        # --- 1. Validation (Same as before) ---
        if username == "" or username == self.username_entry.placeholder:
            self.error_label.config(text="Error: Username is required.")
            return

        if password == "" or password == self.password_entry.placeholder:
            self.error_label.config(text="Error: Password is required.")
            return
        
        if "@" not in username or "." not in username:
            self.error_label.config(text="Error: Invalid username. Must be an email.")
            return

        if len(password) < 8:
            self.error_label.config(text="Error: Password must be at least 8 characters.")
            return

        # --- 2. Functionality (Simulating Scope Logic) ---
        
        # SCOPE: "applies a bcrypt hashing algorithm"
        # In a real app, you would not have the password. You would:
        # 1. Fetch the hashed_password from the MySQL 8.4 database for this 'username'.
        # 2. Check it: 
        #    is_valid = bcrypt.checkpw(password.encode('utf-8'), hashed_password_from_db)
        # 3. If is_valid is False, show an error.
        
        # --- MOCK AUTHENTICATION (for this demo) ---
        # We'll pretend to check credentials
        if (username == "admin@jbson.com" and password == "AdminPass123" and role == "Administrator") or \
           (username == "employee@jbson.com" and password == "EmployeePass123" and role == "Employee"):
            
            # SCOPE: "Activity Log module ... records activities such as logins"
            print("--- LOGIN ATTEMPT (SUCCESS) ---")
            print(f"  [Activity Log]: User '{username}' ({role}) logged in at {location}.")
            print(f"  Username: {username}")
            print(f"  Password: {password} (in a real app, you'd never print this!)")
            print(f"  Remember Me: {remember_me}")
            print(f"  Login Role: {role}")
            print(f"  Location: {location}")
            print("---------------------------------")
            
            messagebox.showinfo(
                "Login Successful", 
                f"Welcome, {username}!\n\nYou have logged in as an '{role}' at the '{location}'."
            )
            
            # Here you would destroy this window and open the main app window
            # self.destroy() 
            # main_app = MainApplication(role) # Pass the role to the main app
            
            self.clear_form()
            
        else:
            # Failed login
            # SCOPE: "Activity Log module ... records activities" (e.g., failed logins)
            print(f"[Activity Log]: FAILED login attempt for user '{username}'.")
            self.error_label.config(text="Error: Invalid username, password, or role.")
            return


    def clear_form(self):
        """
        Resets all form controls to their default state.
        """
        self.username_entry.delete(0, tk.END)
        self.username_entry.insert(0, self.username_entry.placeholder)
        self.username_entry.config(foreground='grey')
        
        self.password_entry.delete(0, tk.END)
        self.password_entry.config(show="")
        self.password_entry.insert(0, self.password_entry.placeholder)
        self.password_entry.config(foreground='grey')
        
        self.remember_var.set(False)
        self.role_var.set("Employee") # Changed to scope default
        self.location_var.set("Manila Branch")
        
        self.error_label.config(text="")
        
        # Put focus back on the first field
        self.username_entry.focus_set()


# --- Main execution ---
if __name__ == "__main__":
    app = App()
    app.mainloop()