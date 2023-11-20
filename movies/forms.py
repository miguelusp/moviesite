
from .models import Movie, Review
from django.forms import ModelForm
from .models import Movie, Review, Provider



class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = [
            'name',
            'release_year',
            'poster_url',
        ]
        labels = {
            'name': 'Nome do Jogador',
            'release_year': 'Ano de aposentadoria',
            'poster_url': 'URL do Poster do Jogador',
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }

class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = [
        ]
        labels = {
        } 