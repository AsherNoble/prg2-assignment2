from tkinter import *
from ErrorView import ErrorView
from RedButton import red_button
from TkUtils import TkUtils as ut
from model.exception.FillException import FillException
from model.exception.InvalidSigningException import InvalidSigningException

class TeamDashboardView:
    def __init__(self, root, model):
        self.root = root
        self.model = model

        self.player_search_var = StringVar()
        self.players_tree = None
        self.sign_btn = None
        self.unsign_btn = None
        self.slot_labels = []

    def control(self):
        ut.image(self.root, "image/banner.png").pack()
        ut.separator(self.root).pack(fill=X, pady=(0, 10))

        manager = self.model.get_logged_in_manager()
        self.team = manager.get_team() if manager else None
        team_name = self.team.get_team_name() if self.team else "No Team Selected"
        ut.label(self.root, team_name).pack()
        ut.separator(self.root).pack(fill=X, pady=(10, 10))

        sign_row = Frame(self.root)
        sign_row.pack(fill=X, padx=24, pady=(0, 10))

        ut.label(sign_row, "Sign a new player:").pack(side=LEFT, padx=(0, 8))
        entry = Entry(sign_row, textvariable=self.player_search_var, width=28)
        entry.pack(side=LEFT)

        self.sign_btn = red_button(sign_row, "Sign", self.on_sign)
        self.sign_btn.config(state=DISABLED)
        self.sign_btn.pack(side=LEFT, padx=(8, 0))

        self.player_search_var.trace_add("write", lambda *_: self._update_sign_state())

        mid = Frame(self.root)
        mid.pack(fill=BOTH, expand=True, padx=24, pady=(8, 12))

        left = Frame(mid)
        left.pack(side=LEFT, fill=BOTH, expand=True)

        self.players_tree = ut.treeview(left, ["Name", "Position"], multi=False, width=420)
        self.players_tree.pack(fill=BOTH, expand=True)
        self._load_players(self.team)

        right = Frame(mid)
        right.pack(side=LEFT, fill=BOTH, expand=True, padx=(16, 0))

        ut.label(right, "Active Team").pack(pady=(0, 6))
        self._build_active_grid(right)
        self._refresh_slots()   

        bottom = Frame(self.root)
        bottom.pack(fill=X, pady=(6, 0))

        self.unsign_btn = red_button(bottom, "Unsign", self.on_unsign)
        self.unsign_btn.config(state=DISABLED)
        self.unsign_btn.pack(side=LEFT, expand=True, fill=X)

        red_button(bottom, "Close", self.root.destroy).pack(side=LEFT, expand=True, fill=X)

        self.players_tree.bind("<<TreeviewSelect>>", self._on_select_row)
        
    def _build_active_grid(self, parent):
        grid = Frame(parent, bg="#FFFFFF")
        grid.pack(fill=BOTH, expand=True)

        positions = [(0,1), (1,0), (1,1), (1,2), (2,1)]
        for idx, (r, c) in enumerate(positions):
            holder = Frame(grid, bg="#FFFFFF")
            holder.grid(row=r, column=c, padx=15, pady=15, sticky="n")
            label = ut.image(holder, "image/none.png", height=64, width=64, background="#FFFFFF")
            label.pack()
            label.bind("<Button-1>", lambda e, i=idx: self._on_slot_click(i))
            self.slot_labels.append(label)

        for col in (0, 1, 2):
            grid.grid_columnconfigure(col, weight=1)

            
    def _on_slot_click(self, i: int):
        current = self.team.current_team
        selected_player = self._get_selected_player()

        slot_player = current[i]

        if selected_player is None:
            if slot_player is not None:
                current[i] = None
                self._refresh_slots()
            return

        for j, player in enumerate(current):
            if player is selected_player:
                current[j] = None
                break

        if slot_player is None:
            current[i] = selected_player
        else:
            current[i] = selected_player

        self._refresh_slots()
        

    def _get_selected_player(self):
        selection = self.players_tree.selection()
        if not selection:
            return None
        selected_name = self.players_tree.item(selection[0])["values"][0]
        
        pool = self.team.get_all_players().get_players()

        for player in pool:
            if player.get_full_name() == selected_name:
                return player
        return None
    
    
    def _refresh_slots(self):
        jersey_active = f"image/{self.team.get_team_name().lower()}.png"
        jersey_empty = "image/none.png"

        for index, label in enumerate(self.slot_labels):
            player = self.team.current_team[index]
            image_path = jersey_active if player else jersey_empty

            temp = ut.image(label.master, image_path, height=64, width=64, background="#FFFFFF")
            label.configure(image=temp.photo)
            label.photo = temp.photo

            tooltip = "Empty slot" if player is None else f"{player.get_full_name()} ({player.get_position()})"
            ut.attach_tooltip(label, tooltip)


    def _load_players(self, team):
        players = team.get_all_players().get_players() if team else []
        for player in players:
            self.players_tree.insert(
                "", "end",
                values=(player.get_full_name(), player.get_position())
            )
            

    def _update_sign_state(self):
        text = self.player_search_var.get().strip()
        self.sign_btn.config(state=NORMAL if text else DISABLED)
        

    def _on_select_row(self, _event):
        has_sel = bool(self.players_tree.selection())
        self.unsign_btn.config(state=NORMAL if has_sel else DISABLED)
        

    def on_sign(self):
        text = self.player_search_var.get().strip()
        if not text:
            return

        try:
            player = self.model.get_players().player(text)

            if player is None:
                raise InvalidSigningException("Player does not exist within the league")

            if player.get_team() == self.team:
                raise InvalidSigningException(f"{player.get_full_name()} is already signed to your team")
            
            if player.get_team() is not None:
                raise InvalidSigningException(f"Cannot sign {player.get_full_name()}, player is already signed to {player.get_team()}")
 

            self.team.get_all_players().add(player)
            player.set_team(self.team)
            self._refresh()

        except Exception as error:
            win = ut.top_level("Error")
            win.title("Error")
            ErrorView(win, self.model, error).control()
            
            win.transient(self.root)
            win.grab_set()
            win.focus_set()
        

    def on_unsign(self):
        try:
            player = self._get_selected_player()
            
            if player in self.team.current_team:
                raise FillException(f"Cannot remove {player.get_full_name()}, player is in the active team")
            
            self.team.get_all_players().remove(player)
            player.set_team(None)
            self._refresh()
            
        except Exception as error:
            win = ut.top_level("Error")
            win.title("Error")
            ErrorView(win, self.model, error).control()
            
            win.transient(self.root)
            win.grab_set()
            win.focus_set()
        

    def _refresh(self):
        ut.same_window("Team Dashboard", self.root)
        TeamDashboardView(self.root, self.model).control()
