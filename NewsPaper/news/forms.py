from django.forms import ModelForm
from .models import Post

class NewForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'author_id',
            'post_type',
            'category_id',
            'title',
            'text'
        ]