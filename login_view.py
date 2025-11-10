import tkinter as tk
from tkinter import ttk  # 'ttk' provides modern-looking widgets
from tkinter import messagebox

class App(tk.Tk):
    """
    Main application window for the Login Form.
    """
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.title("Company POS - Login")
        self.geometry("500x550")  # Set window size
        self.resizable(False, False)  # Prevent resizing
        
        # Configure a style for modern widgets
        style = ttk.Style(self)
        style.theme_use("clam") # You can also try "default", "alt", "classic"

        # --- Main Frame ---
        # We put all widgets inside a main frame with padding
        main_frame = ttk.Frame(self, padding="20 20 20 20")
        main_frame.pack(fill="both", expand=True)

        # --- Form Controls (Widgets) ---
        # We will use .grid() to arrange widgets in a clean label-input table
        
        # 1. Form Title (Label)
        title_label = ttk.Label(main_frame, text="System Login", font=("Helvetica", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # --- Helper Text (Placeholder) Logic ---
        # We define functions to add/remove placeholder text on focus
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
        username_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        # 3. Username (Textbox / Entry)
        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(main_frame, textvariable=self.username_var, width=40, font=("Helvetica", 10))
        self.username_entry.placeholder = "e.g., ana@company.com"
        self.username_entry.widgetName = "usernameEntry" # Custom property
        self.username_entry.insert(0, self.username_entry.placeholder)
        self.username_entry.config(foreground='grey')
        self.username_entry.bind("<FocusIn>", on_focus_in)
        self.username_entry.bind("<FocusOut>", on_focus_out)
        self.username_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        # 4. Password (Label)
        password_label = ttk.Label(main_frame, text="Password:")
        password_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        # 5. Password (Password / Entry)
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(main_frame, textvariable=self.password_var, width=40, font=("Helvetica", 10))
        self.password_entry.placeholder = "Must be at least 8 characters"
        self.password_entry.widgetName = "passwordEntry" # Custom property
        self.password_entry.insert(0, self.password_entry.placeholder)
        self.password_entry.config(foreground='grey', show="") # Show placeholder text
        self.password_entry.bind("<FocusIn>", on_focus_in)
        self.password_entry.bind("<FocusOut>", on_focus_out)
        self.password_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        # 6. "Remember Me" (Checkbox)
        self.remember_var = tk.BooleanVar(value=False)
        remember_check = ttk.Checkbutton(
            main_frame, 
            text="Remember me for 30 days", 
            variable=self.remember_var
        )
        remember_check.grid(row=3, column=1, sticky="w", padx=5, pady=10)

        # 7. & 8. Role Selection (Radio Buttons)
        role_label = ttk.Label(main_frame, text="Login As:")
        role_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        
        self.role_var = tk.StringVar(value="User") # Default value
        
        role_frame = ttk.Frame(main_frame) # Frame to hold the radio buttons
        role_frame.grid(row=4, column=1, sticky="w")

        user_radio = ttk.Radiobutton(role_frame, text="User", variable=self.role_var, value="User")
        user_radio.pack(side="left", padx=5)
        
        admin_radio = ttk.Radiobutton(role_frame, text="Admin", variable=self.role_var, value="Admin")
        admin_radio.pack(side="left", padx=5)

        # 9. Location (Dropdown / Select / Combobox)
        location_label = ttk.Label(main_frame, text="Store Location:")
        location_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        
        self.location_var = tk.StringVar()
        location_combo = ttk.Combobox(
            main_frame, 
            textvariable=self.location_var, 
            values=["Manila Branch", "Quezon City Branch", "Remote (Home)"],
            state="readonly" # Prevents user from typing a new value
        )
        location_combo.current(0) # Set default selection
        # --- This line is changed ---
        location_combo.grid(row=5, column=1, sticky="we", padx=5, pady=5)

        # --- Error Message Label ---
        # This label is initially empty and will show validation errors
        self.error_label = ttk.Label(main_frame, text="", foreground="red", font=("Helvetica", 9))
        self.error_label.grid(row=6, column=0, columnspan=2, pady=10)

        # --- Button Frame ---
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=20)

        # 10. Submit Button
        # Descriptive label: "Login"
        submit_button = ttk.Button(
            button_frame, 
            text="Login Securely", 
            command=self.validate_and_submit
        )
        submit_button.pack(side="left", padx=10, ipady=5) # ipady = internal padding

        # 11. Reset/Clear Button
        # Descriptive label: "Clear Form"
        clear_button = ttk.Button(
            button_frame, 
            text="Clear Form", 
            command=self.clear_form
        )
        clear_button.pack(side="left", padx=10, ipady=5)

        # --- Tab Index / Keyboard Navigation ---
        # The .grid() layout automatically handles tabindex in the
        # order we created the widgets, which is logical (top-to-bottom).
        # We can also be explicit, but it's not needed here.
        # self.username_entry.focus_set() # Start with username selected

    # --- (B) Form Validation and Functionality ---

    def validate_and_submit(self):
        """
        Performs validation and then "handles" the data.
        This function is called when the "Login Securely" button is pressed.
        """
        self.error_label.config(text="") # Clear previous errors
        
        # Get all values from the form variables
        username = self.username_var.get()
        password = self.password_var.get()
        remember_me = self.remember_var.get()
        role = self.role_var.get()
        location = self.location_var.get()

        # --- 1. Validation ---

        # Check for required fields (and placeholder text)
        if username == "" or username == self.username_entry.placeholder:
            self.error_label.config(text="Error: Username is required.")
            return # Stop submission

        if password == "" or password == self.password_entry.placeholder:
            self.error_label.config(text="Error: Password is required.")
            return # Stop submission
        
        # Check for email format (simple check)
        if "@" not in username or "." not in username:
            self.error_label.config(text="Error: Invalid username. Must be an email.")
            return # Stop submission

        # Check for password length (format validation)
        if len(password) < 8:
            self.error_label.config(text="Error: Password must be at least 8 characters.")
            return # Stop submission

        # --- 2. Functionality (Data Handling) ---
        # All validation passed!
        
        # In a real app, you would send this to a database.
        # For this assignment, we will print it to the console
        # to prove the data was handled.
        
        print("--- LOGIN ATTEMPT (SUCCESS) ---")
        print(f"  Username: {username}")
        print(f"  Password: {password}") # Never print passwords in a real app!
        print(f"  Remember Me: {remember_me}")
        print(f"  Login Role: {role}")
        print(f"  Location: {location}")
        print("---------------------------------")
        
        # Show a success message in the UI
        messagebox.showinfo(
            "Login Successful", 
            f"Welcome, {username}!\n\nYou have logged in as an '{role}' at the '{location}'."
        )
        
        # Optionally, you can clear the form after success
        self.clear_form()


    def clear_form(self):
        """
        Resets all form controls to their default state.
        This is called by the "Clear Form" button.
        """
        # Clear Textboxes and add placeholders back
        self.username_entry.delete(0, tk.END)
        self.username_entry.insert(0, self.username_entry.placeholder)
        self.username_entry.config(foreground='grey')
        
        self.password_entry.delete(0, tk.END)
        self.password_entry.config(show="") # Unhide to show placeholder
        self.password_entry.insert(0, self.password_entry.placeholder)
        self.password_entry.config(foreground='grey')
        
        # Reset other controls
        self.remember_var.set(False)
        self.role_var.set("User")
        self.location_var.set("Manila Branch") # Or use .current(0)
        
        # Clear error message
        self.error_label.config(text="")
        
        # Put focus back on the first field
        self.username_entry.focus_set()


# --- Main execution ---
if __name__ == "__main__":
    app = App()
    app.mainloop()  # Starts the application's event loop