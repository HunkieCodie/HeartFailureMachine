from .models import Patient
from django import forms


class PatientModelForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'first_name',
            'last_name',
            'age',
            'anaemia',
            'ejection_fraction',
            'creatinine_phosphokinase',
            'diabetes',
            'high_blood_pressure',
            'platelets',
            'serum_creatinine',
            'serum_sodium',
            'sex',
            'smoking',
            'time',
        )
