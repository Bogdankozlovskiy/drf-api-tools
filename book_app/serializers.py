from book_app.models import Books
from rest_framework.serializers import ModelSerializer


class BookSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"
