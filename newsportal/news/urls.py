from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, PostDetail, NewsSearch, PostCreate, \
                   PostUpdate, PostDelete, subscribe, unsubscribe
# from django.views.decorators.cache import cache_page

urlpatterns = [
   # path — означает путь.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   # path('', cache_page(60)(NewsList.as_view()), name='news'),
   path('', NewsList.as_view(), name='news'),
   # pk — это первичный ключ новости или категории, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   # path('<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post'),
   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('<int:pk1>/subscribe/<int:pk2>/', subscribe, name='subscribe'),
   path('<int:pk1>/unsubscribe/<int:pk2>/', unsubscribe, name='unsubscribe'),
   path('search/', NewsSearch.as_view(), name='news_search'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
