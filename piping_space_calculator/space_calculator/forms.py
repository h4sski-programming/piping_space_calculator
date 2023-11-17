# forms.py
from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class PipeSpaceCalculatorForm(forms.Form):
    pipe_dn_list = [10, 15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300, 350, 400]
    flange_pn_list = ['NONE', 'PN10', 'PN16', 'PN25', 'PN40']
    dn_1 = forms.ChoiceField(choices=[(dn, dn) for dn in pipe_dn_list])
    dn_2 = forms.ChoiceField(choices=[(dn, dn) for dn in pipe_dn_list])
    flange = forms.ChoiceField(choices=[(pn, pn) for pn in flange_pn_list])
    min_gap = forms.IntegerField(max_value=200, min_value=0, step_size=10)
