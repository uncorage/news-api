from django.urls import path
from news_app import views

app_name="news_app"

urlpatterns=[
    path('', views.snippet_list)
    # path('', ArticleView.as_view() ),
    # path('article/<int:pk>/', ArticleDetailView.as_view()),
]