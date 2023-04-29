from django.urls import path

from onepiece import views

app_name = "onepiece"
urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:character_id>/",views.detail,name="detail")
]
