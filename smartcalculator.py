from tkinter import *
import math

# creating a window
screen = Tk()

# entering screen title
screen.title("My Calculator")
screen.configure(bg='black')

# to check if two operators are used continuously
wrong_operations = {'/+': 'wrong input', '/-': 'wrong input', '/*': 'wrong input', '+/': 'wrong input',
                    '+-': 'wrong input', '+*': 'wrong input', '++': 'wrong input', '**': 'wrong input',
                    '*/': 'wrong input', '*-': 'wrong input', '*+': 'wrong input', '--': 'wrong input',
                    '-*': 'wrong input', '-/': 'wrong input', '-+': 'wrong input', '//': '//'}

# to check and correct if 2nd or nth input starts with "0" since python eval can't process it normally
mistyped = {'+0': '+0.', '-0': '-0.', '*0': '*0.', '/0': '/0.'}

trigonometric = False


def string_error():
    global operator
    if operator == 'cannot divide by zero' or operator == 'wrong input' or operator == "input empty":
        operator = '0.0'


def mistype():
    global operator, mistyped, wrong_operations
    for k, v in wrong_operations.items():
        if k in operator:
            operator = v
    for g, h in mistyped.items():
        if g in operator:
            operator = operator.replace(g, h)


def mistype_trigonometry():
    global operator, wrong_operations
    for w in wrong_operations:
        if w in operator:
            operator = operator.replace(w, '')


def sin():
    global operator
    mistype_trigonometry()
    equal()
    string_error()
    operator = str(math.sin(math.radians(float(operator))))
    text.set(operator)


def cos():
    global operator
    mistype_trigonometry()
    equal()
    string_error()
    operator = str(math.cos(math.radians(float(operator))))
    text.set(operator)


def tan():
    global operator
    mistype_trigonometry()
    equal()
    string_error()
    operator = str(math.tan(math.radians(float(operator))))
    text.set(operator)


def csc():
    global operator
    mistype_trigonometry()
    equal()
    string_error()
    try:
        operator = str(1 / math.sin(math.radians(float(operator))))
    except ZeroDivisionError:
        operator = 'cannot divide by zero'
    text.set(operator)


def sec():
    global operator
    mistype_trigonometry()
    equal()
    string_error()
    operator = str(1 / math.cos(math.radians(float(operator))))
    text.set(operator)


def cot():
    global operator
    mistype_trigonometry()
    equal()
    string_error()
    try:
        operator = str(1 / math.sin(math.radians(float(operator))))
    except ZeroDivisionError:
        operator = 'cannot divide by zero'
    text.set(operator)


# defining input in entry
def click(num):
    global operator, wrong_operations
    mistype()
    if operator == 'cannot divide by zero' or operator == 'wrong input' or operator == "input empty":
        operator = ''
        operator += str(num)
    else:
        operator += str(num)
    text.set(operator)


# defining equal function
def equal():
    global operator
    if '/0.' in operator:
        operator = str(eval(operator))
    elif '/0' in operator:
        operator = 'cannot divide by zero'
    elif operator == '':
        operator = "input empty"
    elif operator[0] == '0' or operator[0] == '/' or operator[0] == '*':
        operator = list(operator)
        operator.pop(0)
        operator = ''.join(operator)
        operator = str(eval(operator))
    elif operator == '0.0':
        pass
    else:
        string_error()
        operator = str(eval(operator))
    text.set(operator)


# defining entry clear button
def clear():
    global operator
    operator = ''
    text.set(operator)


def square_root():
    global operator
    equal()
    string_error()
    operator = (eval(operator))
    operator = str(math.sqrt(float(operator)))
    text.set(operator)


def square():
    global operator
    equal()
    string_error()
    operator = str(eval(operator))
    operator = str(float(operator) * float(operator))
    text.set(operator)


def cube():
    global operator
    equal()
    string_error()
    operator = str(eval(operator))
    operator = str(float(operator) * float(operator) * float(operator))
    text.set(operator)


def bk_spc():
    global operator
    while len(operator) != 0:
        operator = list(operator)
        operator.pop(-1)
        break
    operator = ''.join(operator)
    text.set(operator)


# defining hover effect
def on_enter(n):
    btn_equal.configure(bg='red')


def on_leave(n):
    btn_equal.configure(bg='grey')


def trigonometry():
    global trigonometric
    if not trigonometric:
        screen.geometry('450x332')
        screen.minsize(width=450, height=332)
        screen.maxsize(width=450, height=332)
    else:
        screen.geometry('450x440')
        screen.minsize(width=450, height=440)
        screen.maxsize(width=450, height=440)


def switch():
    global trigonometric
    if trigonometric:
        trigonometric = False
    else:
        trigonometric = True
    trigonometry()


# to store value shown in entry box
text = StringVar()

# to store value of typed variable
operator = ''

# creating entry point
entry1 = Entry(screen, bg='black', fg='white', font=('arial', 20, 'italic bold'), justify='right', bd='14',
               textvariable=text)
# entry position
entry1.grid(row=0, columnspan=3)

# creating buttons
btn9 = Button(screen, text='9', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5, command=lambda: click(9),
              activebackground='green', activeforeground='white', bg='grey', fg='white')
btn9.grid(row='1', column='2')

btn8 = Button(screen, text='8', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5, command=lambda: click(8),
              activebackground='green', activeforeground='white', bg='grey', fg='white')
btn8.grid(row='1', column='1')

btn7 = Button(screen, text='7', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5, command=lambda: click(7),
              activebackground='green', activeforeground='white', bg='grey', fg='white')
btn7.grid(row='1', column='0')

