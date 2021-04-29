from django.forms import ModelForm
from .models import Post
from django.contrib.auth.models import User

class NewForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_type',
            'category_id',
            'title',
            'text'
        ]