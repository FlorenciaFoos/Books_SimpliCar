from django.conf.urls import url
from django.urls import path, include, re_path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #Libreria (ABM)
    path('library/<int:pk>', LibraryDetail.as_view()),
    # Libreria (Filtro)
    path('library/<int:library_pk>/books/<int:pk>',
         BookViewSet.as_view({'get': 'retrieve'})),
    # Libros (book detail)
    path('book/<int:pk>', BookDetail.as_view()),
    #Libros (Búsqueda)
    re_path('book/', BooksView.as_view({'get': 'list'})),
    # Autores (author detail)
    path('author/<int:pk>', AuthorDetail.as_view()),
    # Leads
    path('lead', LeadCreate.as_view()),

]
