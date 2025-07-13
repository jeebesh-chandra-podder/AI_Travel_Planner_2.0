from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itinerary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.itinerary = ""

        logger.info("Initialized Travel Planner Instance")

    def set_city(self,city:str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("City Set Successfully")
        except Exception as e:
            logger.error(f"Error While Setting ******CITY***** : {e}")
            raise CustomException(f"Failed to set *****CITY***** , {e}")
        
    def set_interests(self,interests_str:str):
        try:
            self.interests = [i.strip() for i in interests_str.split(',')]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interests Set Successfully")
        except Exception as e:
            logger.error(f"Error While Setting ******INTERESTS***** : {e}")
            raise CustomException(f"Failed to set *****INTERESTS***** , {e}")
        
    def create_itinerary(self):
        try:
            logger.info(f"Generating Itinerary for {self.city} and for interests : {self.interests}")
            itinerary = generate_itinerary(self.city,self.interests)
            self.itinerary = itinerary
            self.messages.append(AIMessage(content=itinerary))
            logger.info("Itinerary Generated Successfully")
            return self.itinerary
        except Exception as e:
            logger.error(f"Error While Generating ******ITINERARY***** : {e}")
            raise CustomException(f"Failed to Generate *****ITINERARY***** , {e}")