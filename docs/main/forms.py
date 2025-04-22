from django import forms
from .models import Class,Activity,School
class SchoolForm(forms.ModelForm):
    class Meta:
        model=School
        fields = ['school_name']
        labels = {'school_name': '学校名称'}
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_name']
        labels = {'class_name': '班级名称'}
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['start_time','end_time','activity_name','activity_description']
        labels = {'start_time': '活动开始时间','end_time':'活动结束时间','activity_name':'活动名称','activity_description':'活动描述'}
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }