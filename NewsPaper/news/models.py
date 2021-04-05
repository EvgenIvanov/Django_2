from django.db import models
from django.contrib.auth.models import User
from django.db.models import (Sum, F)

class Author(models.Model):
    user_id = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.FloatField(default = 0.0)

    def update_rating(self) :
        """
        суммарный рейтинг каждой статьи автора умножается на 3;
        суммарный рейтинг всех комментариев автора;
        суммарный рейтинг всех комментариев к статьям автора.
        """

        value = Post.objects.filter(author_id = self.pk).aggregate(total=Sum(F('rating')*3))['total']
        value += Comment.objects.filter(user_id = self.id).aggregate(total=Sum('rating'))['total']
        value += Comment.objects.filter(post_id__author_id = self.pk).aggregate(total=Sum('rating'))['total']
        self.rating = value
        self.save()

class Category(models.Model):
    name = models.CharField(unique = True, max_length = 50)

class Post(models.Model):
    author_id = models.ForeignKey(Author, on_delete = models.CASCADE)
    news = 'N'
    article = 'A'
    types = (
        (news, 'новость'),
        (article, 'статья')
    )
    post_type = models.CharField(max_length = 1, choices = types, default = news)
    created = models.DateTimeField(auto_now_add = True, editable = False)
    category_id = models.ManyToManyField(Category, through = 'PostCategory')
    title  = models.CharField(max_length = 150)
    text = models.TextField()
    rating = models.FloatField(default = 0.0)

    def preview(self):
        return self.text[0:124] + "..."

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1

    def get_absolute_url(self):
        return f'/news/{self.id}'

class PostCategory(models.Model):
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    tweet = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add = True)
    rating = models.FloatField(default = 0.0)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1