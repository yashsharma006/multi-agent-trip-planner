class TripMemory:

    def __init__(self):
        self.trip = {}

    def save(self, destination, days, budget, travel_style):

        self.trip = {
            "destination": destination,
            "days": days,
            "budget": budget,
            "travel_style": travel_style
        }

    def get_trip(self):
        return self.trip

    def update(self, key, value):
        self.trip[key] = value

    def clear(self):
        self.trip = {}