'''
Created on 17.12.2018

@author: root
'''


from django import forms
from models import PRIORITY_CHOICES, List

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Titel", max_length=250, min_length=1)
    priority = forms.ChoiceField(label="Prio", choices=PRIORITY_CHOICES)
    todo_list = forms.ModelChoiceField(label="Liste", queryset=List.objects.all()) 
    estimation = forms.FloatField(label="Erforderliche Gesamtzeit")

class EditEntryForm(NewEntryForm):
    completed = forms.BooleanField(label="Fertig", required=False)
    remaining_estimation = forms.FloatField(label="Verbleibende Zeit")

class DeleteEntryForm(forms.Form):
    pass
