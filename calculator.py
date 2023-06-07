from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk 


root = Tk()
root.geometry('430x660+150+50')
root.title('Calculator')
root.resizable(False, False)
root.configure(background='black')


# display
output_display = ctk.CTkEntry(root,width=400, 
                       height=50, 
                       text_color='white',
                       font=('Arial', 29))
output_display.place(x=15, y=10)

input_display = ctk.CTkEntry(root,width=400, 
                       height=70, 
                       text_color='white',
                       font=('Arial', 35))
input_display.place(x=15, y=63)



# Button images
button_images = [
    ('assets/back.png', (20, 160)),  # Undo or C
    ('assets/sb.png', (120, 160)),  # Brackets
    ('assets/cb.png', (220, 160)),  # Brackets
    ('assets/division.png', (320, 160)),  # Division
    ('assets/multiply.png', (320, 260)),  # Multiplication
    ('assets/minus.png', (320, 360)),  # Subtraction
    ('assets/add.png', (320, 460)),  # Addition
    ('assets/7.png', (20, 260)),  # 7
    ('assets/8.png', (120, 260)),  # 8
    ('assets/9.png', (220, 260)),  # 9
    ('assets/4.png', (20, 360)),  # 4
    ('assets/5.png', (120, 360)),  # 5
    ('assets/6.png', (220, 360)),  # 6
    ('assets/1.png', (20, 460)),  # 1
    ('assets/2.png', (120, 460)),  # 2
    ('assets/3.png', (220, 460)),  # 3
    ('assets/0.png', (20, 560)),  # 0
    ('assets/dot.png', (120, 560)),  # Dot
    ('assets/mod.png', (220, 560)),  # %
    ('assets/equal.png', (320, 560)),  # Equal
]

# Button commands
def command_c():
    current = input_display.get() # get current value
    input_display.delete(0, END)
    input_display.insert(END, current[:-1])

def command_sb():
    input_display.insert(END, '(')

def command_cb():
    input_display.insert(END, ')')

def command_division():
    input_display.insert(END, '/')

def command_multiply():
    input_display.insert(END, '*')

def command_subtraction():
    input_display.insert(END, '-')

def command_addition():
    input_display.insert(END, '+')

def command_7():
    input_display.insert(END, '7')

def command_8():
    input_display.insert(END, '8')

def command_9():
    input_display.insert(END, '9')

def command_4():
    input_display.insert(END, '4')

def command_5():
    input_display.insert(END, '5')

def command_6():
    input_display.insert(END, '6')

def command_1():
    input_display.insert(END, '1')

def command_2():
    input_display.insert(END, '2')

def command_3():
    input_display.insert(END, '3')

def command_0():
    input_display.insert(END, '0')

def command_dot():
    input_display.insert(END, '.')

def command_mod():
    input_display.insert(END, '%')

def command_equal():
    expression = input_display.get()
    
    try:
        res = eval(expression)
        output_display.delete(0, END)
        output_display.insert(END, res)
    except:
        output_display.delete(0, END)
        output_display.insert(END, "Expression Error")



button_commands = [
    command_c,
    command_sb,
    command_cb,
    command_division,
    command_multiply,
    command_subtraction,
    command_addition,
    command_7,
    command_8,
    command_9,
    command_4,
    command_5,
    command_6,
    command_1,
    command_2,
    command_3,
    command_0,
    command_dot,
    command_mod,
    command_equal,
]

# Create and place buttons
buttons = []
button_images_tk = []  # Store the PhotoImage objects

for image_path, (x, y) in button_images:
    # plot image after resize
    button_image = Image.open(image_path)
    button_image_resize = button_image.resize((80, 80))
    button_image_tk = ImageTk.PhotoImage(image=button_image_resize)
    
    button_widget = ctk.CTkButton(root, image=button_image_tk,
                                  command=button_commands[button_images.index((image_path, (x, y)))],
                                  bg_color='black',
                                  fg_color='black',
                                  hover=False,
                                  text='',
                                  width=100,
                                  height=40
                                  )
    button_widget.place(x=x, y=y)
    buttons.append(button_widget)
    button_images_tk.append(button_image_tk)  # Store the PhotoImage object


root.mainloop()
