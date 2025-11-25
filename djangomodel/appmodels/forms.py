'''from django import forms
from .models import Emp_Details

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp_Details
        fields = '__all__' '''
from django import forms 
from .models import Emp_Details
class EmpForm(forms.ModelForm):
    class Meta :
        model = Emp_Details
        fields = '__all__' 