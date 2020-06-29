from django.urls import path

from converter.views import HTMLConverterAPIView


urlpatterns = [
    path("convert/html", HTMLConverterAPIView.as_view()),
]