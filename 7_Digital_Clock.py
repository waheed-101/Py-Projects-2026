# Digital Clock
# Build a Simple Digital clock using python that updates in real time.


from tkinter import Label, Tk
import time

app = Tk()
app.title("🕒 Digital Clock")
app.geometry("300x150")
app.resizable(False, False)
app.configure(bg = "white")

clock_label = Label(app, bg="white", fg="black", font=("Helvetica", 30), relief='flat')
clock_label.place(x = 20, y = 20)

date_label = Label(app, bg="white", fg="gray", font=("Helvetica", 15), relief='flat')
date_label.place(x = 20, y = 80)

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    current_date = time.strftime("%d/%b/%Y")
    clock_label.config(text = current_time)
    date_label.config(text = current_date)
    clock_label.after(1000, update_time)

update_time()
app.mainloop()

