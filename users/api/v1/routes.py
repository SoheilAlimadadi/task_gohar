import logging
from fastapi import APIRouter
from pymongo.results import InsertOneResult
from pymongo.cursor import Cursor
from pymongo.command_cursor import CommandCursor

from database.collections import (
    user_collection,
    teams_collection
)
from .schemas import UserSchema, TeamCreate, TeamResponseSchema
from users.models import (
    User,
    Team
)

user_router = APIRouter()
usersLogger = logging.getLogger('users')


@user_router.post('/users', response_model=UserSchema)
async def create_user(user: UserSchema):
    """
    Create a new user.

    Args:
        user (UserSchema): The user data.

    Returns:
        UserSchema: The created user.

    """
    user_dict = user.model_dump()
    _: InsertOneResult = await user_collection.insert_one(user_dict)
    usersLogger.info(f"User '{user_dict['name']}' created")
    return UserSchema(**user_dict)


@user_router.get('/users', response_model=list[UserSchema])
async def get_users():
    """
    Get all users.

    Returns:
        List[UserSchema]: The list of users.

    """
    cursor: Cursor = user_collection.find()
    usersLogger.info("Retrieved users")
    return [document for document in await cursor.to_list(length=100)]


@user_router.get("/teams", response_model=list[TeamResponseSchema])
async def get_teams():
    """
    Get all teams.

    Returns:
        List[TeamResponseSchema]: The list of teams.

    """
    teams: CommandCursor = await teams_collection.aggregate([
        {
            "$unwind": "$members"
        },
        {
            "$sort": {"members.age": 1}
        },
        {
            "$group": {
                "_id": "$_id",
                "title": {"$first": "$title"},
                "members": {"$push": "$members"}
            }
        }
    ]).to_list(length=100)
    usersLogger.info("Retrieved teams")
    return teams


@user_router.post("/teams", response_model=TeamResponseSchema)
async def create_team(team: TeamCreate):
    """
    Create a new team.

    Args:
        team (TeamCreate): The team data.

    Returns:
        TeamResponseSchema: The created team.

    """
    users: Cursor = await user_collection.find(
        {"name": {"$in": team.members}}
    ).to_list(length=100)
    members = [User(**user) for user in users]
    team = Team(
        title=team.title,
        members=members
    )
    team_dict = team.model_dump()
    usersLogger.info(f"Team '{team_dict['title']}' created")
    _: InsertOneResult = await teams_collection.insert_one(team_dict)
    return TeamResponseSchema(**team_dict)
