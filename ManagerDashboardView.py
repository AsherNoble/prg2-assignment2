from tkinter import *
from RedButton import red_button
from SwapView import SwapView
from TeamDashboardView import TeamDashboardView
from TkUtils import TkUtils as ut

class ManagerDashboardView:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        
    def control(self):
        self.manager = self.model.get_logged_in_manager()
        self.team = self.manager.get_team()
        
        self.has_team = False if self.team is None else True
        team_name = "No team" if self.team is None else self.team.get_team_name()
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
        
        self.withdraw_btn = red_button(mid, "Withdraw", self.on_withdraw)
        self.withdraw_btn.config(state=DISABLED if not self.has_team else NORMAL)
        self.withdraw_btn.pack(side=LEFT, padx=4)
        
        red_button(mid, "Manage", self.on_manage).pack(side=LEFT, padx=4)

        bottom = Frame(self.root)
        bottom.pack(fill=X, pady=(10, 0))
        red_button(bottom, "Swap Team", self.on_swap).pack(side=LEFT, expand=True, fill=X)
        red_button(bottom, "Close", self.root.destroy).pack(side=LEFT, expand=True, fill=X)
        
    def on_withdraw(self):
        self.model.withdraw_manager_from_team(self.manager)
        self.refresh_dashboard()
        
    def on_manage(self):
        root = ut.same_window("Team Dashboard", self.root)
        TeamDashboardView(root, self.model).control()

    def on_swap(self):
        win = ut.top_level("Swap")
        SwapView(win, self.model, self.refresh_dashboard).control()
        win.transient(self.root); win.grab_set(); win.focus_set()
        
    def refresh_dashboard(self):
        ut.same_window("Manager Dashboard", self.root)
        ManagerDashboardView(self.root, self.model).control()