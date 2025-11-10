from django.urls import path

 # from recipes.views import home a linha de baixo resolve

from . import views     #  igual from recipes import views, ouseja a partir da pasta onde estou

urlpatterns = [
   # path('', home),     # Home
   path('', views.home),
   path('recipes/<int:id>/', views.recipe),
]
