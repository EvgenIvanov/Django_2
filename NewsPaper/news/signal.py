from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Post, PostCategory, Subsribers
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User

@receiver(m2m_changed, sender=Post.category_id.through)
def post_category_change(sender, instance, pk_set, action, **kwargs):
    if action == 'post_add':

        categories = instance.category_id.all()

        for category in categories:

            qs_subscr = category.subscribers.all()

            for subscr in qs_subscr:
                html_content = render_to_string('send_subscribers.html',{'post': instance, 'subscr': subscr})
                msg = EmailMultiAlternatives(
                    subject = f'Portal NewsPaper. We have a new article: {instance.title}',
                    body = 'body',
                    from_email = settings.DEFAULT_FROM_EMAIL,
                    to = [subscr.user.email]
                )
                msg.attach_alternative(html_content, "text/html")

                msg.send()



def send_week(show = 0):
    """
        определить список всех постов за неделю
        определить все категории, в полученном списке всех постов за неделю
        найти всех подписчиков, которые подписаны на категории, выбранных постов за неделю
    """
    today = datetime.today()
    weekNumber = today.strftime("%W")
    cats_of_the_week = Post.objects.values_list('category_id', flat=True).filter(created__week=weekNumber).distinct()
    qs_subscribers = Subsribers.objects.filter(category__in=cats_of_the_week).values('user_id').distinct()

    if show==1:
        print(f'weekNumber={weekNumber}')
        print(cats_of_the_week)
        print(qs_subscribers)

    for subscriber in qs_subscribers:
        """
            цикл по подписчикам
            находим все категории, на которые подписан пользователь
            находим все посты за неделю, на категории которых подписан пользователь
            отправляем сообщение
        """
        subscr_cats = Subsribers.objects.values_list('category', flat=True).filter(user_id=subscriber['user_id'])
        subscr_posts = PostCategory.objects.values_list('post_id',flat=True).filter(post_id_id__created__week=weekNumber,category_id__in=subscr_cats)
        qs_posts = Post.objects.filter(pk__in=subscr_posts)
        if show==1:
            print(f"subscriber: {subscriber['user_id']}")
            print(f"subscr categories: {subscr_cats}")
            print(f"subscr_posts: {subscr_posts}")
            print(f"qs_posts: {qs_posts}")

        if show==0:
            subscr = User.objects.get(pk=subscriber['user_id'])

            html_content = render_to_string('send_subscribers_weekly.html',{'posts': qs_posts, 'subscr': subscr})
            msg = EmailMultiAlternatives(
                subject = f'Portal NewsPaper. Weekly newsletter.',
                body = 'body',
                from_email = settings.DEFAULT_FROM_EMAIL,
                to = [subscr.email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()