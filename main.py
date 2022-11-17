import tkinter as tk
from tkinter import *
from tkinter import messagebox

master = tk.Tk()

master.title("PLACEMENT ELIGIBILITY")
master.iconbitmap(r'C:\Users\Jinju Pulikken\Downloads\img.ico')

master.geometry("900x400")

name_var = StringVar()
level_var = StringVar()
unit1_var = StringVar()
unit3_var = StringVar()
unit4_var = StringVar()
unit6_var = StringVar()
finalscore = StringVar()
group = StringVar()

name_label = tk.Label(master, text="Name")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(master, textvariable=name_var)
name_entry.grid(row=0, column=1)

level_label = tk.Label(master, text="Level")
level_label.grid(row=2, column=0)
level_entry = tk.Entry(master, textvariable=level_var)
level_entry.grid(row=2, column=1)

tk.Label(master, text="Unit.No").grid(row=5, column=0)
tk.Label(master, text="1").grid(row=7, column=0)
tk.Label(master, text="3").grid(row=9, column=0)
tk.Label(master, text="4").grid(row=11, column=0)
tk.Label(master, text="6").grid(row=13, column=0)

tk.Label(master, text="Subject").grid(row=5, column=1)

tk.Label(master, text="Information Technology Systems").grid(row=7, column=1)
tk.Label(master, text="Social Media in Business").grid(row=9, column=1)
tk.Label(master, text="Programming").grid(row=11, column=1)
tk.Label(master, text="Website Development").grid(row=13, column=1)

tk.Label(master, text="Grade").grid(row=5, column=6)

Button1 = Radiobutton(master, text="PASS", variable=unit1_var, value="P")
Button1.grid(row=7, column=4)
Button1 = Radiobutton(master, text="MERIT", variable=unit1_var, value="M")
Button1.grid(row=7, column=5)
Button1 = Radiobutton(master, text="DISTINCTION", variable=unit1_var, value="D")
Button1.grid(row=7, column=6)
Button1 = Radiobutton(master, text="REFER", variable=unit1_var, value="R")
Button1.grid(row=7, column=7)

Button2 = Radiobutton(master, text="PASS", variable=unit3_var, value="P")
Button2.grid(row=9, column=4)
Button2 = Radiobutton(master, text="MERIT", variable=unit3_var, value="M")
Button2.grid(row=9, column=5)
Button2 = Radiobutton(master, text="DISTINCTION", variable=unit3_var, value="D")
Button2.grid(row=9, column=6)
Button2 = Radiobutton(master, text="REFER", variable=unit3_var, value="R")
Button2.grid(row=9, column=7)

Button3 = Radiobutton(master, text="PASS", variable=unit4_var, value="P")
Button3.grid(row=11, column=4)
Button3 = Radiobutton(master, text="MERIT", variable=unit4_var, value="M")
Button3.grid(row=11, column=5)
Button3 = Radiobutton(master, text="DISTINCTION", variable=unit4_var, value="D")
Button3.grid(row=11, column=6)
Button3 = Radiobutton(master, text="REFER", variable=unit4_var, value="R")
Button3.grid(row=11, column=7)

Button4 = Radiobutton(master, text="PASS", variable=unit6_var, value="P")
Button4.grid(row=13, column=4)
Button4 = Radiobutton(master, text="MERIT", variable=unit6_var, value="M")
Button4.grid(row=13, column=5)
Button4 = Radiobutton(master, text="DISTINCTION", variable=unit6_var, value="D")
Button4.grid(row=13, column=6)
Button4 = Radiobutton(master, text="REFER", variable=unit6_var, value="R")
Button4.grid(row=13, column=7)

button = tk.Button(master, text="Submit", bg="black", fg="white", command=lambda: display())
button.grid(row=15, column=1)

# group_label = tk.Label(master, text="Group").grid(row=8, column=3)

def display():                                                      #function display for button click
    score1 = unit1_var.get()                                        #pulling values
    score2 = unit3_var.get()
    score3 = unit4_var.get()
    score4 = unit6_var.get()
    listofscores = [score1, score2, score3, score4]
    print(listofscores)
    print("hi",score2)

    if score1 == '' and len(score2) == '' and len(score3) == '' and len(score4) == '':
        msg = 'please enter grades'
    elif score1 == '' or score2 == '' or score3 == '' or score4 == '':
        msg = 'enter all grades'
    else:
        if not listofscores.__contains__("R"):
            if listofscores.__contains__("P"):
                tk.Label(master, text="Group 3 : Pass Group").grid(row=16, column=8)
                return
        else:
            tk.Label(master, text="Ineligible for placements : Refer Group").grid(row=16, column=8)
            return

        if not listofscores.__contains__("M"):
            if listofscores.__contains__("D"):
                tk.Label(master, text="Group 1 : Distinction Group").grid(row=16, column=8)
                return
        else:
            tk.Label(master, text="Group 2 : Merit Group").grid(row=16, column=8)
            return


exit_button = Button(master, text="Close", command=master.destroy)
exit_button.grid(row=17, column=5)

master.mainloop()
