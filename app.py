import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

# Load environment variables (for API keys or config)
load_dotenv()

# ------------------------
# PAGE CONFIGURATION
# ------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="💦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ------------------------
# HEADER STYLING
# ------------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        text-align: center;
        color: #1F4E79;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        text-align: center;
        font-size: 1.1rem;
        color: #444;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #1F4E79;
        color: white;
        font-weight: 600;
        padding: 0.6rem 2rem;
        border-radius: 0.5rem;
        transition: 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #14416b;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">🌐 AI Travel Itinerary Planner</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Plan a personalized one-day trip by entering your city and interests</div>', unsafe_allow_html=True)

# ------------------------
# FORM UI
# ------------------------
with st.form("planner_form"):
    col1, col2 = st.columns(2)

    with col1:
        city = st.text_input("🏙️ Enter the City", placeholder="e.g., Paris")
    with col2:
        interests = st.text_input("🎯 Your Interests", placeholder="e.g., art, food, history")

    submitted = st.form_submit_button("Generate Itinerary 🚀")

# ------------------------
# OUTPUT AREA
# ------------------------
if submitted:
    if city.strip() and interests.strip():
        with st.spinner("🧠 Crafting your personalized itinerary..."):
            planner = TravelPlanner()
            planner.set_city(city.strip())
            planner.set_interests(interests.strip())
            itinerary = planner.create_itinerary()

        st.markdown("### 📃 Your Personalized Day Itinerary")
        st.success("✅ Trip plan generated successfully!")
        st.markdown(itinerary)
    else:
        st.warning("⚠️ Please fill in both the **City** and **Interests** fields to continue.")
