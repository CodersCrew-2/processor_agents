from pydantic import BaseModel
from typing import Literal, Optional

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

class Question(BaseModel):
    id: str
    text: str
    input_type: Literal["text", "number", "radio", "dropdown", "multiselect"]
    options: Optional[list[str]] = None
    required: bool = True

class QuestionResponse(BaseModel):
    message: str
    questions: list[Question]

class CareerOverview(BaseModel):
    annual_income: str
    job_growth: str
    time_to_proficiency: str

class CareerOption(BaseModel):
    name: str
    description: str
    overview: CareerOverview
    requirements: list[str]
    youtube: str

class ResultData(BaseModel):
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
    options: list[CareerOption]

class AgentResponse(BaseModel):
    type: Literal["question", "result"]
    data: QuestionResponse | ResultData
