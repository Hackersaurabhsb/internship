from django.urls import path
from . import views
urlpatterns=[
    path("",views.registration,name="home_page"),
    path('clients/',views.Client_list_create_api_view.as_view(),name='client_list'),
    path('artists/',views.Artist_list_create_api_view.as_view(),name='artist-list'),
    path('works/',views.Work_list_create_api_view.as_view(),name='work-list'),
]