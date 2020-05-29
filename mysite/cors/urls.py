from django.urls import path
from . import views
urlpatterns = [
    path('user/', views.current_user, name='curent_user_data'),
    path('new-user/', views.create_user, name="crete_new_user"),
]