import tkinter
import customtkinter as ctk
import time
import sys

from helper_funcs import get_date

from calendar_module.calendar_frame import CalendarFrame
from home_module.home_frame import HomeFrame
from pomodoro_module.pomo_frame import PomodoroFrame
from projects_module.projects_frame import ProjectFrame
from music_module.music_frame import MusicFrame
from notes_module.notes_frame import NotesFrame


class Dashboard(ctk.CTk):
    def __init__(self):

        # Initiailze Frame
        super().__init__()
        self.title("Personal Organizer")
        self.geometry("1200x800")

        # Configure Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ========= SIDEBAR FRAME =========
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0,
                                            border_width=2)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(8, weight=1)

        # ========= APP LOGO LABEL =========
        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame,
            text=get_date(), 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # ========= HOME BUTTON =========
        self.home_button = ctk.CTkButton(
            self.sidebar_frame, 
            text="Home", 
            command=self.show_home
        )
        self.home_button.grid(row=1, column=0, padx=20, pady=10)

        # ========= CALENDAR WORK =========
        self.calendar_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Calendar", 
            command=self.show_calendar
        )
        self.calendar_button.grid(row=2, column=0, padx=20, pady=10)

        # ========= NOTES WORK =========
        self.notes_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Notes",
            command=self.show_notes
        )
        self.notes_button.grid(row=3, column=0, padx=20, pady=10)

        # ========= PROJECTS WORK =========
        self.projects_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Projects",
            command=self.show_projects
        )
        self.projects_button.grid(row=4, column=0, padx=20, pady=10)

        # ========= MUSIC WORK =========
        self.music_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Music",
            command=self.show_music
        )
        self.music_button.grid(row=5, column=0, padx=20, pady=10)

        # ========= POMODORO WORK =========
        self.pomo_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Pomodoro",
            command=self.show_pomo
        )
        self.pomo_button.grid(row=6, column=0, padx=20, pady=10)

        # ========= MAIN CONTAINER =========
        self.container = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.container.grid(row=0, column=1, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # =======   == STACK ALL FRAMES =========
        self.frames = {}

        # Create the home frame
        self.frames["Home"] = HomeFrame(parent=self.container)
        self.frames["Home"].grid(row=0, column=0, sticky="nsew")

        # Create the calendar frame
        self.frames["Calendar"] = CalendarFrame(parent=self.container)
        self.frames["Calendar"].grid(row=0, column=0, sticky="nsew")

        # Create the notes frame
        self.frames["Notes"] = NotesFrame(self.container)
        self.frames["Notes"].grid(row=0, column=0, sticky="nsew")

        # Create the projects frame
        self.frames["Projects"] = ProjectFrame(self.container)
        self.frames["Projects"].grid(row=0, column=0, sticky="nsew")

        # Create the music frame
        self.frames["Music"] = MusicFrame(self.container)
        self.frames["Music"].grid(row=0, column=0, sticky="nsew")

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
    
    def show_notes(self):
        self.frames["Notes"].tkraise()
    
    def show_projects(self):
        self.frames["Projects"].tkraise()
    
    def show_music(self):
        self.frames["Music"].tkraise()
    
    def show_pomo(self):
        """Raise the pomodoro frame to the top of the main container."""
        self.frames["Pomodoro"].tkraise()