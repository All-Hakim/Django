from . import views
from django.urls import path

urlpatterns = [
    path('accueil',views.accueil, name="accueil"),
    path('show/<train_id>',views.show, name="show"),
    path('random',views.random, name="random"),    
    path('create',views.create, name="create"),    

]
