from django.forms import ModelForm
from .models import Post, Author


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('likes',)


class AddNewAuthor(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

