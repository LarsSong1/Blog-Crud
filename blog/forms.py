from django import forms
from .models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class blogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['imagen','subtitulo','categoria', 'titulo', 'autor','informacion']

class loginForm(AuthenticationForm):
    pass

    # usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'usuario'}))
    # contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'contraseña'}))


class registroForm(UserCreationForm):
    pass
