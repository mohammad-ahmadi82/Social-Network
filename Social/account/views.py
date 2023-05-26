from django.shortcuts           import render, redirect
from django.views               import View
from .forms                     import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib             import messages
from django.contrib.auth        import  authenticate, login, logout

class UserRegisterView(View):
    form_class  = UserRegistrationForm
    template_name   = 'account/register.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            messages.success(request, 'User created successfully', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})

class UserLoginView(View):
    form_class  = UserLoginForm
    template_name   = 'account/login.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,  {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('home:home')
            messages.error(request, 'your username or password is wrong', 'warning')
        return render(request, self.template_name,  {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.error(request, 'you logged out', 'danger')
        return redirect('home:home')
