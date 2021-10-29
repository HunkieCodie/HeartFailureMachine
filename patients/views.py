from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from .models import Patient
from .forms import PatientModelForm
from .utils import convert_boolean


# Create your views here.
class LandingPageView(TemplateView):
    template_name = "home.html"


class PatientListView(ListView):
    template_name = "patient_list.html"
    queryset = Patient.objects.all()
    context_object_name = "patients"


class PatientDetailView(DetailView):
    template_name = "patient_detail.html"
    queryset = Patient.objects.all()


class PatientCreateView(CreateView):
    template_name = "patient_create.html"
    form_class = PatientModelForm

    def get_success_url(self):
        return reverse("patient-list")


class PatientUpdateView(UpdateView):
    template_name = "patient_update.html"
    queryset = Patient.objects.all()
    form_class = PatientModelForm

    def get_success_url(self):
        return reverse("patient-list")


class PatientDeleteView(DeleteView):
    template_name = "patient_delete.html"
    queryset = Patient.objects.all()
    context_object_name = 'patient'

    def get_success_url(self):
        return reverse("patient-list")
