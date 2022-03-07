from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from book_app.models import Books
from book_app.serializers import BookSerializer


class BookListCreateApi(ListCreateAPIView):
    queryset = Books.objects
    serializer_class = BookSerializer


class RetiveUpdateDestroyBookAPI(RetrieveUpdateDestroyAPIView):
    queryset = Books.objects
    serializer_class = BookSerializer
