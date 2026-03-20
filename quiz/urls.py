from django.urls import path
from . import views

app_name = "quiz"
urlpatterns = [
    # ex: /quiz/
    path("", views.index, name="index"),
    # ex: /quiz/5/
    path("<int:soru_id>/", views.detay, name="detay"),
    # ex: /quiz/5/sonuclar/
    path("<int:soru_id>/sonuclar/", views.sonuclar, name="sonuclar"),
    # ex: /quiz/5/cevapla/
    path("<int:soru_id>/cevapla/", views.cevapla, name="cevapla"),
]