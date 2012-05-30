﻿
import models

from processors import BaseProcessor
from models import model_mgr
from stats import stat_mgr

class Processor(BaseProcessor):

    def __init__(self):
        BaseProcessor.__init__(self)

        self.priority = 10

    def on_commander(self, e):

        # Remove the commander flag from the previous player
        if e.team.commander_id:
            old_player = model_mgr.get_player(e.team.commander_id)
            if old_player:
                old_player.commander = False

        # Update the commander for the team
        e.team.commander_id = e.player.id

        # Add the commander flag to the new player
        e.player.commander = True

    def on_connect(self, e):

        # Update the connection flag for the player
        e.player.connected = True
        e.player.artificial = (e.player.address == None)

    def on_disconnect(self, e):

        # Update the connection flags for the player
        e.player.connected = False

    def on_kit_drop(self, e):
    
        # Update the kit for the player
        e.player.kit_id = e.kit.id

    def on_kit_pickup(self, e):
    
        # Update the kit for the player
        e.player.kit_id = None

    def on_spawn(self, e):

        # Update the team for the player
        self._update_team(e.player, e.team)

    def on_squad(self, e):

        # Make sure the squad is associated with a team
        if e.squad != models.squads.EMPTY:
            team = model_mgr.get_team(e.player.team_id)
            team.squad_ids.add(e.squad.id)

        # Remove the player from the previous squad
        if e.player.squad_id:
            old_squad = model_mgr.get_squad(e.squad.id)
            if old_squad and old_squad != models.squads.EMPTY:
                old_squad.player_ids.remove(e.player.id)
                if old_squad.leader_id == e.player.id:
                    old_squad.leader_id = None

        # Add the player to the new squad
        e.squad.player_ids.add(e.player.id)

        # Update the squad for the player
        e.player.squad_id = e.squad.id

        # Remove the squad leader flag from the player if needed
        if e.player.squad_id == models.squads.EMPTY.id:
            e.player.leader = False

    def on_squad_leader(self, e):

        # Remove the squad leader flag from the previous player
        if e.squad.leader_id:
            old_player = model_mgr.get_player(e.squad.leader_id)
            if old_player:
                old_player.leader = False

        # Update the leader for the squad
        e.squad.leader_id = e.player.id

        # Add the squad leader flag to the new player
        e.player.leader = True

    def on_team(self, e):

        # Update the team for the player
        self._update_team(e.player, e.team)

    def on_vehicle_enter(self, e):

        # Update the vehicle for the player
        e.player.vehicle_id = e.vehicle.id

    def on_vehicle_exit(self, e):

        # Update the vehicle for the player
        e.player.vehicle_id = None

    def on_weapon(self, e):

        # Update the weapon for the player
        e.player.weapon_id = e.weapon.id

    def _update_team(self, player, team):

        # Check whether the team needs to be updated
        if player.team_id and player.team_id == team.id:
            return

        # Remove the player from the previous team
        if player.team_id:
            old_team = model_mgr.get_team(player.team_id)
            if old_team:
                old_team.players_ids.remove(player.id)
                if old_team.commander_id == player.id:
                    old_team.commander_id = None
                    player.commander = False

        # Add the player to the new team
        team.player_ids.add(player.id)

        # Update the team for the player
        player.team_id = team.id