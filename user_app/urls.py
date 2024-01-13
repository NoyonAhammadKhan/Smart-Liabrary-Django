from django.urls import path
from .views import UserSignupView, UserLoginView, user_logout

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="signup"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout')
]
