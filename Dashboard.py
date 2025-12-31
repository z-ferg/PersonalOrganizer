import tkinter
import customtkinter
import time

from helper_funcs import get_date

class Dashboard(customtkinter.CTk):
    def __init__(self):

        # Initiailze Frame
        super().__init__()
        self.title("Personal Organizer")
        self.geometry("800x600")

        # Configure Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ========= SIDEBAR FRAME =========
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # ========= APP LOGO LABEL =========
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text=get_date(), font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # ========= HOME BUTTON =========
        self.home_button = customtkinter.CTkButton(self.sidebar_frame, text="Home", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, padx=20, pady=10)

        # ========= FINANCE WORK =========
        self.finance_button = customtkinter.CTkButton(self.sidebar_frame, text="Personal Finance", command=self.finance_button_event)
        self.finance_button.grid(row=2, column=0, padx=20, pady=10)

        # ========= MAIN FRAME =========
        self.main_content_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_content_frame.grid(row=0, column=1, sticky="nsew")

        self.content_label = customtkinter.CTkLabel(self.main_content_frame, text="Welcome to Home Page!", font=("Roboto", 24))
        self.content_label.pack(padx=20, pady=20)

    def home_button_event(self):
        self.content_label.configure(text="Welcome to home page!")
    
    def finance_button_event(self):
        self.content_label.configure(text="Settings Panel (placeholder)")