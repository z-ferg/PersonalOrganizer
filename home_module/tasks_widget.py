import customtkinter as ctk

class TaskWidget(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        task_label = ctk.CTkLabel(self.content_frame, text="Daily Tasks\n")
        task_label.grid(row=0, column=0, columnspan=2)

        self.content_frame.grid_columnconfigure(0,weight=0)
        self.content_frame.grid_columnconfigure(1,weight=1)
        
        self.check_vars = [ctk.StringVar(
            value="off"
        )]
        self.checkboxes = [ctk.CTkCheckBox(
            master=self.content_frame, 
            command=lambda idx=0: self.check_event(idx),
            variable=self.check_vars[0], 
            onvalue="on", 
            offvalue="off",
            text=""
        )]
        self.task_texts = [ctk.CTkTextbox(
            self.content_frame, 
            width=100, 
            height=50
        )]
        
        self.checkboxes[-1].grid(
            column=0, 
            row=1, 
            sticky="w", 
            padx=(10,5)
        )
        self.task_texts[-1].grid(
            column=1, 
            row=1, 
            sticky="ew", 
            padx=(0,10)
        )
    
    def check_event(self, index):
        textbox = self.task_texts[index]
        
        if self.check_vars[index].get() == "on":
            textbox.configure(font=("", 12, "overstrike"))
        else:
            textbox.configure(font=("", 12, "normal"))