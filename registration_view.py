import customtkinter as ctk
from tkinter import messagebox

class RegistrationFrame(ctk.CTkFrame):
    """
    Modernized registration form UI with validation and error messages.
    """
    def __init__(self, master):
        super().__init__(master)
        
        # --- FRAME DESIGN SETTINGS ---
        self.configure(corner_radius=15)
        self.grid_columnconfigure((0, 1), weight=1)

        # Page Title
        self.title = ctk.CTkLabel(self, text="🧾 Create New Account", 
                                  font=ctk.CTkFont(size=22, weight="bold"))
        self.title.grid(row=0, column=0, columnspan=2, pady=(25, 10))

        # --- FORM ENTRIES ---
        self.first_name_label = ctk.CTkLabel(self, text="First Name *")
        self.first_name_label.grid(row=1, column=0, sticky="w", padx=25, pady=(10, 0))
        self.first_name_entry = ctk.CTkEntry(self, placeholder_text="e.g., Ana Pauline")
        self.first_name_entry.grid(row=2, column=0, padx=25, pady=(0, 10), sticky="ew")

        self.last_name_label = ctk.CTkLabel(self, text="Last Name *")
        self.last_name_label.grid(row=1, column=1, sticky="w", padx=25, pady=(10, 0))
        self.last_name_entry = ctk.CTkEntry(self, placeholder_text="e.g., Cruz")
        self.last_name_entry.grid(row=2, column=1, padx=25, pady=(0, 10), sticky="ew")

        self.username_label = ctk.CTkLabel(self, text="Username * (min 5 characters)")
        self.username_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=25, pady=(10, 0))
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Minimum 5 characters")
        self.username_entry.grid(row=4, column=0, columnspan=2, padx=25, pady=(0, 10), sticky="ew")

        self.password_label = ctk.CTkLabel(self, text="Password *")
        self.password_label.grid(row=5, column=0, sticky="w", padx=25, pady=(10, 0))
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Create a secure password", show="*")
        self.password_entry.grid(row=6, column=0, padx=25, pady=(0, 10), sticky="ew")

        self.confirm_pass_label = ctk.CTkLabel(self, text="Confirm Password *")
        self.confirm_pass_label.grid(row=5, column=1, sticky="w", padx=25, pady=(10, 0))
        self.confirm_pass_entry = ctk.CTkEntry(self, placeholder_text="Re-type your password", show="*")
        self.confirm_pass_entry.grid(row=6, column=1, padx=25, pady=(0, 10), sticky="ew")

        self.email_label = ctk.CTkLabel(self, text="Email Address *")
        self.email_label.grid(row=7, column=0, columnspan=2, sticky="w", padx=25, pady=(10, 0))
        self.email_entry = ctk.CTkEntry(self, placeholder_text="user@example.com")
        self.email_entry.grid(row=8, column=0, columnspan=2, padx=25, pady=(0, 10), sticky="ew")

        self.role_label = ctk.CTkLabel(self, text="Account Role *")
        self.role_label.grid(row=9, column=0, sticky="w", padx=25, pady=(10, 0))
        self.role_var = ctk.StringVar(value="Employee")
        self.role_dropdown = ctk.CTkComboBox(self, values=["Employee", "Admin"],
                                             variable=self.role_var, state="readonly")
        self.role_dropdown.grid(row=10, column=0, padx=25, pady=(0, 10), sticky="ew")

        self.emp_id_label = ctk.CTkLabel(self, text="Employee ID * (5-digits)")
        self.emp_id_label.grid(row=9, column=1, sticky="w", padx=25, pady=(10, 0))
        self.emp_id_entry = ctk.CTkEntry(self, placeholder_text="e.g., 10001")
        self.emp_id_entry.grid(row=10, column=1, padx=25, pady=(0, 10), sticky="ew")

        self.date_hired_label = ctk.CTkLabel(self, text="Date of Hire (Optional)")
        self.date_hired_label.grid(row=11, column=0, sticky="w", padx=25, pady=(10, 0))
        self.date_hired_entry = ctk.CTkEntry(self, placeholder_text="YYYY-MM-DD")
        self.date_hired_entry.grid(row=12, column=0, padx=25, pady=(0, 15), sticky="ew")

        self.terms_var = ctk.StringVar(value="off")
        self.terms_check = ctk.CTkCheckBox(self, text="I agree to the Terms of Service *",
                                           variable=self.terms_var, onvalue="on", offvalue="off")
        self.terms_check.grid(row=13, column=0, columnspan=2, padx=25, pady=10, sticky="w")

        # Message label for feedback
        self.message_label = ctk.CTkLabel(self, text="", text_color="red")
        self.message_label.grid(row=14, column=0, columnspan=2, padx=25, pady=(0, 10), sticky="w")

        # Buttons
        self.reset_button = ctk.CTkButton(self, text="Reset Form", fg_color="gray", command=self.reset_form)
        self.reset_button.grid(row=15, column=0, padx=25, pady=20, sticky="w")

        self.submit_button = ctk.CTkButton(self, text="Register", command=self.submit_registration_placeholder)
        self.submit_button.grid(row=15, column=1, padx=25, pady=20, sticky="e")

    # --- FORM FUNCTIONS ---

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
        """Frontend validation with error messages."""
        fname = self.first_name_entry.get().strip()
        lname = self.last_name_entry.get().strip()
        uname = self.username_entry.get().strip()
        pwd = self.password_entry.get().strip()
        cpwd = self.confirm_pass_entry.get().strip()
        email = self.email_entry.get().strip()
        emp_id = self.emp_id_entry.get().strip()
        terms = self.terms_var.get()

        # --- VALIDATIONS ---
        if not fname or not lname or not uname or not pwd or not cpwd or not email or not emp_id:
            self.message_label.configure(text="⚠️ Please fill in all required fields.", text_color="red")
            return

        if len(uname) < 5:
            self.message_label.configure(text="⚠️ Username must be at least 5 characters long.", text_color="red")
            return

        if pwd != cpwd:
            self.message_label.configure(text="⚠️ Passwords do not match.", text_color="red")
            return

        if not emp_id.isdigit() or len(emp_id) != 5:
            self.message_label.configure(text="⚠️ Employee ID must be a 5-digit number.", text_color="red")
            return

        if "@" not in email or "." not in email:
            self.message_label.configure(text="⚠️ Please enter a valid email address.", text_color="red")
            return

        if terms != "on":
            self.message_label.configure(text="⚠️ You must agree to the Terms of Service.", text_color="red")
            return

        # --- SUCCESS MESSAGE ---
        self.message_label.configure(text="✅ Registration successful!", text_color="green")
        print(f"Registered user: {uname}, Role: {self.role_var.get()}")

# Run as standalone window
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("JBSON Hardware - User Registration")
    app.geometry("720x750")

    frame = RegistrationFrame(app)
    frame.pack(fill="both", expand=True, padx=15, pady=15)

    app.mainloop()
