from django import forms
from .models import DjangoModelForm
from django import forms
from django.forms.widgets import NumberInput
import datetime

class ModelForm(forms.ModelForm):
    class Meta:
        model = DjangoModelForm
        fields = '__all__'

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class PracticeDjangoForm(forms.Form):
	first_name = forms.CharField(initial='Your name')
	email = forms.EmailField()
	email_address = forms.EmailField( 
    required = False,
)
	email_address = forms.EmailField( 
    label="Please enter your email address",
)
	value = forms.DecimalField()
	date = forms.DateField()
	day = forms.DateField(initial=datetime.date.today)
	birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
	birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	
	agree = forms.BooleanField()
	agree = forms.BooleanField(initial=True)
	favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
	favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
	favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
	message = forms.CharField(
	max_length = 10,
)
	comment = forms.CharField(widget=forms.Textarea)

