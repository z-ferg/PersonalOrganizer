import customtkinter as ctk

class MusicWidget(ctk.CTkFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Configure Grid
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_columnconfigure(2, weight=1)
        self.content_frame.grid_columnconfigure(3, weight=1)
        self.content_frame.grid_columnconfigure(4, weight=1)

        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(2, weight=1)
        self.content_frame.grid_rowconfigure(3, weight=1)
        self.content_frame.grid_rowconfigure(4, weight=1)

        # Media Controls
        back_skip = ctk.CTkButton(self.content_frame, corner_radius=10, text="⏮",
                                  border_width=0)
        back_skip.grid(row=5, column=1, sticky="nsew", padx=10)

        front_skip = ctk.CTkButton(self.content_frame, corner_radius=10, text="⏭",
                                   border_width=0)
        front_skip.grid(row=5, column=3, sticky="nsew", padx=10)

        self.state = {}

        self.state["Pause"] = ctk.CTkButton(self.content_frame, corner_radius=10, text="⏸",
                                            border_width=0, command=self.pause_music)
        self.state["Pause"].grid(row=5, column=2, sticky="nsew", padx=10)

        self.state["Play"] = ctk.CTkButton(self.content_frame, corner_radius=10, text="▶︎",
                                           border_width=0, command=self.play_music)
        self.state["Play"].grid(row=5, column=2, sticky="nsew", padx=10)
    
    def pause_music(self):
        self.state["Play"].tkraise()
        print("Paused music!")
        # TODO: Insert spotify pause mechanics

    def play_music(self):
        self.state["Pause"].tkraise()
        print("Playing music!")
        # TODO: Insert spotify play mechanics