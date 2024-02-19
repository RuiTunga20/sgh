"""veltrix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from .views import MyPasswordChangeView, MyPasswordSetView
from django.conf.urls.static import static
from django.conf import settings
from veltrix import views
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    # Dashboards View
    path('', views.DashboardView.as_view(), name='dashboard'),
    # calender
    path('calendar', views.CalendarView.as_view(), name='calendar'),
    # Email
    path("email/", include("e_mail.urls")),
    # Components
    path("components/", include("components.urls")),
    # Extra_Pages
    path("Gestao/", include("gestao.urls")),
    path("Desempenho/", include("Desempenho.url")),

    # Extra_Pages
    path("email_templates/", include("email_templates.urls")),
    # layouts
    path("layouts/", include("layouts.urls")),  
    # Authentication
    path("authentication/", include("authentication.urls")),  
    
    path(
        "account/password/change/",
        login_required(MyPasswordChangeView.as_view()),name="account_change_password",),
    path(
        "account/password/set/",
        login_required(MyPasswordSetView.as_view()),name="account_set_password",),
    
    # auth-allath
    path('account/', include('allauth.urls')),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
