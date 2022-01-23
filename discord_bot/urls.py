from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import  static
from django.conf import settings
from discord_bot import views

app_name = 'discord_bot'

# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls.static import  static
# from django.conf import settings
# from portfolio import views


urlpatterns = [
    ## кавычки пустые, потому что, это домашная страница
    ## то есть самая первая
    path('', views.all_discord_bots, name='all_discord_bots'),
    path('all_discord_bots', views.all_discord_bots, name='all_discord_bots'),
    path('<int:discord_id>', views.detail, name='detail'),
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)