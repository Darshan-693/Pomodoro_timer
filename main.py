import tkinter as t
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
COUNTMIN = 00
SEP = ':'
COUNTSEC = 00
WORK_MIN = 1
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 1
stop = 0
cycles = 0





# ---------------------------- TIMER RESET ------------------------------- #
def stopclicked():
    global stop,cycles
    stop = 0
    cycles=0
    canvas.itemconfig(cct,text = f"00:00")
    label.config(text='T i m e r', font=(FONT_NAME, 30, 'bold'), bg=YELLOW, fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def startclicked():
    global stop
    stop = 1
    startcounting()
def startcounting():
    global cycles
    cycles += 1
    if cycles%2 !=0:
        calc(WORK_MIN*60)
        label.config(text = "WORK TIME",fg = GREEN)
    elif cycles == 8:
        calc(LONG_BREAK_MIN*60)
        label.config(text="B R E A K",fg = RED)
    else:
        calc(SHORT_BREAK_MIN*60)
        label.config(text="B R E A K", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def calc(count):
    global stop
    if 1 == stop:
        COUNTMIN = int(count/60)
        COUNTSEC = int(count%60)
        if COUNTSEC<10:
            COUNTSEC = f"0{COUNTSEC}"
        canvas.itemconfig(cct,text = f"{COUNTMIN}:{COUNTSEC}")

        if count != 1:
            window.after(1000,calc,count - 1)
        else:
            startcounting()
    # ---------------------------- UI SETUP ------------------------------- #


window = t.Tk()
window.title("Pomodoro")
window.config(bg=YELLOW)
window.minsize(width=410, height=330)
window.maxsize(width=410, height=330)
tomato = t.PhotoImage(file="tomato.png")
canvas = t.Canvas()
canvas.config(bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 112, image=tomato)
cct = canvas.create_text(103, 115, text=f"00{SEP}00", font=(FONT_NAME, 35, "bold"), fill='white')
canvas.place(x=100, y=60)
label = t.Label(text='T i m e r', font=(FONT_NAME, 30, 'bold'), bg=YELLOW, fg=GREEN)
label.place(x=100, y=30)
start = t.Button(text='START', font=("Arial", 10, 'bold'), command=startclicked)

start.place(x=30, y=275)
reset = t.Button(text='RESET', font=("Arial", 10, 'bold'), command=stopclicked)
reset.place(x=325, y=275)

window.after(1000)
window.mainloop()
