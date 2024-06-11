from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import IndexView, SignUpView, UploadImageView

app_name = "giphy_app"

urlpatterns = [
  path("", IndexView.as_view(), name="index"),
  path(
    "login/",
    LoginView.as_view(
      template_name="giphy_app/login.html",
      next_page="giphy_app:index",
      redirect_authenticated_user=True,
    ),
    name="login",
  ),

  path(
    "logout/",
    LogoutView.as_view(next_page="giphy_app:index"),
    name="logout",
  ),
  path("signup/", SignUpView.as_view(), name="signup"),
  path("upload/", UploadImageView.as_view(), name="upload"),
]


# from django.urls import path
# from .views import IndexView, SignUpView, UploadImageView
# from django.contrib.auth.views import LoginView, LogoutView

# app_name = "giphy_app"


# urlpatterns = [
#      path('', IndexView.as_view(), name='index'),
#      path("login/", LoginView.as_view(template_name = "giphy_app/login.html", next_page = "giphy_app:index", redirect_authenticated_user = True,), name="login",),
#      path("logout/", LogoutView.as_view(next_page = "giphy_app:index"), name="logout",), 
#      path("signup/", SignUpView.as_view(), name="signup"),
#     path("upload/", UploadImageView.as_view(), name="upload"),
# ]
