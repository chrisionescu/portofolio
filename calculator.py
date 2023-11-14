import tkinter as tk
from tkinter import ttk

calculation = ""
result = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calc():
    global calculation
    global result
    try:
        text_history['state'] = 'disabled'
        calc1 = calculation
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        text_history['state'] = 'normal'
        result = calc1 + "=" + calculation + "\n"
        text_history.insert(1.0,result)
        text_history['state'] = 'disabled'

        
    except:
        clear_calc()
        text_result.insert(1.0, "Error")
    if calculation == "":
        text_result.insert(1.0, " Input calculation: ")


def clear_calc():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")



#####





root = tk.Tk()
root.title('Calculator')
root.config(background='#e2b9eb')
root.geometry("420x410")

text_result = tk.Text(root,height=2,width=16,font=("Calibri", 24), background='#f6d9fc')
text_result.grid(columnspan=6)

text_history = tk.Text(root, height=10, width=10, font=("Calibri", 20), background='#f6d9fc')

text_history.grid(column=6,rowspan=6)





btn1 = tk.Button(root, text="1", command=lambda:add_to_calculation(1), width=5, font=("Calibri", 14), background='#cd9ee6', activebackground='#6e237d')
btn1.grid(row=2, column=1)

btn2 = tk.Button(root, text="2", command=lambda:add_to_calculation(2), width=5, font=("Calibri", 14), background='#cd9ee6', activebackground='#6e237d')
btn2.grid(row=2, column=2)

btn3 = tk.Button(root, text="3", command=lambda:add_to_calculation(3), width=5, font=("Calibri", 14), background='#cd9ee6', activebackground='#6e237d')
btn3.grid(row=2, column=3)


btn4 = tk.Button(root, text="4", command=lambda:add_to_calculation(4), width=5, font=("Calibri", 14), background='#cd9ee6', activebackground='#6e237d')
btn4.grid(row=3, column=1)

btn5 = tk.Button(root, text="5", command=lambda:add_to_calculation(5), width=5, font=("Calibri", 14), background='#cd9ee6', activebackground='#6e237d')
btn5.grid(row=3, column=2)

btn6 = tk.Button(root, text="6", command=lambda:add_to_calculation(6), width=5, font=("Calibri", 14), background='#cd9ee6', activebackground='#6e237d')
btn6.grid(row=3, column=3)

btn7 = tk.Button(root, text="7", command=lambda:add_to_calculation(7), width=5, font=("Calibri", 14), background='#cd9ee6', activebackground='#6e237d')
btn7.grid(row=4, column=1)

btn8 = tk.Button(root, text="8", command=lambda:add_to_calculation(8), width=5, font=("Calibri", 14), background='#cd9ee6', activebackground='#6e237d')
btn8.grid(row=4, column=2)

btn9 = tk.Button(root, text="9", command=lambda:add_to_calculation(9), width=5, font=("Calibri", 14), background='#cd9ee6', activebackground='#6e237d')
btn9.grid(row=4, column=3)

btn0 = tk.Button(root, text="0", command=lambda:add_to_calculation(0), width=5, font=("Calibri", 14), background='#cd9ee6', activebackground='#6e237d')
btn0.grid(row=5, column=2)

btn_prtL = tk.Button(root, text="(", command=lambda:add_to_calculation("("), width=5, font=("Calibri", 14), background='#cd9ee6', activebackground='#6e237d')
btn_prtL.grid(row=5, column=1)

btn_prtR = tk.Button(root, text=")", command=lambda:add_to_calculation(")"), width=5, font=("Calibri", 14), background='#cd9ee6', activebackground='#6e237d')
btn_prtR.grid(row=5, column=3)

btn_plus = tk.Button(root, text="+", command=lambda:add_to_calculation("+"), width=5, font=("Calibri", 14), background='#7a5882', activebackground='#6e237d')
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda:add_to_calculation("-"), width=5, font=("Calibri", 14), background='#7a5882', activebackground='#6e237d')
btn_minus.grid(row=3, column=4)

btn_times = tk.Button(root, text="*", command=lambda:add_to_calculation("*"), width=5, font=("Calibri", 14), background='#7a5882', activebackground='#6e237d')
btn_times.grid(row=4, column=4)

btn_divided = tk.Button(root, text="/", command=lambda:add_to_calculation("/"), width=5, font=("Calibri", 14), background='#7a5882', activebackground='#6e237d')
btn_divided.grid(row=5, column=4)

btn_equal = tk.Button(root, text="=", command=evaluate_calc, width=11, font=("Calibri", 14), background='#7a5882', activebackground='#6e237d')
btn_equal.grid(row=6, column=1 , columnspan=2)

btn_clear = tk.Button(root, text="C", command=clear_calc, width=11, font=("Calibri", 14), background='#7a5882', activebackground='#6e237d')
btn_clear.grid(row=6, column=3 , columnspan=2)


root.mainloop()
