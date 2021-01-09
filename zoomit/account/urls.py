from django.urls import path
from account.views import Login, Logout, RegisterView
from .api import user_list, user_details, UserViewSet
from zoomit.urls import router

router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('api/users/', UserViewSet.as_view(), name='users_list'),
]
