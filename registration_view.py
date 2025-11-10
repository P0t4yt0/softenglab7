import customtkinter as ctk

class RegistrationFrame(ctk.CTkFrame):
    """
    Modernized Registration Form UI
    (Frontend only — all logic unchanged)
    """
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        # --- Card container for a clean centered layout ---
        self.card = ctk.CTkFrame(self, corner_radius=20, fg_color=("white", "#2a2d2e"))
        self.card.pack(expand=True, fill="both", padx=40, pady=40)

        # Grid config for responsiveness
        self.card.grid_columnconfigure((0, 1), weight=1)

        # --- Title ---
        self.title = ctk.CTkLabel(
            self.card,
            text="Create New Account",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color=("#1f1f1f", "white"),
        )
        self.title.grid(row=0, column=0, columnspan=2, pady=(20, 25))

        # --- Form Inputs ---
        entry_style = {"height": 40, "corner_radius": 12}

        # First Name
        self.first_name_label = ctk.CTkLabel(self.card, text="First Name *")
        self.first_name_label.grid(row=1, column=0, padx=20, sticky="w")
        self.first_name_entry = ctk.CTkEntry(self.card, placeholder_text="e.g., Ana Pauline", **entry_style)
        self.first_name_entry.grid(row=2, column=0, padx=20, pady=(0, 15), sticky="ew")

        # Last Name
        self.last_name_label = ctk.CTkLabel(self.card, text="Last Name *")
        self.last_name_label.grid(row=1, column=1, padx=20, sticky="w")
        self.last_name_entry = ctk.CTkEntry(self.card, placeholder_text="e.g., Cruz", **entry_style)
        self.last_name_entry.grid(row=2, column=1, padx=20, pady=(0, 15), sticky="ew")

        # Username
        self.username_label = ctk.CTkLabel(self.card, text="Username * (min 5 characters)")
        self.username_label.grid(row=3, column=0, columnspan=2, padx=20, sticky="w")
        self.username_entry = ctk.CTkEntry(self.card, placeholder_text="Minimum 5 characters", **entry_style)
        self.username_entry.grid(row=4, column=0, columnspan=2, padx=20, pady=(0, 15), sticky="ew")

        # Password
        self.password_label = ctk.CTkLabel(self.card, text="Password *")
        self.password_label.grid(row=5, column=0, padx=20, sticky="w")
        self.password_entry = ctk.CTkEntry(self.card, placeholder_text="Create a secure password", show="*", **entry_style)
        self.password_entry.grid(row=6, column=0, padx=20, pady=(0, 15), sticky="ew")

        # Confirm Password
        self.confirm_pass_label = ctk.CTkLabel(self.card, text="Confirm Password *")
        self.confirm_pass_label.grid(row=5, column=1, padx=20, sticky="w")
        self.confirm_pass_entry = ctk.CTkEntry(self.card, placeholder_text="Re-type your password", show="*", **entry_style)
        self.confirm_pass_entry.grid(row=6, column=1, padx=20, pady=(0, 15), sticky="ew")

        # Email
        self.email_label = ctk.CTkLabel(self.card, text="Email Address *")
        self.email_label.grid(row=7, column=0, columnspan=2, padx=20, sticky="w")
        self.email_entry = ctk.CTkEntry(self.card, placeholder_text="user@example.com", **entry_style)
        self.email_entry.grid(row=8, column=0, columnspan=2, padx=20, pady=(0, 15), sticky="ew")

        # Role
        self.role_label = ctk.CTkLabel(self.card, text="Account Role *")
        self.role_label.grid(row=9, column=0, padx=20, sticky="w")
        self.role_var = ctk.StringVar(value="Employee")
        self.role_dropdown = ctk.CTkComboBox(
            self.card, values=["Employee", "Admin"], variable=self.role_var, height=40, corner_radius=12
        )
        self.role_dropdown.grid(row=10, column=0, padx=20, pady=(0, 15), sticky="ew")

        # Employee ID
        self.emp_id_label = ctk.CTkLabel(self.card, text="Employee ID * (5-digits)")
        self.emp_id_label.grid(row=9, column=1, padx=20, sticky="w")
        self.emp_id_entry = ctk.CTkEntry(self.card, placeholder_text="e.g., 10001", **entry_style)
        self.emp_id_entry.grid(row=10, column=1, padx=20, pady=(0, 15), sticky="ew")

        # Date of Hire
        self.date_hired_label = ctk.CTkLabel(self.card, text="Date of Hire (Optional)")
        self.date_hired_label.grid(row=11, column=0, padx=20, sticky="w")
        self.date_hired_entry = ctk.CTkEntry(self.card, placeholder_text="YYYY-MM-DD", **entry_style)
        self.date_hired_entry.grid(row=12, column=0, padx=20, pady=(0, 15), sticky="ew")

        # Terms Checkbox
        self.terms_var = ctk.StringVar(value="off")
        self.terms_check = ctk.CTkCheckBox(
            self.card,
            text="I agree to the Terms of Service *",
            variable=self.terms_var,
            onvalue="on",
            offvalue="off",
        )
        self.terms_check.grid(row=13, column=0, columnspan=2, padx=20, pady=(5, 10), sticky="w")

        # Message label
        self.message_label = ctk.CTkLabel(self.card, text="", text_color="gray")
        self.message_label.grid(row=14, column=0, columnspan=2, padx=20, sticky="w")

        # Buttons
        self.button_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        self.button_frame.grid(row=15, column=0, columnspan=2, pady=20)

        self.reset_button = ctk.CTkButton(
            self.button_frame, text="Reset", fg_color="#6c757d", hover_color="#5a6268",
            corner_radius=10, width=120, command=self.reset_form
        )
        self.reset_button.pack(side="left", padx=10)

        self.submit_button = ctk.CTkButton(
            self.button_frame, text="Register", fg_color="#0078D7", hover_color="#005fa3",
            corner_radius=10, width=150, command=self.submit_registration_placeholder
        )
        self.submit_button.pack(side="left", padx=10)

    def reset_form(self):
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
        print("Registration button clicked!")
        self.message_label.configure(text="Registration logic not implemented yet.", text_color="gray")
        print(f"Username: {self.username_entry.get()}")
        print(f"Role: {self.role_var.get()}")
        print(f"Terms agreed: {self.terms_var.get()}")


# Preview window
if __name__ == "__main__":
    ctk.set_appearance_mode("light")  # Try "dark" for dark mode
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("JBSON Hardware - User Registration")
    app.geometry("720x780")

    frame = RegistrationFrame(app)
    frame.pack(fill="both", expand=True)

    app.mainloop()
