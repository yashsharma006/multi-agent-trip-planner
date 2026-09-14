import json


class RestaurantAgent:

    def __init__(self):

        with open(
            "data/restaurants.json",
            "r",
            encoding="utf-8"
        ) as file:

            self.restaurants = json.load(file)

    def run(self, destination):

        result = []

        for restaurant in self.restaurants:

            if restaurant["city"].lower() == destination.lower():

                result.append(restaurant)

        if len(result) == 0:

            return "No restaurants found."

        result = sorted(
            result,
            key=lambda x: x["rating"],
            reverse=True
        )

        output = "## 🍽️ Restaurant Recommendations\n\n"

        for restaurant in result:

            output += f"""
### {restaurant['name']}

📍 Location: {restaurant['location']}

🍴 Cuisine: {restaurant['cuisine']}

⭐ Rating: {restaurant['rating']}

💰 Average Cost: ₹{restaurant['price']} for two

---

"""

        return output