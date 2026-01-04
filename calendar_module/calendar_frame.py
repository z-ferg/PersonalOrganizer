import customtkinter as ctk
from datetime import datetime, timedelta
import calendar

from calendar_module.calendar_funcs import get_all_calendars, get_next_events

class CalendarFrame(ctk.CTkFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Calendar Page!")
        label.pack(side="top", fill="x", pady=10)

        # Current date tracking
        self.current_date = datetime.now()
        self.view_mode = "month"  # day, week, month
        
        # Fetch the events
        all_cals = get_all_calendars(name_only=True)
        
        
        self.events = [
            {"date": datetime.now(), "time": "10:00", "title": "Team Meeting", "duration": 60},
            {"date": datetime.now(), "time": "14:30", "title": "Project Review", "duration": 90},
            {"date": datetime.now() + timedelta(days=1), "time": "09:00", "title": "Client Call", "duration": 45},
            {"date": datetime.now() + timedelta(days=2), "time": "15:00", "title": "Workshop", "duration": 120},
        ]
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=20)
        
        # Navigation buttons
        nav_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        nav_frame.pack(side="left")
        
        self.prev_btn = ctk.CTkButton(nav_frame, text="◀", width=40, command=self.previous_period)
        self.prev_btn.pack(side="left", padx=5)
        
        self.date_label = ctk.CTkLabel(nav_frame, text="", font=("Arial", 20, "bold"))
        self.date_label.pack(side="left", padx=20)
        
        self.next_btn = ctk.CTkButton(nav_frame, text="▶", width=40, command=self.next_period)
        self.next_btn.pack(side="left", padx=5)
        
        self.today_btn = ctk.CTkButton(nav_frame, text="Today", width=80, command=self.go_to_today)
        self.today_btn.pack(side="left", padx=10)
        
        # View toggle
        view_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        view_frame.pack(side="right")
        
        self.view_toggle = ctk.CTkSegmentedButton(
            view_frame,
            values=["Day", "Week", "Month"],
            command=self.change_view,
            width=300
        )
        self.view_toggle.set("Month")
        self.view_toggle.pack()
        
        # Main content area
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        self.update_view()
        
    def change_view(self, value):
        self.view_mode = value.lower()
        self.update_view()
        
    def update_view(self):
        # Clear current content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        if self.view_mode == "day":
            self.show_day_view()
        elif self.view_mode == "week":
            self.show_week_view()
        else:
            self.show_month_view()
            
    def show_day_view(self):
        self.date_label.configure(text=self.current_date.strftime("%A, %B %d, %Y"))
        
        # Scrollable frame for time slots
        scroll_frame = ctk.CTkScrollableFrame(self.content_frame)
        scroll_frame.pack(fill="both", expand=True)
        
        # Time slots from 6 AM to 10 PM
        for hour in range(6, 23):
            time_slot = ctk.CTkFrame(scroll_frame, height=60)
            time_slot.pack(fill="x", pady=1)
            
            time_label = ctk.CTkLabel(time_slot, text=f"{hour:02d}:00", width=80, font=("Arial", 12))
            time_label.pack(side="left", padx=10, pady=10)
            
            event_frame = ctk.CTkFrame(time_slot, fg_color="transparent")
            event_frame.pack(side="left", fill="both", expand=True, padx=10)
            
            # Check for events at this hour
            for event in self.events:
                if event["date"].date() == self.current_date.date():
                    event_hour = int(event["time"].split(":")[0])
                    if event_hour == hour:
                        event_card = ctk.CTkFrame(event_frame, fg_color="#1f6aa5", corner_radius=8)
                        event_card.pack(fill="x", pady=5)
                        
                        event_text = f"{event['time']} - {event['title']} ({event['duration']}min)"
                        event_label = ctk.CTkLabel(event_card, text=event_text, font=("Arial", 12))
                        event_label.pack(padx=10, pady=8)
                        
    def show_week_view(self):
        start_of_week = self.current_date - timedelta(days=self.current_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        
        self.date_label.configure(text=f"{start_of_week.strftime('%b %d')} - {end_of_week.strftime('%b %d, %Y')}")
        
        # Day headers
        header_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 10))
        
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i, day in enumerate(days):
            day_date = start_of_week + timedelta(days=i)
            day_label = ctk.CTkLabel(
                header_frame, 
                text=f"{day}\n{day_date.strftime('%b %d')}", 
                font=("Arial", 12, "bold")
            )
            day_label.grid(row=0, column=i, sticky="ew", padx=5)
            header_frame.grid_columnconfigure(i, weight=1)
        
        # Week grid
        week_grid = ctk.CTkScrollableFrame(self.content_frame)
        week_grid.pack(fill="both", expand=True)
        
        for i in range(7):
            day_date = start_of_week + timedelta(days=i)
            day_frame = ctk.CTkFrame(week_grid, corner_radius=8)
            day_frame.grid(row=0, column=i, sticky="nsew", padx=5, pady=5)
            week_grid.grid_columnconfigure(i, weight=1)
            
            # Events for this day
            day_events = [e for e in self.events if e["date"].date() == day_date.date()]
            
            if day_events:
                for event in day_events:
                    event_card = ctk.CTkFrame(day_frame, fg_color="#1f6aa5", corner_radius=6)
                    event_card.pack(fill="x", padx=5, pady=5)
                    
                    event_label = ctk.CTkLabel(
                        event_card, 
                        text=f"{event['time']}\n{event['title']}", 
                        font=("Arial", 10)
                    )
                    event_label.pack(padx=8, pady=8)
            else:
                empty_label = ctk.CTkLabel(day_frame, text="No events", text_color="gray")
                empty_label.pack(pady=20)
                
    def show_month_view(self):
        self.date_label.configure(text=self.current_date.strftime("%B %Y"))
        
        cal = calendar.monthcalendar(self.current_date.year, self.current_date.month)
        
        # Day headers
        header_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 10))
        
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            day_label = ctk.CTkLabel(header_frame, text=day, font=("Arial", 12, "bold"))
            day_label.grid(row=0, column=i, sticky="ew", padx=5)
            header_frame.grid_columnconfigure(i, weight=1)
        
        # Calendar grid
        month_grid = ctk.CTkFrame(self.content_frame)
        month_grid.pack(fill="both", expand=True)
        
        for week_num, week in enumerate(cal):
            for day_num, day in enumerate(week):
                if day == 0:
                    day_frame = ctk.CTkFrame(month_grid, fg_color="transparent")
                else:
                    day_frame = ctk.CTkFrame(month_grid, corner_radius=8)
                    
                    # Day number
                    day_label = ctk.CTkLabel(day_frame, text=str(day), font=("Arial", 14, "bold"))
                    day_label.pack(anchor="nw", padx=5, pady=5)
                    
                    # Check for events
                    day_date = datetime(self.current_date.year, self.current_date.month, day)
                    day_events = [e for e in self.events if e["date"].date() == day_date.date()]
                    
                    if day_events:
                        for event in day_events[:3]:  # Show max 3 events
                            event_label = ctk.CTkLabel(
                                day_frame, 
                                text=f"• {event['title']}", 
                                font=("Arial", 9),
                                anchor="w"
                            )
                            event_label.pack(fill="x", padx=5, pady=2)
                        
                        if len(day_events) > 3:
                            more_label = ctk.CTkLabel(
                                day_frame, 
                                text=f"+{len(day_events)-3} more", 
                                font=("Arial", 8),
                                text_color="gray"
                            )
                            more_label.pack(padx=5, pady=2)
                
                day_frame.grid(row=week_num, column=day_num, sticky="nsew", padx=2, pady=2)
                month_grid.grid_columnconfigure(day_num, weight=1)
            month_grid.grid_rowconfigure(week_num, weight=1)
            
    def previous_period(self):
        if self.view_mode == "day":
            self.current_date -= timedelta(days=1)
        elif self.view_mode == "week":
            self.current_date -= timedelta(days=7)
        else:  # month
            if self.current_date.month == 1:
                self.current_date = self.current_date.replace(year=self.current_date.year-1, month=12)
            else:
                self.current_date = self.current_date.replace(month=self.current_date.month-1)
        self.update_view()
        
    def next_period(self):
        if self.view_mode == "day":
            self.current_date += timedelta(days=1)
        elif self.view_mode == "week":
            self.current_date += timedelta(days=7)
        else:  # month
            if self.current_date.month == 12:
                self.current_date = self.current_date.replace(year=self.current_date.year+1, month=1)
            else:
                self.current_date = self.current_date.replace(month=self.current_date.month+1)
        self.update_view()
        
    def go_to_today(self):
        self.current_date = datetime.now()
        self.update_view()