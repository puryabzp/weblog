from django.urls import path
from account.views import Login, Logout, RegisterView
from .api import user_list,user_details

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('api/users/', UserViewSet.as_view(), name='users_list'),
    path('api/users/', user_list, name='users_list'),
    path('api/users/<int:pk>/', user_details, name='user_detail')
]
