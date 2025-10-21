from tkinter import *
from ErrorView import ErrorView
from ManagerDashboardView import ManagerDashboardView
from RedButton import red_button
from TkUtils import TkUtils as ut
from model.application.League import league
from model.exception.UnauthorisedAccessException import UnauthorisedAccessException

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
        self.manager_id_entry = Entry(content_frame)
        self.manager_id_entry.pack(side=LEFT)
        content_frame.pack()
        
        def on_login():
            try:
                manager_id = int(self.manager_id_entry.get())
            except ValueError:
                print("Invalid input. Try again.")
            
            try:
                manager = league.validate_manager(manager_id)
            except UnauthorisedAccessException as error:
                win = ut.top_level("Error")
                win.title("Error")
                ErrorView(win, self.model, error).control()

                win.transient(self.root)
                win.grab_set()
                win.focus_set()
                return
                
            league.set_logged_in_manager(manager)
            ut.same_window("Manager Dashboard", self.root)
            ManagerDashboardView(self.root, self.model).control()
        
        btn_frame = Frame(self.root)
        red_button(btn_frame, "Login", on_login).pack(side=LEFT, expand=True, fill=X)
        red_button(btn_frame, "Close", self.root.destroy).pack(side=LEFT, expand=True, fill=X)
        btn_frame.pack(expand=True, fill=BOTH, pady=(10, 0))

if __name__ == "__main__":
    root = ut.root()
    LoginView(root, league).control()
    root.mainloop()