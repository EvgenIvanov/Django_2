from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView, UpdateView
from .models import BaseRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserProfile

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

class UserProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'user_profile.html'
    form_class = UserProfile

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return User.objects.get(pk=self.request.user.id)