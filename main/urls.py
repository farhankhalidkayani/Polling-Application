from django.urls import path
from main import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.detail, name="detail"),
    path("result/<int:id>", views.result, name="result"),
    path("deleteQuestion/<int:pk>", views.delete_question, name="deletequestion"),
    path("addOption/<int:id>", views.add_option, name="addoption"),
    path("updateQuestion/<int:pk>", views.update_question, name="updatequestion"),
    path("addQuestion/", views.add_question, name="addquestion"),
]
