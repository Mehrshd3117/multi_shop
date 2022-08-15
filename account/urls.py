from django.urls import path
from . import views


app_name = "account"

urlpatterns = [
    path("login", views.UserLogin.as_view(), name="login"),
    path("logout", views.UserLogout.as_view(), name="logout"),
    path("register", views.UserRegister.as_view(), name="register"),
    path("profile/", views.UserEdit.as_view(), name="user_edit"),
    path("password_change/", views.PasswordChange.as_view(), name="password_change"),
    path("password_change_done/", views.PasswordChangeDone.as_view(), name="password_change_done"),
    path("password_reset/", views.UserPasswordReset.as_view(), name="password_reset"),
    path("password_reset/done/", views.USerPasswordResetDone.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>", views.UserPasswordResetConfirm.as_view(), name="password_reset_confirm"),
    path("reset/done/", views.UserPasswordResetComplete.as_view(), name="password_reset_complete"),

]

