from pydantic import BaseModel

class FitnessQuery(BaseModel):
    question: str
    user_profile: str