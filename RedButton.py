import sys
from tkinter import ttk
from TkUtils import TkUtils as ut

# using a ttk button in place of the provided tk button as it's styling didn't work on macOS
def red_button(parent, text, command):
    if sys.platform != "darwin":
        return ut.button(parent, text, command)

    style = ttk.Style(parent)
    try:
        style.theme_use("clam")
    except Exception:
        pass
    style.configure(
        "MacRed.TButton",
        background="#ff8f8f",
        foreground="white",
        font="Arial 11 bold",
        borderwidth=0,
        focusthickness=0,
        padding=(10, 6),
    )
    style.map(
        "MacRed.TButton",
        background=[("active", "#ff8080"), ("pressed", "#ff8080")],
        foreground=[("disabled", "gray70")],
    )
    return ttk.Button(parent, text=text, command=command, style="MacRed.TButton")
