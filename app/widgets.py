import customtkinter as ctk

class StyledEntry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            font=("Poppins", 14),
            fg_color="#212121",
            text_color="white",
            border_width=1,
            border_color="#1E88E5",
            corner_radius=10,
            height=50
        )

class StyledButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            font=("Poppins", 14, "bold"),
            fg_color="#1E88E5",
            text_color="white",
            hover_color="#1565C0",
            corner_radius=10,
            border_width=0,
            height=50,
            width=150,
        )

