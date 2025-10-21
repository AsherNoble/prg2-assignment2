from tkinter import *
from RedButton import red_button
from TkUtils import TkUtils as ut

class ErrorView:
    def __init__(self, root, model, exception):
        self.root = root
        self.model = model
        self.exception = exception

    def control(self):
        err_type = type(self.exception).__name__
        err_msg = str(self.exception)

        ut.image(self.root, "image/error.png").pack(fill=X)
        ut.separator(self.root).pack(fill=X, pady=(8, 8))

        Label(self.root, text=err_type, font="Courier 18 bold", fg="red", bg="#d9d9d9").pack(pady=(0, 6))
        ut.separator(self.root).pack(fill=X, pady=(6, 6))
        Label(self.root, text=err_msg, font="Helvetica 12 bold", fg="#ff8f8f", bg="#d9d9d9",
              wraplength=520, justify=CENTER).pack(pady=(0, 12))

        bottom = Frame(self.root, bg="#d9d9d9")
        bottom.pack(fill=X, pady=(4, 12))
        red_button(bottom, "Close", self.root.destroy).pack(fill=X, padx=12)
