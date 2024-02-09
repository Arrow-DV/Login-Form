# Made By Arrow-Dev (Ali-Hany) <3
# visit us https://arrow-dev.rf.gd/bio


# Setups

# 1 | Import Needed Library's

from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import customtkinter as ctk
import sqlite3
from tkinter import messagebox
import re # To Check Email
# 2 | Get the current script's directory

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
ASSETS_PATH = script_dir / "assets" / "frame0"
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# 3 | Connect The Database

db = sqlite3.connect("users.db")
cursor = db.cursor()
def create_table():
    cursor.execute("CREATE TABLE if not exists Users (email text,password text)")
    cursor.execute("insert into users (email,password) VALUES('arrow@gmail.com','1234')")
    db.commit()
def check():
    
    email = entry_1.get()
    password = entry_2.get()
    email_reg = re.search(r"[A-z0-9_.+-]+@[A-z0-9-]+\.[A-z0-9-.]+",email)
    if email_reg:
        cursor.execute(f"SELECT password from users where email='{email}'")
        try:
            if cursor.fetchone()[0] == password:
                messagebox.showinfo(title="Login",message="Logged in")
            else:
                messagebox.showwarning(title="Login",message="invaild password")
        except:
            pass
    else:
        messagebox.showwarning(title="Login",message="Please Write A Vaild Email")

# 4 | Design The Window
        
root = Tk()
root.geometry("502x320")
root.configure(bg="#29266D")
root.title("Arrow-Dev | Login Form")
root.resizable(False, False)


# Canvas

canvas = Canvas(
    root,
    bg="#4945A0",
    height=320,
    width=502,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    208.0,
    320.0,
    fill="#5550BC",
    outline=""
)

# Email Textbox

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    350.5,
    113.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,font=ctk.CTkFont(size=20),
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=244.0,
    y=95.0,
    width=213.0,
    height=34.0
)

# Password Textbox
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    350.5,
    198.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,font=ctk.CTkFont(size=20),
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=244.0,
    y=180.0,
    width=213.0,
    height=34.0
)

# Labels 
canvas.create_text(
    239.0,
    63.0,
    anchor="nw",
    text="Email",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    239.0,
    149.0,
    anchor="nw",
    text="Password\n",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)
# Button | Log In
font = ctk.CTkFont(size=30)
button_1 = ctk.CTkButton(
    root,
    text="Login",
    border_width=0,font=font,
    corner_radius=0,
    command=lambda: check(),
    width=223,
    height=38,
)

button_1.place(
    x=239.0,
    y=249.0
)



# The Image
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    130.0,
    160.0,
    image=image_image_1
)





# Run The App
create_table()
root.mainloop()
# Close Database After App Exit
print("-> Closed Database")
db.close()