import customtkinter as ctk

class ProjectFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self