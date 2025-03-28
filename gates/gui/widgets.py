import customtkinter as ctk

class StyledEntry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            font=("Poppins", 14),
            fg_color="#212121",     # Background color
            text_color="white",     # Text color
            border_width=1,
            border_color="#1E88E5",
            corner_radius=10        # Rounded corners
        )

class StyledButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            font=("Poppins", 14, "bold"),
            fg_color="#1E88E5",     # Button color
            text_color="white",
            hover_color="#1565C0",
            corner_radius=10,       # Rounded corners
            border_width=0
        )

