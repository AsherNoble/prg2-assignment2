from tkinter import *
from TkUtils import TkUtils as ut

class ErrorView:
    
    def __init__(self, root, model, exception):
        self.root = root
        self.model = model
        self.exception = exception
        
    def control(self):
        # btn_frame = Frame(self.root)
        ut.image(self.root, "image/error.png").pack(padx=16, pady=(16, 8))
        err_type = type(self.exception).__name__
        err_msg = str(self.exception)
        ut.error_label(self.root, f"{err_type}: {err_msg}").pack(pady=(0, 8))
        ut.button(self.root, "Close", self.root.destroy).pack(pady=(0, 16))
