import customtkinter as ctk
import sys

from music_module.music_widget import MusicWidget

class TempHomeApp(ctk.CTkFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Designate Content Frame
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Configure Grid
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_columnconfigure(2, weight=1)
        self.content_frame.grid_columnconfigure(3, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(2, weight=1)

        # Setup Widgets
        self.setup_daily_tasks()
        self.setup_weather()
        self.setup_music()
        self.setup_habit_tracker()
        self.setup_projects()
    
    def setup_daily_tasks(self):
        daily_tasks = ctk.CTkFrame(self.content_frame, corner_radius=10,
                                   border_color="gray", border_width=2)
        daily_tasks.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=(0, 10))
        
        label = ctk.CTkLabel(daily_tasks, text="Daily Tasks", 
                            font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=20, padx=20)


    def setup_weather(self):
        weather = ctk.CTkFrame(self.content_frame, corner_radius=10,
                                   border_color="gray", border_width=2)
        weather.grid(row=0, column=1, sticky="nsew", columnspan=2, padx=5, pady=(0, 5))
        
        label = ctk.CTkLabel(weather, text="Weather", 
                            font=ctk.CTkFont(size=18, weight="bold"))
        label.pack(expand=True)


    def setup_music(self):
        music = ctk.CTkFrame(self.content_frame, corner_radius=10,
                                border_color="gray", border_width=2)
        music.grid(row=0, column=3, sticky="nsew", padx=(5, 0), pady=(0, 5))
        
        music_widget = MusicWidget(music)
        music_widget.pack(expand=True)


    def setup_habit_tracker(self):
        blank = ctk.CTkFrame(self.content_frame, corner_radius=10,
                                border_color="gray", border_width=2)
        blank.grid(row=1, column=1, sticky="nsew", rowspan=2, columnspan=2, padx=5, pady=(5, 0))
        
        label = ctk.CTkLabel(blank, text="Habit Tracker", 
                            font=ctk.CTkFont(size=16))
        label.pack(expand=True)


    def setup_projects(self):
        projects = ctk.CTkFrame(self.content_frame, corner_radius=10,
                                   border_color="gray", border_width=2)
        projects.grid(row=1, column=3, sticky="nsew", rowspan=2, padx=(5, 0), pady=(5, 0))
        
        label = ctk.CTkLabel(projects, text="Projects", 
                            font=ctk.CTkFont(size=18, weight="bold"))
        label.pack(expand=True)