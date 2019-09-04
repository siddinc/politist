from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import Search


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
    #overriding the default field labels
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Name'
        self.fields['email'].label = 'Email'

class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('topic_search',)
        widgets = {
            'topic_search': forms.TextInput(attrs = {'class': 'form-control form-control-lg',
                                                        'placeholder': 'Type something...'}),
        }
