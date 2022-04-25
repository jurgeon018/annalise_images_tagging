from django.urls import path
from images.api.views import (
    ImageList,
    ImageDetail,
    TagList,
    TagDetail,
)


urlpatterns = [
    path('images/', ImageList.as_view()),
    path('image/<pk>/', ImageDetail.as_view()),
    path('tags/', TagList.as_view()),
    path('tags/<pk>/', TagDetail.as_view()),
]
