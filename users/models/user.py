from pydantic import (
    BaseModel,
    Field,
    field_validator,
    ValidationError
)
from bson import ObjectId
from users.helpers import GendersEnum


class User(BaseModel):

    _id: ObjectId
    name: str = Field(
        min_length=4,
        max_length=40,
        description="Name of the user",
        examples=["soheil"]
    )
    gender: GendersEnum = Field(
        description="Gender of the user",
        examples=["male"]
    )
    age: int = Field(
        description="Age of the user",
        examples=[30]
    )

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<name: {self.name} - age: {self.age}>"
