from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.db.session import Base
from datetime import datetime

class HealthLog(Base):
    __tablename__ = "health_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    metric_name = Column(String)
    metric_value = Column(String)
    logged_at = Column(DateTime, default=datetime.utcnow)
