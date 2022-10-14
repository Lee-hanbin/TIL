from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta:
        modes = Movie
        fields = '__all__'