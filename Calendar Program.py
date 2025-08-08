import calendar as cal
import tkinter as tk
import tkinter.font as tkfont
Tall=700
Long=800

def change_font():
	font_style.configure(size=10)

def change_back():
	font_style.configure(size=30)


def get_year(entry):
	year=entry
	full_year=""
	month=int(''.join(map(str,listbox.curselection())))
	month=month+1
	c= cal.TextCalendar(cal.SUNDAY)
	x=1
	if month<=12:
		change_back()
		try:
			calendar.set(c.formatmonth(int(year),month))
		except:
			calendar.set("That is not a valid year")
	else:
		change_font()
		while x<=12:
			full_year=c.formatyear(int(year), 2, 1, 1, 3)
			x=x+1
		calendar.set(full_year)
root=tk.Tk()

font_style=tkfont.Font(family="courier", size=30)
calendar=tk.StringVar()

canvas=tk.Canvas(root, height=Tall, width=Long, bg="black")
canvas.pack()

entry=tk.Entry(canvas, bg="blue", fg="white", font=("Courier", 15), bd=4)
entry.place(relheight=0.05, relwidth=0.175, relx=0.025, rely=0.075)

listbox=tk.Listbox(canvas, bg="blue", fg="white", selectmode="single", font=("Courier", 15))
listbox.place(relheight=0.25, relwidth=0.175, relx=0.025, rely=0.15)
listbox.insert(1, "January")
listbox.insert(2, "Febuary")
listbox.insert(3, "March")
listbox.insert(4, "April")
listbox.insert(5, "May")
listbox.insert(6, "June")
listbox.insert(7, "July")
listbox.insert(8, "August")
listbox.insert(9, "September")
listbox.insert(10, "October")
listbox.insert(11, "November")
listbox.insert(12, "December")
listbox.insert(13, "Entire Year")

button=tk.Button(canvas, bg="cyan", fg="blue", text="Get Calendar", font=("Courier", 10), command=lambda: get_year(entry.get()))
button.place(relheight=0.05, relwidth=0.175, relx=0.025, rely=0.425)

label1=tk.Label(canvas, bg="blue", fg="white", text="Year:" ,font=("Courier", 15))
label1.place(relheight=0.05, relwidth=0.175, relx=0.025, rely=0.025)

label2=tk.Label(canvas, bg="white", fg="black", font=font_style, textvariable=calendar, justify="left")
label2.place(relheight=0.95, relwidth=0.75, relx=0.225, rely=0.025)

root.mainloop()