import sys
sys.path.insert(0, "D:/clinic-service-api/Clinic-service-api")

from app.db.database import engine
from sqlalchemy import text

conn = engine.connect()
conn.execute(text("SELECT 1"))
print("Database connected successfully")
conn.close()
