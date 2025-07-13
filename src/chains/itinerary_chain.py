from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY

llm = ChatGroq(
    GROQ_API_KEY = GROQ_API_KEY,
    model_name = "llama-3.3-70b-versatile",
    temperature = 0.3
)

itinerary_prompt = ChatPromptTemplate([
    (
        "system",
        """You are a highly knowledgeable and friendly travel assistant that specializes in creating personalized day trip itineraries.

        When generating an itinerary:
        - Tailor the recommendations to the user's stated **city** and **interests**.
        - Include a logical flow of activities, covering morning, afternoon, and evening.
        - Incorporate **local experiences**, popular attractions, food options, and optional activities aligned with the interests.
        - Keep the plan feasible within one day and optimize for minimal backtracking.
        - Use **bullet points** for each time slot or activity for readability.
        - Keep descriptions **brief but engaging**, offering local flavor.

        Context:
        City: {city}
        User Interests: {interests}
        """
    ),
    (
        "human",
        "Can you help me plan a fun and engaging one-day itinerary for my trip?"
    )
])

def generate_itinerary(city:str, interests:list[str]) -> str:
    response = llm.invoke(
        itinerary_prompt.format_messages(city = city, interests = ", ".join(interests))
    )
    return response.content
