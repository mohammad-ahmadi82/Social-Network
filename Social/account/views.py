from django.shortcuts           import render, redirect, get_object_or_404
from django.views               import View
from .forms                     import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib             import messages
from django.contrib.auth        import  authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models                import Post
from django.contrib.auth        import views as auth_views
from django.urls                import reverse_lazy

class UserRegisterView(View):
    form_class  = UserRegistrationForm
    template_name   = 'account/register.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)
    

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


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.error(request, 'you logged out', 'danger')
        return redirect('home:home')


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        posts   = Post.objects.filter(user=user)
        return render(request, 'account/profile.html', {'user':user, 'posts':posts})


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name       = 'account/password_reset_form.html'
    success_url         =  reverse_lazy('account:password_reset_done')
    email_template_name = 'account:password_reset_email.html' 