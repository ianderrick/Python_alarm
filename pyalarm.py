import tkinter as tk
from tkinter import ttk
import datetime
import pygame

# Initialize pygame
pygame.init()

# Load the alarm sound
alarm_sound = pygame.mixer.Sound("alarm.mp3")

# Create the main window
root = tk.Tk()
root.title("Alarm App")

# Create the time input field
time_input = ttk.Entry(root, width=5)
time_input.pack()

# Create the set alarm button
set_alarm_button = ttk.Button(root, text="Set Alarm")
set_alarm_button.pack()

# Create the stop alarm button (initially disabled)
stop_alarm_button = ttk.Button(root, text="Stop Alarm", state="disabled")
stop_alarm_button.pack()

# Function to set the alarm
def set_alarm():
# Get the current time
    current_time = datetime.datetime.now()

# Get the desired alarm time
    desired_time = datetime.datetime.strptime(time_input.get(), "%H:%M")

# Calculate the time until the alarm should go off
    time_difference = desired_time - current_time
    time_until_alarm = time_difference.seconds

# Enable the stop alarm button
    stop_alarm_button.config(state="normal")

# Schedule the alarm to go off
    root.after(time_until_alarm * 1000, sound_alarm)

# Function to sound the alarm
def sound_alarm():
# Play the alarm sound
    alarm_sound.play()

# Disable the set alarm button and enable the stop alarm button
    set_alarm_button.config(state="disabled")
    stop_alarm_button.config(state="normal")

# Function to stop the alarm
def stop_alarm():
# Stop the alarm sound
    alarm_sound.stop()

# Enable the set alarm button and disable the stop alarm button
    set_alarm_button.config(state="normal")
    stop_alarm_button.config(state="disabled")

# Set the command for the set alarm button
set_alarm_button["command"] = set_alarm

# Set the command for the stop alarm button
stop_alarm_button["command"] = stop_alarm

# Run the main loop
root.mainloop()
