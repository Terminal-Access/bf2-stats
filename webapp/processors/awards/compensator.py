
from processors.awards import AwardProcessor,Column,PLAYER_COL
from models.vehicles import ARMOR
from timer import Timer

class Processor(AwardProcessor):
    '''
    Overview
    This processor keeps track of the amount of time a player spends driving
    tanks.

    Implementation
    This implementation uses the timer object to automatically compute elapsed
    time based on game ticks as events are processed.

    Notes
    None.
    '''

    def __init__(self):
        AwardProcessor.__init__(self, 'Compensator',
                'Most Time Driving Tanks',
                [PLAYER_COL, Column('Time', Column.TIME, Column.DESC)])

        # Setup the results to store timers instead of numbers
        self.results = dict()

    def on_vehicle_enter(self, e):

        # Create a timer for the player as needed
        if not e.player in self.results:
            self.results[e.player] = Timer()

        # Start the timer for armor vehicles
        vehicle_type = e.vehicle.vehicle_type;
        if e.player.driver and vehicle_type == ARMOR:
            self.results[e.player].start(e.tick)

    def on_vehicle_exit(self, e):

        # Stop the timer for the player
        self.results[e.player].stop(e.tick)
