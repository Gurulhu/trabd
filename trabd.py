import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Trabd")

window.resizable(0,0)

creditos = ttk.Label( window, text="Vida Longa ao Guru!")
creditos.grid( column = 0, row = 0 )

#User field
user = tk.StringVar()
user_label = ttk.Label( window, text="Login:")
user_label.grid( column = 0, row = 3 )
user_field = ttk.Entry( window, width = 60, textvariable = user )
user_field.grid( column = 0, row = 4 )

#Pwd field
pwd = tk.StringVar()
pwd_label = ttk.Label( window, text="Senha:")
pwd_label.grid( column = 0, row = 6 )
pwd_field = ttk.Entry( window, width = 60, textvariable = pwd )
pwd_field.grid( column = 0, row = 7 )

#Login button
def login_button_callback():
    pass

login_button = ttk.Button( window, text = "Login", command = login_button_callback )
login_button.grid( column = 0, row = 9 )

#pimp
user_field.focus()

window.mainloop()
