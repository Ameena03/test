from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import fields
from users.models import Category,Project,Profile
from django.core.validators import RegexValidator


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Full_name',)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    last_name = forms.CharField(label='Phone',validators=[phone_regex], max_length=10)

    class Meta:
        model = User
        fields = ['username', 'first_name','email','last_name','password1', 'password2']


class categoryForm(forms.ModelForm):
    name = forms.CharField(label='Category Label',widget=forms.Textarea(attrs={'rows':2}))

    class Meta:
        model = Category
        fields = ('name',)

YEAR_CHOICES = [
    ('2550', '2550'),
    ('2551', '2551'),
    ('2552', '2552'),
    ('2553', '2553'),
    ('2554', '2554'),
    ('2555', '2555'),
    ('2556', '2556'),
    ('2557', '2557'),
    ('2558', '2558'),
    ('2559', '2559'),
    ('2560', '2560'),
    ('2561', '2561'),
    ('2562', '2562'),
    ('2563', '2563'),
    ('2564', '2564'),
]

class ProjectForm(forms.ModelForm):
    p_name = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Add a Catchy Title','rows':1}))
    p_abstract = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Start writing your post here.','rows':8}))
    p_type = forms.ModelChoiceField(label='Categories',queryset=Category.objects.all(), required=False)
    p_date = forms.ChoiceField(
        label= 'year',
        choices = YEAR_CHOICES,
        )
    f_pdf = forms.FileField(label='Add a file')

    class Meta:
        model = Project
        fields = ('p_name','p_abstract', 'p_type','p_date', 'p_img','f_pdf')