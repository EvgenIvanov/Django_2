"""
Что вы должны сделать в консоли Django?

    Создать двух пользователей (с помощью метода User.objects.create_user).
    Создать два объекта модели Author, связанные с пользователями.
    Добавить 4 категории в модель Category.
    Добавить 2 статьи и 1 новость.
    Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
    Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
    Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
    Обновить рейтинги пользователей.
    Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
    Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
    Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

    откат миграций
    $ manage.py migrate --fake <appname> zero
    $ rm -rf migrations
    $ manage.py makemigrations <appname>
    $ manage.py migrate --fake <appname>
"""
"""
python manage.py makemigrations
python manage.py migrate

python manage.py shell

from news.models import Category
categories = ['Спорт','Культура','ИТ','Экономика','Литература','Мода','Религия']
for category in categories:
    Category.objects.create(name = category)from

from django.contrib.auth import get_user_model
UserModel = get_user_model()
user1 = UserModel.objects.create_user("Test User1", password="foo")
user1.save()

user2 = UserModel.objects.create_user("Test User2", password="foo")
user2.save()

from news.models import Author
Author.objects.create(user_id=user1)
Author.objects.create(user_id=user2)

auth1 = Author.objects.get(id=1)
auth2 = Author.objects.get(id=2)

from news.models import Post
article1 = Post()
article1.author_id = auth2
article1.post_type = article1.article
article1.title="Первая статья"
article1.text = "Это текст первой статьи"
article1.rating = 1.1

article2 = Post()
article2.author_id = auth2
article2.post_type = article2.article
article1.title="Вторая статья"
article1.text = "Это текст второй статьи"
article1.rating = 2.2
article2.save()

article3 = Post()
article3.author_id = auth1
article3.post_type = article2.news
article3.title="Первая НОВОСТЬ"
article3.text = "Это текст первой НОВОСТИ"
article3.rating = 1.5
article3.save()

cat1 = Category.objects.get(id=7)
cat2 = Category.objects.get(id=6)
from news.models import PostCategory
post_cat1 = PostCategory.objects.create(category_id=cat1, post_id=article1)
# article1.category_id.all()
# <QuerySet [<Category: Category object (7)>]>
post_cat2 = PostCategory.objects.create(category_id=cat2, post_id=article1)
# article1.category_id.all()
# <QuerySet [<Category: Category object (7)>, <Category: Category object (6)>]>
cat3 = Category.objects.get(id=5)
PostCategory.objects.create(category_id=cat3, post_id=article3)
cat4 = Category.objects.get(id=4)
cat5 = Category.objects.get(id=3)
PostCategory.objects.create(category_id=cat4, post_id=article2)
PostCategory.objects.create(category_id=cat5, post_id=article2)

from django.contrib.auth.models import User
user3 = User(username="Test User3",password="bar")
user3.save()

from news.models import (Comment, Post, Author)
from django.contrib.auth.models import User
comm1 = Comment()
comm1.post_id = Post.objects.get(id=1)
comm1.user_id = User.objects.get(id=1)
comm1.tweet = "Первый коммент к первой статье"
comm1.save()
del comm1
comm = Comment()
comm.post_id = Post.objects.get(id=1)
comm.user_id = User.objects.get(id=2)
comm.tweet = "Второй коммент к первой статье"
comm.save()
del comm
comm = Comment()
comm.post_id = Post.objects.get(id=1)
comm.user_id = User.objects.get(id=3)
comm.tweet = "Третий коммент к первой статье"
comm.save()
del comm
comm = Comment()
comm.post_id = Post.objects.get(id=2)
comm.user_id = User.objects.get(id=1)
comm.tweet = "Первый коммент ко второй статье"
comm.save()
del comm
comm = Comment()
comm.post_id = Post.objects.get(id=2)
comm.user_id = User.objects.get(id=2)
comm.tweet = "Второй коммент ко второй статье"
comm.save()
del comm
comm = Comment()
comm.post_id = Post.objects.get(id=2)
comm.user_id = User.objects.get(id=3)
comm.tweet = "Третий коммент ко второй статье"
comm.save()
del comm
comm = Comment()
comm.post_id = Post.objects.get(id=3)
comm.user_id = User.objects.get(id=1)
comm.tweet = "Первый коммент к первой НОВОСТИ"
comm.save()
del comm
comm = Comment()
comm.post_id = Post.objects.get(id=3)
comm.user_id = User.objects.get(id=2)
comm.tweet = "Второй коммент к первой НОВОСТИ"
comm.save()
del comm
comm = Comment()
comm.post_id = Post.objects.get(id=3)
comm.user_id = User.objects.get(id=3)
comm.tweet = "Третий коммент к первой НОВОСТИ"
comm.save()
del comm

comm = Comment.objects.get(id=9)
comm.like()
comm.save()

post = Post.objects.get(id=3)
post.text = "dadljaldal a ldjajdajd akd;kw;ekqk kkjdajdjodj jdljsdljldjaldkmmelne oijoaijdoijojxLdmla ljlajdljadjajdjasdijwoiao oijojASJLjsDLKJALJjsajd ooajdj douaojdlajdljlj jaojdoajdljalkdqwoie"
post.save()
post.preview()
post.like()
post.like()
post.like()
post.like()
post.dislike()
post.save()
del post
post = Post.objects.get(id=2)
post.dislike()
post.like()
post.save()
post = Post.objects.get(id=1)
post.like()
post.like()
post.like()
post.like()
post.dislike()

8.
import news.models as m
a = m.Author.objects.get(pk=2)
a.update_rating()
a = m.Author.objects.get(pk=1)
a.update_rating()

9.
author = m.Author.objects.all().order_by('-rating').first()
print(f'User name: "{author.user_id.username}"\nRating: {author.rating}')

10.
max_rating = m.Post.objects.aggregate(max_rating=Max('rating'))['max_rating']
best_post = m.Post.objects.filter(rating=max_rating).first()
print(f'Best post id: {best_post.id}\nDate created: {best_post.created.date().isoformat()}\nAuthor: "{best_post.author_id.user_id.username}"\nRating: {best_post.rating}\nTitle: {best_post.title}\nText preview: {best_post.preview()}')

11.
item = 0
for comment in comments:
 item += 1
 print(f'item #{item}\nDate created: {comment.created.date().isoformat()}\nUser: {comment.user_id.username}\nRating: {comment.rating}\nText: {comment.tweet}\n-------------------------')

"""