from pydantic import BaseModel, Field
from typing import List

class SalesOutput(BaseModel):
    value: float = Field(description='Total value - Sum of all courses')
    courses: List[str] = Field(description='List of all courses')
    resume: str = Field(description='Resume and analysis of all sales')

def sales():
    sales = [
        ['AI for all', '2.000,00'],
        ['AI for all', '2.000,00'],
        ['AI for beginner', '1.000,00'],
        ['AI for beginner', '1.000,00'],
        ['AI for beginner', '1.000,00'],
    ]
    return sales