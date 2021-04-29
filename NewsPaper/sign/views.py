import news
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserProfile, BaseRegisterForm
from django.core.mail import send_mail
from news.models import Category, Subsribers

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def upgarde_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/news/')

@login_required
def subscribe(request):
    user = request.user
    qs = request.GET
    category = Category.objects.get(pk=qs.get('catID'))
    if not Subsribers.objects.filter(user=user, category=category).exists():
        Subsribers.objects.create(user=user, category=category)
        send_mail(
                subject = 'sublist on the news portal NewsPaper',
                message = f'Hello {user.username}! You subscribed to the category {category.name} on the news portal NewsPaper.',
                from_email = 'evgen2007@bk.ru',
                recipient_list = [f'{user.email}']
            )
        return redirect(f'/subscribe/{category.id}')
    else:
        return redirect('/')

class UserProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'user_profile.html'
    form_class = UserProfile
    success_url = '/sign/profile/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return User.objects.get(pk=self.request.user.id)
