from utils.llm import get_llm


class TravelAgent:

    def __init__(self):
        self.llm = get_llm()

    def run(self, destination, days, travel_style):

        prompt = f"""
You are a travel planner.

Create a {days}-day itinerary for {destination}.

Travel Style: {travel_style}

Return:

1. Overview
2. Day-wise itinerary
3. Top attractions
4. Best food
5. Tips

Keep it concise.
"""

        response = self.llm.invoke(prompt)

        return response.content