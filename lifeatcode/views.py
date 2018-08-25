from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from templated_email import send_templated_mail


class HomePageView(View):

    def get(self, request):
        return render(request, 'home.html')


class AboutMeView(View):

    def get(self, request):
        return render(request, 'about.html')


class PortfolioView(View):

    def get(self, request):
        return render(request, 'portfolio.html')


class PrivacyView(View):

    def get(self, request):
        return render(request, 'privacy.html')


class RefundView(View):

    def get(self, request):
        return render(request, 'refund.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        from_email = request.POST.get('email')
        sender_name = request.POST.get('name')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        send_templated_mail(
            template_name='contact',
            from_email=from_email,
            recipient_list=['vubon.roy@gmail.com'],
            context={
                'subject': subject,
                'name': sender_name,
                'message': message,
            },
        )

        return HttpResponseRedirect('/contacts/')


class OrderView(View):

    def get(self, request):
        return render(request, 'orders.html')
