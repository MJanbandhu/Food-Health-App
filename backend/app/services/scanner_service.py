from app.ai.food_detection import FoodDetectionAI

class ScannerService:
    @staticmethod
    def process_image(image_data):
        return FoodDetectionAI.detect_food_from_image(image_data)
