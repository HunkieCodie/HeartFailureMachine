"""HeartFailureApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from patients.views import (LandingPageView, PatientDeleteView, PatientCreateView, PatientUpdateView,
                            PatientDetailView, PatientListView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="home"),
    path('<int:pk>/delete/', PatientDeleteView.as_view(), name="delete"),
    path('create/', PatientCreateView.as_view(), name="create"),
    path('patients/', PatientListView.as_view(), name="patient-list"),
    path('<int:pk>/update/', PatientUpdateView.as_view(), name="update"),
    path('list/<int:pk>/', PatientDetailView.as_view(), name="detail"),
]
