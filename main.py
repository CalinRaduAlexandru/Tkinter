from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = entry.get()
    calculated_value = round(int(new_text) * 1.6, 2)
    my_label_result.config(text=f"{calculated_value} Km")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Enter value in miles")
#Gets text in entry
print(entry.get())
entry.grid(column=0, row=1)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="Miles to Km")
my_label.grid(column=0, row=0)
my_label.config(padx=0, pady=15)

#Button
button = Button(text="Calculate", height=1, command=button_clicked)
button.config(padx=0, pady=0)
button.grid(column=1, row=1)

# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)

#Label
my_label_two = Label()
my_label_two.config(text="Here will show your transformed value")
my_label_two.grid(column=0, row=3)
my_label_two.config(padx=0, pady=30)

#Entry
# input = Entry(width=10)
# print(input.get())
# input.grid(column=0, row=4)

my_label_result = Label()
my_label_result.config(text="")
my_label_result.grid(column=0, row=5)
my_label_result.config(padx=0, pady=0)









window.mainloop()