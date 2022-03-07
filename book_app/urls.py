from django.urls import path
from book_app import views


app_name = "book_app"
urlpatterns = [
    path("books/", views.BookListCreateApi.as_view(), name="list-create-book"),
    path("books/<int:pk>/", views.RetiveUpdateDestroyBookAPI.as_view(), name="book-retrive-update-destroy")
]
