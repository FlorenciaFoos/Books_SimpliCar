from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, mixins
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from book.models import Library
from .serializers import *


#Libreria (ABM)

class LibraryDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#Libreria (Filtro)

class BookViewSet(ModelViewSet):
    """Viewset de book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self, *args, **kwargs):
        library_id = self.kwargs.get("library_pk")
        try:
            libraries = Library.objects.get(id=library_id)
        except Library.DoesNotExist:
            raise NotFound('No existe libreria con este ID')
        return self.queryset.filter(libraries=libraries)


# Libros (book detail)

class BookDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#Libros (Búsqueda)

class BooksView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['title']

    # def get_queryset(self):
    #     queryset = Book.objects.all()
    #     text = self.request.query_params.get('text', None)
    #     if text is not None:
    #         queryset = queryset.filter(title=text)
    #     return queryset


# Autores (author detail)

class AuthorDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Leads

class LeadCreate(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
