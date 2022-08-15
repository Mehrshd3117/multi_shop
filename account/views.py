from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, UpdateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

from django.contrib.auth import login, logout, authenticate
from . import forms
from account.models import User


class UserLogin(View):
    form_class = forms.LoginForm
    template_name = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:main')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect("home:main")
            messages.error(request, 'Your username or password is wrong')
        return render(request, self.template_name, {'form': form})


class UserRegister(View):
    form_class = forms.RegisterForm
    template_name = 'account/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:main')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                password=cd['password1']
            )
            login(request, user)
            return redirect('home:main')
        return render(request, self.template_name, {'form': form})


class UserLogout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home:main')


class UserEdit(UpdateView):
    model = User
    form_class = forms.UserCreationForm
    template_name = 'account/user_profile.html'

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


# Password change
class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy("account:password_change_done")
    template_name = "account/password_change.html"


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = "account/password_change_done.html"


#  Reset forgotten password
class UserPasswordReset(PasswordResetView):
    template_name = 'account/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_done')
    email_template_name = 'account/password_reset_email.html'


class USerPasswordResetDone(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class UserPasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')


class UserPasswordResetComplete(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'






