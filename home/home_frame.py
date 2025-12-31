import customtkinter as ctk

class TempHomeApp(ctk.CTkFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Home page!")
        label.pack(side="top", fill="x", pady=10)