from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('authuser/',UserCreationView.as_view(),name='authuser'),
    path('authlog/',signview.as_view(),name='authlog'),
    path('authlogout/',logoutview.as_view(),name='authlogout'),
    path('travel-package-create/', TravelPackageCreateView.as_view(), name='travel-package-create'),
    path('travel-package-view/', TravelPackageListView.as_view(), name='travel-package-view'),
    path('travel-packages-update/<int:pk>/', TravelPackageDetailView.as_view(), name='travel-package-detail'),
    path('users/', UserRegListCreateView.as_view(), name='userreg-list-create'),
    path('users/<int:id>/', UserRegUpdateAPIView.as_view(), name='userreg-update-api'),
    path('users/<int:pk>/', UserRegDetailView.as_view(), name='userreg-detail-api'),
    # path('login/', obtain_auth_token, name='api_token_auth'),  # Use this line for Token authentication
    path('custom-login/', UserLoginView.as_view(), name='user-login'),  # Use this line for custom login without Token
]
