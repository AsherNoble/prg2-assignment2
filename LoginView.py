from tkinter import *
from TkUtils import TkUtils as ut
from model.application.League import league

class LoginView:

    def __init__(self, root, model):
        self.root = root
        self.model = model

    def control(self):
        ut.image(self.root, "image/banner.png").pack()
        ut.separator(self.root).pack(fill=X, pady=(0, 10))
        ut.label(self.root, "Login").pack()
        ut.separator(self.root).pack(fill=X, pady=(10, 10))

        content_frame = Frame(self.root)
        ut.label(content_frame, "Manager ID: ").pack(side=LEFT)
        Entry(content_frame).pack(side=LEFT)
        content_frame.pack()

        btn_frame = Frame(self.root)
        ut.button(btn_frame, "Login").pack(side=LEFT, expand=True, fill=X)
        ut.button(btn_frame, "Close").pack(side=LEFT, expand=True, fill=X)
        btn_frame.pack(expand=True, fill=BOTH, pady=(10, 0))

if __name__ == "__main__":
    root = ut.root()
    LoginView(root, league).control()
    root.mainloop()