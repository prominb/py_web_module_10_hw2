from django.urls import path
from . import views


app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),  # AAAAA
    # path('<int:page>', views.main, name='main_paginate'),  # AAAAA
    path('tag/', views.tag, name='tag'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('author/<int:author_id>', views.author, name='author'),  # https://quotes.toscrape.com/author/Madeleine-LEngle/ https://quotes.toscrape.com/author/J-K-Rowling/
    # path('note/', views.note, name='note'),
    # path('detail/<int:note_id>/', views.detail, name='detail'),
    # path('done/<int:note_id>', views.set_done, name='set_done'),
    # path('', views.index, name='index'),  # HERE <==
    # ex: /polls/5/
    # path('<int:quotes_id>/', views.detail, name='detail'),  # HERE <==
]
