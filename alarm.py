import tkinter as tk
import datetime
import winsound

def set_alarm():
    alarm_time = entry.get()  # Get the alarm time from the entry widget
    try:
        alarm_time_obj = datetime.datetime.strptime(alarm_time, "%H:%M")
        current_time = datetime.datetime.now().strftime("%H:%M")
        while current_time != alarm_time:
            current_time = datetime.datetime.now().strftime("%H:%M")
            time_label.config(text=current_time)
            window.update()
        # Play sound
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
    except ValueError:
        pass

def stop_alarm():
    # Stop sound
    winsound.PlaySound(None, winsound.SND_ASYNC)

# Create the main window
window = tk.Tk()
window.title("Alarm Clock")
window.geometry("300x250")
window.config(bg="#ECECEC")

# Create and position the widgets
title_label = tk.Label(window, text="Alarm Clock", font=("Arial", 24), bg="#ECECEC", fg="#333333")
title_label.pack(pady=10)

label = tk.Label(window, text="Enter alarm time (HH:MM):", font=("Arial", 12), bg="#ECECEC", fg="#333333")
label.pack()

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=10)

set_button = tk.Button(window, text="Set Alarm", font=("Arial", 12), command=set_alarm, bg="#4CAF50", fg="white")
set_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop Alarm", font=("Arial", 12), command=stop_alarm, bg="#FF0000", fg="white")
stop_button.pack(pady=10)

time_label = tk.Label(window, text="", font=("Arial", 20), bg="#ECECEC", fg="#333333")
time_label.pack()

# Start the main loop
window.mainloop()
