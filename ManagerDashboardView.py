from tkinter import *
from TkUtils import TkUtils as ut

class ManagerDashboardView:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.manager = model.logged_in_manager
        
    def control(self):
        ut.image(self.root, "image/banner.png").pack()
        ut.separator(self.root).pack(fill=X, pady=(0, 10))
        ut.label(self.root, self.manager.team.name if hasattr(self.manager, "team") else "Your Team").pack()
        ut.separator(self.root).pack(fill=X, pady=(10, 10))

        center = Frame(self.root)
        center.pack()
        ut.image(center, "image/jersey.png", height=220, width=220, background="#d9d9d9").pack(pady=8)

        mid = Frame(self.root)
        mid.pack(pady=(4, 8))
        ut.button(mid, "Withdraw", self.on_withdraw).pack(side=LEFT, padx=4)
        ut.button(mid, "Manage", self.on_manage).pack(side=LEFT, padx=4)

        bottom = Frame(self.root)
        bottom.pack(fill=X, pady=(10, 0))
        ut.button(bottom, "Swap Team", self.on_swap).pack(side=LEFT, expand=True, fill=X)
        ut.button(bottom, "Close", self.root.destroy).pack(side=LEFT, expand=True, fill=X)