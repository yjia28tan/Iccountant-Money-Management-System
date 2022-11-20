from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#000000",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    829.0, 409.5,
    text = "FULL NAME",
    fill = "#ffffff",
    font = ("Lato-Regular", int(16.0)))

canvas.create_text(
    842.0, 350.5,
    text = "BASIC DETAILS",
    fill = "#ffffff",
    font = ("Lato-ExtraBold", int(16.0)))

canvas.create_text(
    828.5, 507.5,
    text = "USERNAME",
    fill = "#ffffff",
    font = ("Lato-Regular", int(16.0)))

canvas.create_text(
    1434.5, 409.5,
    text = "PASSWORD",
    fill = "#ffffff",
    font = ("Lato-Regular", int(16.0)))

canvas.create_text(
    1473.5, 507.5,
    text = "CONFIRM PASSWORD",
    fill = "#ffffff",
    font = ("Lato-Regular", int(16.0)))

canvas.create_text(
    809.0, 605.5,
    text = "EMAIL",
    fill = "#ffffff",
    font = ("Lato-Regular", int(16.0)))

canvas.create_text(
    849.0, 202.0,
    text = "SIGN UP",
    fill = "#ffffff",
    font = ("Lato-ExtraBold", int(32.0)))

window.resizable(False, False)
window.mainloop()
