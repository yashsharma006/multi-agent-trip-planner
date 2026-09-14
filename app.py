import streamlit as st
from coordinator import Coordinator

st.set_page_config(
    page_title="AI Multi-Agent Trip Planner",
    page_icon="✈️",
    layout="wide"
)

# ---------------- Custom CSS ---------------- #

st.markdown("""
<style>

.main{
    background:#F5F7FA;
}

.block-container{
    padding-top:2rem;
}

h1{
    text-align:center;
    color:#0E76FD;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.15);
}

.metric{
    background:#ffffff;
    padding:15px;
    border-radius:10px;
    text-align:center;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ---------------- Header ---------------- #

st.title("✈️ AI Multi-Agent Trip Planner")
st.caption("Travel • Hotels • Restaurants • Budget")

# ---------------- Sidebar ---------------- #

st.sidebar.title("🧳 Plan Your Trip")

destination = st.sidebar.text_input(
    "Destination",
    "Goa"
)

days = st.sidebar.slider(
    "Days",
    1,
    15,
    3
)

budget = st.sidebar.slider(
    "Budget (₹)",
    5000,
    100000,
    20000,
    1000
)

travel_style = st.sidebar.selectbox(
    "Travel Style",
    [
        "Budget",
        "Luxury",
        "Solo",
        "Family",
        "Adventure"
    ]
)

query = st.sidebar.text_input(
    "Ask your Assistant",
    "Plan everything"
)

generate = st.sidebar.button(
    "🚀 Generate Trip",
    use_container_width=True
)

# ---------------- Metrics ---------------- #

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("📍 Destination",destination)

with col2:
    st.metric("📅 Days",days)

with col3:
    st.metric("💰 Budget",f"₹{budget:,}")

with col4:
    st.metric("🎒 Style",travel_style)

# ---------------- Generate ---------------- #

if generate:

    coordinator = Coordinator()

    with st.spinner("🤖 AI Agents are Planning..."):

        result = coordinator.process(
            query,
            destination,
            days,
            budget,
            travel_style
        )

    st.success("✅ Trip Generated Successfully")

    st.markdown("---")

    st.markdown(result)

    st.download_button(
        "📥 Download Trip",
        result,
        file_name="trip_plan.txt"
    )