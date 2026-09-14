# AI Multi-Agent Trip Planner

An AI-powered travel planning application built with Python and Streamlit. The application creates personalized trip plans based on a user’s destination, travel duration, budget, travel style, and query.

## Features

- Generates AI-based day-wise travel itineraries
- Supports travel styles such as Budget, Luxury, Solo, Family, and Adventure
- Provides hotel recommendations based on destination and budget
- Suggests restaurants based on location and ratings
- Creates a detailed travel budget breakdown
- Uses intent-based routing to handle travel, hotel, restaurant, and budget queries
- Stores trip preferences in memory during processing
- Allows users to download generated trip plans
- Includes an interactive Streamlit user interface

## Technologies Used

- Python
- Streamlit
- LangChain
- Ollama
- Llama 3.2
- JSON
- Python Dotenv

## Project Structure

```text
travel_assistant_ai/
│
├── agents/
│   ├── travel_agent.py
│   ├── hotel_agent.py
│   ├── restaurant_agent.py
│   └── budget_agent.py
│
├── data/
│   ├── hotels.json
│   └── restaurants.json
│
├── router/
│   └── intent_router.py
│
├── utils/
│   └── llm.py
│
├── app.py
├── coordinator.py
├── memory.py
└── requirements.txt

How It Works
1. The user enters trip preferences such as destination, number of days, budget, and travel style.
2. The coordinator saves the trip information and identifies the user’s intent.
3. The intent router forwards the request to the relevant specialized agent.
4. The travel agent uses an LLM to generate a personalized itinerary.
5. The hotel and restaurant agents filter local JSON data and return highly rated recommendations.
6. The budget agent divides the travel budget across accommodation, food, transport, activities, and emergency expenses.
7. The generated plan is displayed in the Streamlit application and can be downloaded.
