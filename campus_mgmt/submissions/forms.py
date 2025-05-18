from django import forms
from .models import Submission, Assignment  # Make sure Assignment is imported
import os

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['assignment', 'file']
        widgets = {
            'assignment': forms.Select(attrs={'class': 'form-select'}),
        }
        
    def clean_file(self):
        uploaded_file = self.cleaned_data.get('file')
        if uploaded_file:
            ext = os.path.splitext(uploaded_file.name)[1].lower()
            if ext not in ['.pdf', '.docx', '.py', '.txt']:
                raise forms.ValidationError("Only PDF, DOCX, PY, or TXT files allowed.")
        return uploaded_file

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['course', 'title', 'description', 'due_date']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }