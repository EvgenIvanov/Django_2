from django_filters import FilterSet
from .models import Post

class NewFilter(FilterSet):
    class Meta:
        model = Post
        # fields = ('created','title','author_id__user_id_id__username')
        # /news/search/?created__gt=2021-03-21&title__icontains=статья&author_id__user_id_id__username__icontains=user2
        fields = {
            'created': ['gt'],
            'title': ['icontains'],
            'author_id__user_id_id__username': ['icontains']
        }