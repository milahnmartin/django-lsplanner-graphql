from graphene import ObjectType, List, Field, String
from lsplanner.models import User


class UserQuery(ObjectType):
    users = List(User)
    user = Field(User, username=String(required=True))

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_user(self, info, username):
        return User.objects.get(username=username)
