from users.api.views import api_detail_user_view
from django.urls import path

urlpatterns = [
    path('<str:username>/', api_detail_user_view, name='detail'),
]
