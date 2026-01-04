import customtkinter as ctk

class NotesFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        label = ctk.CTkLabel(self, text="Notes Page!")
        label.pack(side="top", fill="x", pady=10)