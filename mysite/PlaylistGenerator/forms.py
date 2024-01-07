from django import forms


class ParamsForm(forms.Form):
    genres = forms.CharField(label="genres", max_length=100)
    artists = forms.CharField(label="artists", max_length=100)
    tracks = forms.CharField(label="tracks", max_length=100)
