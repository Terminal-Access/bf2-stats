﻿
class BaseProcessor(object):

    def __init__(self):

        module_names = self.__class__.__module__.split('.')
        self.id = module_names[-1]
        self.processor_type = '.'.join(module_names[1:-1])
        self.type_index = 0
        self.priority = 100
        self.enabled = True

    def start(self):
        pass

    def post_process(self):
        pass

    def stop(self):
        pass

    def on_accuracy(self, e):
        pass

    def on_ammo(self, e):
        pass

    def on_assist(self, e):
        pass

    def on_ban(self, e):
        pass

    def on_chat(self, e):
        pass

    def on_clock_limit(self, e):
        pass

    def on_commander(self, e):
        pass

    def on_connect(self, e):
        pass

    def on_control_point(self, e):
        pass

    def on_disconnect(self, e):
        pass

    def on_death(self, e):
        pass

    def on_event(self, e):
        pass

    def on_flag_action(self, e):
        pass

    def on_game_status(self, e):
        pass

    def on_heal(self, e):
        pass

    def on_kick(self, e):
        pass

    def on_kit_drop(self, e):
        pass

    def on_kill(self, e):
        pass

    def on_kit_pickup(self, e):
        pass

    def on_loss(self, e):
        pass

    def on_repair(self, e):
        pass

    def on_reset(self, e):
        pass

    def on_revive(self, e):
        pass

    def on_score(self, e):
        pass

    def on_squad_leader(self, e):
        pass

    def on_spawn(self, e):
        pass

    def on_squad(self, e):
        pass

    def on_server_status(self, e):
        pass

    def on_team_damage(self, e):
        pass

    def on_ticket_limit(self, e):
        pass

    def on_team(self, e):
        pass

    def on_vehicle_destroy(self, e):
        pass

    def on_vehicle_enter(self, e):
        pass

    def on_vehicle_exit(self, e):
        pass

    def on_weapon(self, e):
        pass

    def on_win(self, e):
        pass
