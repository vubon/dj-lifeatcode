from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden, HttpResponse

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegisterUserForm, LoginForm


class RegisterUserView(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "dashboard/users/register.html"
    success_url = '/users/signup'
    success_message = "Account has been created successfully"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()
        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super(RegisterUserView, self).form_valid(form)


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = "dashboard/users/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('admin_panel')
    success_message = "login success"


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)
