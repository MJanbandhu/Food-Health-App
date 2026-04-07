class HealthService:
    @staticmethod
    def analyze_health(total_calories: int, daily_goal: int):
        alerts = []
        if total_calories > daily_goal:
            alerts.append("Warning: You have exceeded your daily calorie goal!")
        elif total_calories < (daily_goal * 0.5):
            alerts.append("Notice: You are tracking very few calories today. Make sure you are eating enough.")
        return alerts
