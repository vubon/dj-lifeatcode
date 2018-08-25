"""lifeatcode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from lifeatcode.views import HomePageView, AboutMeView, PortfolioView, PrivacyView, RefundView, ContactView, OrderView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^about/', AboutMeView.as_view(), name='about'),
    url(r'^portfolio/', PortfolioView.as_view(), name='portfolio'),
    url(r'^privacy/', PrivacyView.as_view(), name='privacy'),
    url(r'^refund/', RefundView.as_view(), name='refund'),
    url(r'^contacts/', ContactView.as_view(), name='contacts'),
    url(r'^orders/', OrderView.as_view(), name='orders'),
]
