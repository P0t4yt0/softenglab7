import customtkinter as ctk

class RegistrationFrame(ctk.CTkFrame):
    """
    This frame contains the complete user registration form's FRONTEND.
    It includes all 10+ form controls (widgets) laid out on the screen.
    The validation and database logic will be added later.
    """
    def __init__(self, master):
        super().__init__(master)
        
        # Configure the grid to make widgets expand
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # 1. Page Title
        self.title = ctk.CTkLabel(self, text="Create New Account", font=ctk.CTkFont(size=20, weight="bold"))
        self.title.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10))

        # --- Form Controls (Widgets) ---
        
        # 1. First Name (Textbox)
        self.first_name_label = ctk.CTkLabel(self, text="First Name *")
        self.first_name_label.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="w")
        self.first_name_entry = ctk.CTkEntry(self, placeholder_text="e.g., Ana Pauline")
        self.first_name_entry.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")

        # 2. Last Name (Textbox)
        self.last_name_label = ctk.CTkLabel(self, text="Last Name *")
        self.last_name_label.grid(row=1, column=1, padx=20, pady=(10, 0), sticky="w")
        self.last_name_entry = ctk.CTkEntry(self, placeholder_text="e.g., Cruz")
        self.last_name_entry.grid(row=2, column=1, padx=20, pady=(0, 10), sticky="ew")

        # 3. Username (Textbox)
        self.username_label = ctk.CTkLabel(self, text="Username * (min 5 characters)")
        self.username_label.grid(row=3, column=0, padx=20, pady=(10, 0), sticky="w")
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Minimum 5 characters")
        self.username_entry.grid(row=4, column=0, columnspan=2, padx=20, pady=(0, 10), sticky="ew")

        # 4. Password (Password)
        self.password_label = ctk.CTkLabel(self, text="Password *")
        self.password_label.grid(row=5, column=0, padx=20, pady=(10, 0), sticky="w")
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Create a secure password", show="*")
        self.password_entry.grid(row=6, column=0, padx=20, pady=(0, 10), sticky="ew")

        # 5. Confirm Password (Password)
        self.confirm_pass_label = ctk.CTkLabel(self, text="Confirm Password *")
        self.confirm_pass_label.grid(row=5, column=1, padx=20, pady=(10, 0), sticky="w")
        self.confirm_pass_entry = ctk.CTkEntry(self, placeholder_text="Re-type your password", show="*")
        self.confirm_pass_entry.grid(row=6, column=1, padx=20, pady=(0, 10), sticky="ew")
        
        # 6. Email (Email)
        self.email_label = ctk.CTkLabel(self, text="Email Address *")
        self.email_label.grid(row=7, column=0, padx=20, pady=(10, 0), sticky="w")
        self.email_entry = ctk.CTkEntry(self, placeholder_text="user@example.com")
        self.email_entry.grid(row=8, column=0, columnspan=2, padx=20, pady=(0, 10), sticky="ew")

        # 7. Role (Dropdown/Select) - Matches your 2-level system
        self.role_label = ctk.CTkLabel(self, text="Account Role *")
        self.role_label.grid(row=9, column=0, padx=20, pady=(10, 0), sticky="w")
        self.role_var = ctk.StringVar(value="Employee")
        self.role_dropdown = ctk.CTkComboBox(self, 
                                             values=["Employee", "Admin"],
                                             variable=self.role_var,
                                             state="readonly")
        self.role_dropdown.grid(row=10, column=0, padx=20, pady=(0, 10), sticky="ew")

        # 8. Employee ID (Number)
        self.emp_id_label = ctk.CTkLabel(self, text="Employee ID * (5-digits)")
        self.emp_id_label.grid(row=9, column=1, padx=20, pady=(10, 0), sticky="w")
        self.emp_id_entry = ctk.CTkEntry(self, placeholder_text="e.g., 10001")
        self.emp_id_entry.grid(row=10, column=1, padx=20, pady=(0, 10), sticky="ew")

        # 9. Date of Hire (Date)
        self.date_hired_label = ctk.CTkLabel(self, text="Date of Hire (Optional)")
        self.date_hired_label.grid(row=11, column=0, padx=20, pady=(10, 0), sticky="w")
        self.date_hired_entry = ctk.CTkEntry(self, placeholder_text="YYYY-MM-DD")
        self.date_hired_entry.grid(row=12, column=0, padx=20, pady=(0, 20), sticky="ew")

        # 10. Terms (Checkbox)
        self.terms_var = ctk.StringVar(value="off")
        self.terms_check = ctk.CTkCheckBox(self, text="I agree to the Terms of Service *",
                                           variable=self.terms_var, onvalue="on", offvalue="off")
        self.terms_check.grid(row=13, column=0, columnspan=2, padx=20, pady=10, sticky="w")
        
        # 11. Error/Success Message Label
        self.message_label = ctk.CTkLabel(self, text="", text_color="red")
        self.message_label.grid(row=14, column=0, columnspan=2, padx=20, pady=(0, 10), sticky="w")

        # 12. Submit Button
        self.submit_button = ctk.CTkButton(self, text="Register", command=self.submit_registration_placeholder)
        self.submit_button.grid(row=15, column=1, padx=20, pady=20, sticky="e")
        
        # 13. Reset Button
        self.reset_button = ctk.CTkButton(self, text="Reset Form", command=self.reset_form, fg_color="gray")
        self.reset_button.grid(row=15, column=0, padx=20, pady=20, sticky="w")

    def reset_form(self):
        """Clears all entry fields and resets the form."""
        self.first_name_entry.delete(0, 'end')
        self.last_name_entry.delete(0, 'end')
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.confirm_pass_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.emp_id_entry.delete(0, 'end')
        self.date_hired_entry.delete(0, 'end')
        self.role_var.set("Employee")
        self.terms_var.set("off")
        self.message_label.configure(text="")

    def submit_registration_placeholder(self):
        """
        This is a PLACEHOLDER function for the frontend.
        It just shows the developer that the button is working.
        We will add the validation and database logic here later.
        """
        print("Registration button clicked!")
        
        # Example of showing a temporary message:
        self.message_label.configure(text="Registration logic not implemented yet.", text_color="gray")
        
        # You can also read the values to test them
        print(f"Username: {self.username_entry.get()}")
        print(f"Role: {self.role_var.get()}")
        print(f"Terms agreed: {self.terms_var.get()}")


# This 'if' block lets you run and test this file by itself.
if __name__ == "__main__":
    # This just runs a test window if you execute this file directly
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    app = ctk.CTk()
    app.title("JBSON Hardware - User Registration")
    app.geometry("700x700")
    
    frame = RegistrationFrame(app)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    app.mainloop()