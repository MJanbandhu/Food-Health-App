class CalorieService:
    @staticmethod
    def calculate_daily_total(meals):
        return sum(meal.calories for meal in meals)
