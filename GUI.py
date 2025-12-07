from tkinter import *
import speech_to_text
import action

try:
    from PIL import Image, ImageTk
    _PIL_AVAILABLE = True
except Exception:
    Image = None
    ImageTk = None
    _PIL_AVAILABLE = False

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")


def ask():
    # Speech input
    user_val = speech_to_text.speech_to_text()
    if user_val is None:
        user_val = ""

    bot_val = action.Action(user_val)

    text.insert(END, 'USER ---> ' + user_val + "\n")
    if bot_val is not None:
        text.insert(END, "BOT  <--- " + str(bot_val) + "\n")

    # Shutdown check (case-insensitive, safe)
    if str(bot_val).strip().lower() == "ok sir":
        root.destroy()


def send():
    send_text = entry.get()
    entry.delete(0, END)

    bot_val = action.Action(send_text)

    text.insert(END, 'USER ---> ' + send_text + "\n")
    if bot_val is not None:
        text.insert(END, "BOT  <--- " + str(bot_val) + "\n")

    if str(bot_val).strip().lower() == "ok sir":
        root.destroy()


def del_text():
    text.delete('1.0', 'end')


# Frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=55, pady=10)

# Text label
text_label = Label(frame,
                   text="AI Assistant",
                   font=("Comic Sans MS", 14, "bold"),
                   bg="#356696",
                   fg="white")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
img_path = "image/assitant.png"  # keep your path; shows fallback if missing
image = None

if _PIL_AVAILABLE:
    try:
        pil_img = Image.open(img_path)
        image = ImageTk.PhotoImage(pil_img)
    except Exception:
        image = None
else:
    try:
        image = PhotoImage(file=img_path)
    except Exception:
        image = None

if image:
    image_label = Label(frame, image=image, bg="#356696")
    image_label.image = image
    image_label.grid(row=1, column=0, pady=20)
else:
    image_label = Label(frame,
                        text="(image not available)",
                        bg="#356696",
                        fg="white")
    image_label.grid(row=1, column=0, pady=20)

# Text widget
text = Text(root, font=('courier', 10, 'bold'), bg="#356696", fg="white")
text.place(x=100, y=375, width=375, height=100)

# Entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=100, y=500, width=350, height=30)

# Buttons
Button1 = Button(root, text="ASK", bg='#356696',
                 pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

Button2 = Button(root, text="Send", bg='#356696',
                 pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575)

Button3 = Button(root, text="Delete", bg='#356696',
                 pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text)
Button3.place(x=225, y=575)

root.mainloop()
