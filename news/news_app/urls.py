from django.urls import path
from .views import  ArticleView, ArticleDetailView

app_name="news_app"

urlpatterns=[
    path('', ArticleView.as_view() ),
    path('article/<int:pk>/', ArticleDetailView.as_view()),
]