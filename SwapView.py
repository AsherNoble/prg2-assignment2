from tkinter import *
from RedButton import red_button
from TkUtils import TkUtils as ut

class SwapView:
    def __init__(self, root, model, observable_view):
        self.root = root
        self.model = model
        self.observable_view = observable_view
        self.tree = None
        self.swap_btn = None

    def control(self):
        ut.image(self.root, "image/banner.png").pack()
        ut.separator(self.root).pack(fill=X, pady=(0, 10))
        ut.label(self.root, "Swap Team").pack()
        ut.separator(self.root).pack(fill=X, pady=(10, 10))

        body = Frame(self.root)
        body.pack(fill=BOTH, expand=True, padx=8, pady=4)

        self.tree = ut.treeview(body, ["Teams"], multi=False, width=540)
        self.tree.pack(fill=BOTH, expand=True)
        self._load_teams()

        bottom = Frame(self.root)
        bottom.pack(fill=X, pady=(10, 0))
        
        self.swap_btn = red_button(bottom, "Swap", self.on_swap)
        self.swap_btn.config(state=DISABLED)
        self.swap_btn.pack(side=LEFT, expand=True, fill=X)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        red_button(bottom, "Close", self.root.destroy).pack(side=LEFT, expand=True, fill=X)

    def _load_teams(self):
        names = []
        try:
            names = [team.get_team_name() for team in self.model.get_manageable_teams().get_teams()]
        except Exception:
            names = []
        for name in names:
            self.tree.insert("", "end", values=[name])

    def on_swap(self):
        selection = self.tree.selection()

        selected_item = selection[0]
        team_name = self.tree.item(selected_item)["values"][0]

        for team in self.model.get_manageable_teams().get_teams():
            if team.get_team_name() == team_name:
                chosen_team = team
                break
        
        self.model.set_manager_for_team(self.model.get_logged_in_manager(), chosen_team)
        
        if callable(self.observable_view):
            self.observable_view()
        
        self.refresh_tree()
        
    def on_select(self, event):
        selection = self.tree.selection()
        if selection:
            self.swap_btn.config(state=NORMAL)
        else:
            self.swap_btn.config(state=DISABLED)
    
    def refresh_tree(self):
        for iid in self.tree.get_children():
            self.tree.delete(iid)
        self._load_teams()
        self.swap_btn.config(state=DISABLED)
