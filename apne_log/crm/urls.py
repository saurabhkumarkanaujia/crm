from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    path('base/',views.base,name='base'),
    path('add_person/',views.add_person,name='add_person'),
    path('person_details/',views.person_details,name='person_details'),
]   