btn6 = Button(screen, text='6', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5, command=lambda: click(6),
              activebackground='green', activeforeground='white', bg='grey', fg='white')
btn6.grid(row='2', column='2')

btn5 = Button(screen, text='5', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5, command=lambda: click(5),
              activebackground='green', activeforeground='white', bg='grey', fg='white')
btn5.grid(row='2', column='1')

btn4 = Button(screen, text='4', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5, command=lambda: click(4),
              activebackground='green', activeforeground='white', bg='grey', fg='white')
btn4.grid(row='2', column='0')

btn3 = Button(screen, text='3', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5, command=lambda: click(3),
              activebackground='green', activeforeground='white', bg='grey', fg='white')
btn3.grid(row='3', column='2')

btn2 = Button(screen, text='2', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5, command=lambda: click(2),
              activebackground='green', activeforeground='white', bg='grey', fg='white')
btn2.grid(row='3', column='1')

btn1 = Button(screen, text='1', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5, command=lambda: click(1),
              activebackground='green', activeforeground='white', bg='grey', fg='white')
btn1.grid(row='3', column='0')

btn0 = Button(screen, text='0', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5, command=lambda: click(0),
              activebackground='green', activeforeground='white', bg='grey', fg='white')
btn0.grid(row='4', column='1')

btn_plus = Button(screen, text='+', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5,
                  command=lambda: click('+'),
                  activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_plus.grid(row='1', column='3')

btn_minus = Button(screen, text='-', font=('arial', 16, 'italic bold'), bd=4, padx=42, pady=5,
                   command=lambda: click("-"),
                   activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_minus.grid(row='2', column='3')

btn_multiply = Button(screen, text='x', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5,
                      command=lambda: click("*"),
                      activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_multiply.grid(row='4', column='3')

btn_div = Button(screen, text='/', font=('arial', 16, 'italic bold'), bd=4, padx=42, pady=5,
                 command=lambda: click("/"),
                 activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_div.grid(row='3', column='3')

btn_dot = Button(screen, text='.', font=('arial', 16, 'italic bold'), bd=4, padx=42, pady=5,
                 command=lambda: click("."),
                 activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_dot.grid(row='4', column='2')

btn_equal = Button(screen, text='=', font=('arial', 16, 'italic bold'), bd=4, padx=39, pady=5,
                   command=lambda: equal(),
                   activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_equal.grid(row='5', column='3')

btn_clear = Button(screen, text='C', font=('arial', 15, 'italic bold'), bd=4, padx=39, pady=5,
                   command=lambda: clear(),
                   activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_clear.grid(row='4', column='0')

btn_sqroot = Button(screen, text='sqrt', font=('arial', 16, 'italic bold'), bd=4, padx=25, pady=5,
                    command=lambda: square_root(),
                    activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_sqroot.grid(row='6', column='0')

btn_sq = Button(screen, text='x^2', font=('arial', 16, 'italic bold'), bd=4, padx=27, pady=5,
                command=lambda: square(),
                activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_sq.grid(row='5', column='2')

btn_cube = Button(screen, text='x^3', font=('arial', 16, 'italic bold'), bd=4, padx=27, pady=5,
                  command=lambda: cube(),
                  activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_cube.grid(row='6', column='1')

btn_bk_spc = Button(screen, text='<--', font=('arial', 16, 'italic bold'), bd=6, padx=30, pady=7,
                    command=lambda: bk_spc(),
                    activebackground='green', activeforeground='black', bg='brown', fg='yellow')
btn_bk_spc.grid(row='0', column='3')

# ******************************************** TRIGONOMETRY *************************************************

btn_sin = Button(screen, text='sin', font=('arial', 16, 'italic bold'), bd=4, padx=30, pady=5,
                 command=lambda: sin(),
                 activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_sin.grid(row='6', column='2')

btn_cos = Button(screen, text='cos', font=('arial', 15, 'italic bold'), bd=4, padx=30, pady=5,
                 command=lambda: cos(),
                 activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_cos.grid(row='6', column='3')

btn_tan = Button(screen, text='tan', font=('arial', 16, 'italic bold'), bd=4, padx=30, pady=5,
                 command=lambda: tan(),
                 activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_tan.grid(row='7', column='2')

btn_csc = Button(screen, text='csc', font=('arial', 16, 'italic bold'), bd=4, padx=27, pady=5,
                 command=lambda: csc(),
                 activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_csc.grid(row='7', column='0')

btn_sec = Button(screen, text='sec', font=('arial', 16, 'italic bold'), bd=4, padx=27, pady=5,
                 command=lambda: sec(),
                 activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_sec.grid(row='7', column='1')

btn_cot = Button(screen, text='cot', font=('arial', 16, 'italic bold'), bd=4, padx=29, pady=5,
                 command=lambda: cot(),
                 activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_cot.grid(row='7', column='3')

btn_tri = Button(screen, text='Advanced', font=('arial', 16, 'italic bold'), bd=5, padx=50, pady=5,
                 command=lambda: switch(),
                 activebackground='green', activeforeground='white', bg='grey', fg='white')
btn_tri.grid(row='5', columnspan='2')

# ********************************************** BINDING HOVER EFFECT **********************************************
# class Binding:

btn_equal.bind('<Enter>', on_enter)
btn_equal.bind('<Leave>', on_leave)
#
# btn1.bind('<Enter>', on_enter)
# btn1.bind('<Enter>', on_leave)

# btn2.bind('<Enter>', on_enter)
# btn2.bind('<Enter>', on_leave)

trigonometry()
screen.mainloop()
