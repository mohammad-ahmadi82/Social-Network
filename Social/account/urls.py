from django.urls    import path
from .              import views


app_name = 'account'

urlpatterns = [
    path('register/',               views.UserRegisterView.as_view(),           name='register'),
    path('login/',                  views.UserLoginView.as_view(),              name='login'),
    path('logout/',                 views.UserLogoutView.as_view(),             name='logout'),
    path('profile/<int:user_id>/',  views.UserProfileView.as_view(),            name='profile'),
    path('reset/',                  views.UserPasswordResetView.as_view(),      name='reset_password'),
]
