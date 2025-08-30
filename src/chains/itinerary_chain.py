from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY
from src.utils.weather import get_weather

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)

# Base prompt template
prompt_template = """You are a highly knowledgeable and friendly travel assistant that specializes in creating personalized day trip itineraries.

When generating an itinerary:
- Tailor the recommendations to the user's stated **city** and **interests**.
- Include a logical flow of activities, covering morning, afternoon, and evening.
- Incorporate **local experiences**, popular attractions, food options, and optional activities aligned with the interests.
- Keep the plan feasible within one day and optimize for minimal backtracking.
- Use **bullet points** for each time slot or activity for readability.
- Provide the travel time required to travel from the source to the destination site and whether it's a feasible choice or not. If not, provide alternatives.
- Keep descriptions **brief but engaging**, offering local flavor.
{weather_context}
Context:
City: {city}
User Interests: {interests}
"""

def generate_itinerary(city: str, interests: list[str]) -> str:
    # Fetch weather data
    weather_info = get_weather(city)

    weather_context_str = ""
    if weather_info:
        weather_context_str = f"""
- Also consider the current weather while planning:
  - **Weather**: {weather_info['condition']}
  - **Temperature**: {weather_info['temperature_celsius']}°C
  - **Wind**: {weather_info['wind_kph']} km/h
"""

    # Update the prompt with weather context
    formatted_prompt = prompt_template.format(
        weather_context=weather_context_str,
        city=city,
        interests=", ".join(interests)
    )

    # Create the chat prompt template
    itinerary_prompt = ChatPromptTemplate.from_messages([
        ("system", formatted_prompt),
        ("human", "Can you help me plan a fun and engaging one-day itinerary for my trip?")
    ])

    # Invoke the LLM
    response = llm.invoke(itinerary_prompt.format_messages())
    return response.content
