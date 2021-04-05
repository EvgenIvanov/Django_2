from django.urls import path
from .views import PostsList, PostSearch, PostDetail, PostCreate, PostDelete, PostUpdate

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='new_detail'),
    path('<int:pk>/delete', PostDelete.as_view(), name='new_delete'),
    path('add/', PostCreate.as_view(), name='new_add'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='new_add'),
    path('search/', PostSearch.as_view()),
]