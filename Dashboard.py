import tkinter
import customtkinter
import time
import sys

from helper_funcs import get_date

from calendar_module.calendar_frame import CalendarApp
from home_module.home_frame import TempHomeApp
from pomodoro_module.pomo_frame import PomodoroFrame


class Dashboard(customtkinter.CTk):
    def __init__(self):

        # Initiailze Frame
        super().__init__()
        self.title("Personal Organizer")
        self.geometry("1200x800")

        # Configure Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ========= SIDEBAR FRAME =========
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # ========= APP LOGO LABEL =========
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text=get_date(), 
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # ========= HOME BUTTON =========
        self.home_button = customtkinter.CTkButton(
            self.sidebar_frame, 
            text="Home", 
            command=self.show_home
        )
        self.home_button.grid(row=1, column=0, padx=20, pady=10)

        # ========= CALENDAR WORK =========
        self.calendar_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Calendar", 
            command=self.show_calendar
        )
        self.calendar_button.grid(row=2, column=0, padx=20, pady=10)

        # ========= POMODORO WORK =========
        self.pomo_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Pomodoro",
            command=self.show_pomo
        )
        self.pomo_button.grid(row=3, column=0, padx=20, pady=10)

        # ========= MAIN CONTAINER =========
        self.container = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.container.grid(row=0, column=1, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # ========= STACK ALL FRAMES =========
        self.frames = {}

        # Create the home frame
        self.frames["Home"] = TempHomeApp(parent=self.container)
        self.frames["Home"].grid(row=0, column=0, sticky="nsew")

        # Create the calendar frame
        self.frames["Calendar"] = CalendarApp(parent=self.container)
        self.frames["Calendar"].grid(row=0, column=0, sticky="nsew")

        # Create the pomodoro frame
        self.frames["Pomodoro"] = PomodoroFrame(parent=self.container)
        self.frames["Pomodoro"].grid(row=0, column=0, sticky="nsew")

        self.show_home()

    
    def show_home(self):
        """Raise the home frame to the top of the main container."""
        self.frames["Home"].tkraise()
    

    def show_calendar(self):
        """Raise the calendar frame to the top of the main container."""
        self.frames["Calendar"].tkraise()
    
    
    def show_pomo(self):
        """Raise the pomodoro frame to the top of the main container."""
        self.frames["Pomodoro"].tkraise()