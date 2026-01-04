import customtkinter as ctk

class MusicFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        label = ctk.CTkLabel(self, text="Music Page!")
        label.pack(side="top", fill="x", pady=10)