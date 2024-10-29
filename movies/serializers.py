from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    # Verificação de data minima de filmes
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1990.")
        return value

    # Verificação de quantidade de caracteres permitidos
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("O resumo não pode ter mais de 2 caracteres.")
        return value