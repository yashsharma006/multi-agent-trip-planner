class IntentRouter:

    def get_intent(self, query):

        query = query.lower()

        if any(word in query for word in [
            "hotel",
            "stay",
            "resort",
            "room"
        ]):
            return "hotel"

        elif any(word in query for word in [
            "restaurant",
            "food",
            "eat",
            "cafe"
        ]):
            return "restaurant"

        elif any(word in query for word in [
            "budget",
            "cost",
            "money",
            "expense"
        ]):
            return "budget"

        elif any(word in query for word in [
            "plan",
            "trip",
            "travel",
            "itinerary",
            "visit"
        ]):
            return "travel"

        else:
            return "all"