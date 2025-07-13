import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Travel Planner", page_icon="💦")
st.title("AI Travel Itinerary Planner")
st.write("Plan Your Day Trip Itinerary by entering Your City & Interests")

with st.form("planner_form"):
    city = st.text_input("Enter the City Name For Your Trip")
    interests = st.text_input("Enter your Interests (comma-separated)")
    submitted = st.form_submit_button("Generate Itinerary")

    if submitted:
        if city and interests:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itinerary = planner.create_itinerary()

            st.subheader("📃 Your Itinerary")
            st.markdown(itinerary)
        else:
            st.warning("***** Please Fill City or Interests to move Forward *****")