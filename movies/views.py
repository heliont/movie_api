# Importando restframework
from rest_framework import generics
# Obriga a requisição ter autenticação de usuário da API
from rest_framework.permissions import IsAuthenticated

# Importando o modelo Movie do app movies
from .models import Movie
from movies.serializers import MovieSerializer
# Permissão Global do Django-Admin
from core.permissions import GlobalDefaultPermissions


# View API | List | Create
class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# View API | List Detail | Update | Delete
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer