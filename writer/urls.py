from django.urls import path
from .views import writepost,readpost,listposts

urlpatterns = [
    path('createpost/', writepost),
    path('listposts/', listposts),
    path('readepost/', readpost),
]