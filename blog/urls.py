from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # 127.0.0.1:8000
    path('', views.post_list, name='post_list'),
    # 127.0.0.1:8000/post/2
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
