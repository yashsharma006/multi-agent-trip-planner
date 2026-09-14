class BudgetAgent:

    def run( self, days,budget):

        hotel = budget * 0.40
        food = budget * 0.25
        transport = budget * 0.15
        activities = budget * 0.15
        emergency = budget * 0.05

        per_day = budget / days

        return f"""
## 💰 Budget Planner

### Budget Breakdown

🏨 Hotel: ₹{hotel:.0f}

🍽️ Food: ₹{food:.0f}

🚕 Transport: ₹{transport:.0f}

🎯 Activities: ₹{activities:.0f}

🆘 Emergency: ₹{emergency:.0f}

---

### Daily Budget

💵 ₹{per_day:.0f} per day

---

### Budget Tips

• Book hotels early.

• Use local transport.

• Eat at local restaurants.

• Keep an emergency budget.

• Avoid overspending on shopping.
"""