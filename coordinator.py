from agents.travel_agent import TravelAgent
from agents.hotel_agent import HotelAgent
from agents.restaurant_agent import RestaurantAgent
from agents.budget_agent import BudgetAgent

from router.intent_router import IntentRouter
from memory import TripMemory


class Coordinator:

    def __init__(self):

        self.travel = TravelAgent()
        self.hotel = HotelAgent()
        self.restaurant = RestaurantAgent()
        self.budget = BudgetAgent()

        self.router = IntentRouter()

        self.memory = TripMemory()

    def process(self,query,destination,days,budget,travel_style):

        self.memory.save(destination,days,budget,travel_style)

        intent = self.router.get_intent(query)

        if intent == "travel":

            return self.travel.run(destination,days,travel_style)

        elif intent == "hotel":

            return self.hotel.run(destination,budget)

        elif intent == "restaurant":

            return self.restaurant.run(destination)

        elif intent == "budget":

            return self.budget.run(days,budget)

        else:

            travel = self.travel.run(destination, days,travel_style)

            hotel = self.hotel.run(destination,budget)

            restaurant = self.restaurant.run(destination)

            budget_plan = self.budget.run(days,budget)

            return f"""
{travel}

---

{hotel}

---

{restaurant}

---

{budget_plan}
"""