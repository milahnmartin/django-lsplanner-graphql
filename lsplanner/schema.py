import graphene
from graphene_django.types import DjangoObjectType

from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, username=graphene.String())
    user_by_id = graphene.Field(UserType, id=graphene.ID(required=True))

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_user(self, info, username):
        return User.objects.get(username=username)

    def resolve_user_by_id(self, info, id):
        return User.objects.get(pk=id)

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, username, email, password):
        user = User(username=username, email=email, password=password)
        user.save()
        return CreateUser(user=user)

class UpdateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, username, email, password):
        user = User(username=username, email=email, password=password)
        user.save()
        return UpdateUser(user=user)

class DeleteUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        
    user = graphene.Field(UserType)

    def mutate(self, info, username):
        user = User.objects.get(username=username)
        user.delete()
        return DeleteUser(user=user)
    

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

    
    
schema = graphene.Schema(query=Query, mutation=Mutation)
