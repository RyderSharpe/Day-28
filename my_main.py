from tkinter import *
import math
import winsound

# import pygame
#
# pygame.init()

# ------------------------------ NOTES -------------------------------- #
# *args is unlimited positional arguments. **kw are unlimited keyword arguments ie. image=tomato_img

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
reps = 0
timer = None

WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)

    # timer text 00:00
    canvas.itemconfig(timer_text, text="00:00")

    # title_label "timer"
    timer_label.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)

    # reset check_marks
    check_mark_label.config(text=" ")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global timer_label
    reps += 1

    work = WORK_MIN * 4
    short_break = SHORT_BREAK_MIN * 2
    long_break = WORK_MIN * 10

    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Long Break 🧘️", font=(FONT_NAME, 22, "bold"), fg=GREEN, bg=YELLOW)
        # winsound.Beep(2500, 1000)
        # pygame.mixer.Sound("timer_sound.mp3").play()

    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Short Break 😊", font=(FONT_NAME, 22, "bold"), fg=PINK, bg=YELLOW)
        # winsound.Beep(2000, 500)
        # pygame.mixer.Sound("short_break_sound.mp3").play()
    else:
        count_down(work)
        timer_label.config(text="Work 😈", font=(FONT_NAME, 35, "bold"), fg=RED, bg=YELLOW)
        # winsound.Beep(500, 500)
        # pygame.mixer.Sound("work_sound.mp3").play()

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Pass timer_type recursively
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
            check_mark_label.config(text=mark, font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

# Tomato stuff
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="#FFFFFF", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=2, row=2)

# ✔️ Label
check_mark_label = Label(fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=2, row=4)

# Start button
start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

# Reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

# Check every millisecond to see if something happened. Keeps window open.
window.mainloop()
