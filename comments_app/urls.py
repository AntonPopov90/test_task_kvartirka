from django.urls import path

from . import views


urlpatterns = [
    path('article/', views.ArticleView.as_view()),
    path('article/<int:pk>/', views.ArticleDetailView.as_view()),
    path('comment/', views.CommentCreateView.as_view())
]