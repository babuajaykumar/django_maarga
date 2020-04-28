from django.urls import path
from . import views


urlpatterns=[
    path('apartment',views.apartment, name='apartment'),
    path('apartmentsFilter',views.apartmentsFilter, name='apartmentsFilter'),
]
