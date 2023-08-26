from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    """
    Schema for representing a user.

    Attributes:
        name (str): The name of the user.
        gender (str): The gender of the user.
        age (int): The age of the user.

    """

    name: str
    gender: str
    age: int


class TeamSchema(BaseModel):
    """
    Schema for representing a team.

    Attributes:
        title (str): The title of the team.

    """

    title: str


class TeamCreate(BaseModel):
    """
    Model for creating a team.

    Attributes:
        title (str): The title of the team.
        members (list): A list of team members.

    """

    title: str
    members: list[str] = Field(..., min_items=1)


class TeamMemberSchema(BaseModel):
    """
    Schema for representing a team member.

    Attributes:
        name (str): The name of the team member.
        age (int): The age of the team member.

    """

    name: str
    age: int


class TeamResponseSchema(BaseModel):
    """
    Schema for representing a team response.

    Attributes:
        title (str): The title of the team.
        members (list): A list of team members.

    """

    title: str
    members: list[TeamMemberSchema]
