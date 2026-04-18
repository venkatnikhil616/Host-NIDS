from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from database.db import Base


# SYSTEM LOG MODEL

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)

    # System stats
    cpu = Column(Float, default=0.0)
    memory = Column(Float, default=0.0)
    disk = Column(Float, default=0.0)

    # Optional process info
    process_name = Column(String, nullable=True)
    process_cpu = Column(Float, nullable=True)

    # Event type
    event_type = Column(String, default="system")

    # Timestamp
    timestamp = Column(DateTime, default=datetime.utcnow)

# ALERT MODEL

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    # Alert details
    message = Column(String, nullable=False)
    severity = Column(String, default="LOW")   # LOW / MEDIUM / HIGH
    source = Column(String, default="system")  # system / process / file

    timestamp = Column(DateTime, default=datetime.utcnow)


# FILE EVENTS MODEL

class FileEvent(Base):
    __tablename__ = "file_events"

    id = Column(Integer, primary_key=True, index=True)

    file_path = Column(String, nullable=False)
    event_type = Column(String)  # created / modified / deleted

    timestamp = Column(DateTime, default=datetime.utcnow)


# PROCESS EVENTS MODEL

class ProcessEvent(Base):
    __tablename__ = "process_events"

    id = Column(Integer, primary_key=True, index=True)

    pid = Column(Integer)
    name = Column(String)
    cpu = Column(Float)

    event_type = Column(String)  # new / suspicious

    timestamp = Column(DateTime, default=datetime.utcnow)
