from django import forms
from .models import task  # Import the task model from the same app (assuming "todoapp" is your app name)

class todoform(forms.ModelForm):  # Use "ModelForm" instead of "modelform" and "Meta" instead of "meta"
    class Meta:  # Use "Meta" with an uppercase 'M'
        model = task  # Use lowercase 'model' and 'task'
        fields = ['name', 'priority', 'date']  # Use lowercase field names
