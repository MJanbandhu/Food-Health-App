from app.ai.recommendation_llm import RecommendationLLM

class RecommendationService:
    @staticmethod
    def get_recommendations(user_id: int):
        return RecommendationLLM.generate_recommendations({"user_id": user_id})
