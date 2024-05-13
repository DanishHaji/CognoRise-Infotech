import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")

        self.label = tk.Label(master, text="Set Countdown (seconds):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_countdown)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_countdown, state=tk.DISABLED)
        self.stop_button.pack()

        self.remaining_time = 0
        self.countdown_active = False

    def start_countdown(self):
        try:
            seconds = int(self.entry.get())
            if seconds <= 0:
                messagebox.showerror("Error", "Please enter a positive integer")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")
            return

        self.remaining_time = seconds
        self.countdown_active = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.update_label()

    def stop_countdown(self):
        self.countdown_active = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_label(self):
        if self.countdown_active:
            self.label.config(text=f"Time Remaining: {self.remaining_time} seconds")
            self.remaining_time -= 1
            if self.remaining_time >= 0:
                self.master.after(1000, self.update_label)
            else:
                self.countdown_active = False
                messagebox.showinfo("Timer", "Countdown complete!")
                self.start_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.DISABLED)
        else:
            self.label.config(text="Set Countdown (seconds):")

root = tk.Tk()
timer = CountdownTimer(root)
root.mainloop()