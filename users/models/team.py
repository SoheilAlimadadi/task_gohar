from pydantic import (
    BaseModel,
    Field
)
from bson import ObjectId

from .user import User

class Team(BaseModel):

    _id: ObjectId
    title: str = Field(
        min_length=4,
        max_length=40,
        description="Title of the team",
        examples=["Back-end"]
    )
    members: list[User] = Field(
        description="Members of the team",
        examples=["soheil", "amir", "ali"]
    )

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"<Team: {self.title} -  \
                members: {[member for member in self.members]}>"
