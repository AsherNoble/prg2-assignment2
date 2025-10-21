from tkinter import *
from TkUtils import TkUtils as ut

class ManagerDashboardView:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        
    def control(self):
        self.manager = self.model.get_logged_in_manager()
        self.team = self.manager.get_team()
        
        team_name = "Your Team" if self.team is None else self.team.get_team_name()
        jersey_image = "none" if self.team is None else self.team.get_team_name().lower()
        
        ut.image(self.root, "image/banner.png").pack()
        ut.separator(self.root).pack(fill=X, pady=(0, 10))
        ut.label(self.root, team_name).pack()
        ut.separator(self.root).pack(fill=X, pady=(10, 10))

        center = Frame(self.root)
        center.pack()
        ut.image(center, f"image/{jersey_image}.png", height=220, width=220, background="#d9d9d9").pack(pady=8)

        mid = Frame(self.root)
        mid.pack(pady=(4, 8))
        ut.button(mid, "Withdraw", self.on_withdraw).pack(side=LEFT, padx=4)
        # ut.button(mid, "Manage", self.on_manage).pack(side=LEFT, padx=4)

        bottom = Frame(self.root)
        bottom.pack(fill=X, pady=(10, 0))
        # ut.button(bottom, "Swap Team", self.on_swap).pack(side=LEFT, expand=True, fill=X)
        ut.button(bottom, "Close", self.root.destroy).pack(side=LEFT, expand=True, fill=X)
        
    def on_withdraw(self):
        self.model.withdraw_manager_from_team(self.manager)
        ut.same_window("Manager Dashboard", self.root)
        ManagerDashboardView(self.root, self.model).control()