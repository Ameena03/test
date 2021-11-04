from django.urls import path
from users.views import *

app_name = 'posts'

urlpatterns = [
    path('', post, name="post_list"),
    path('<int:pk>/', PostDetailView, name='post_detail'),
    path('<pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('<pk>/update/', PostUpdateView.as_view(), name="post-update"),
]
