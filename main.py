import tkinter
import customtkinter

from Dashboard import Dashboard

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# App Frame
app = Dashboard()

# Run App
app.mainloop()
