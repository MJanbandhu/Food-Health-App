from app.ai.vertex_ai_client import vertex_client

class RecommendationLLM:
    @staticmethod
    def generate_recommendations(user_data):
        # Uses vertex_client
        return vertex_client.get_smart_recommendations()
