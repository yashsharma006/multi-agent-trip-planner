import json


class HotelAgent:

    def __init__(self):

        with open(
            "data/hotels.json",
            "r",
            encoding="utf-8"
        ) as file:

            self.hotels = json.load(file)

    def run(self, destination, budget):

        result = []

        for hotel in self.hotels:

            if (
                hotel["city"].lower() == destination.lower()
                and hotel["price"] <= budget
            ):

                result.append(hotel)

        if len(result) == 0:

            return "No hotels found."

        result = sorted(
            result,
            key=lambda x: x["rating"],
            reverse=True
        )

        output = "## 🏨 Hotel Recommendations\n\n"

        for hotel in result:

            output += f"""
**{hotel['name']}**

📍 Location: {hotel['location']}

⭐ Rating: {hotel['rating']}

💰 Price: ₹{hotel['price']} / night

---

"""

        return output