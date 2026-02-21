from pydantic import BaseModel
from typing import Literal

class Preferences(BaseModel):
    learning_style: str
    intensity: Literal["low", "medium", "high"]

class UserProfile(BaseModel):
    domain: str
    goal: str
    current_level: str
    skills: list[str]
    experience_years: int
    timeline_months: int
    daily_hours: int
    age: int
    location: str
    constraints: list[str]
    resources_access: list[str]
    preferences: Preferences
