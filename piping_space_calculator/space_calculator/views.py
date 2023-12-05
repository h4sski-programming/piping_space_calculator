import math

from django.shortcuts import render
from django.http import HttpResponse

from .forms import MyForm, PipeSpaceCalculatorForm
from .calculations import calculate_pipe_space
from .pipe_db import pipe_dimensions, flange_dimensions
# Create your views here.


def index(request):
    context = {
        'template': 'index.html'
    }
    return render(request, 'index.html', context)


def hello(request):
    return HttpResponse("Hello, world. Hello.")


def aaa(request):
    context = {
        'pipe_space': '',
        'flange': 'NONE',
    }
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            context['name'] = form.cleaned_data['name']
            context['message'] = form.cleaned_data['message']

        pipe_space_calculator_form = PipeSpaceCalculatorForm(request.POST)
        if pipe_space_calculator_form.is_valid():
            context['dn_1'] = pipe_space_calculator_form.cleaned_data['dn_1']
            context['dn_2'] = pipe_space_calculator_form.cleaned_data['dn_2']
            context['flange'] = pipe_space_calculator_form.cleaned_data['flange']
            context['min_gap'] = pipe_space_calculator_form.cleaned_data['min_gap']


            # context['pipe_space'] = 123
            context['pipe_space'] = calculate_pipe_space(context['dn_1'], context['dn_2'], context['flange'], context['min_gap'])

    else:
        form = MyForm()
        pipe_space_calculator_form = PipeSpaceCalculatorForm()

    context['form'] = form
    context['pipe_space_calculator_form'] = pipe_space_calculator_form
    context['pipe_dimensions'] = pipe_dimensions
    print(f'{pipe_dimensions.keys}')
    context['flange_dimensions'] = flange_dimensions[context['flange']]

    return render(request, 'aaa.html', context)


def bbb(request):
    context = {
        'pipe_space': '',
        'flange': 'NONE',
    }
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            context['name'] = form.cleaned_data['name']
            context['message'] = form.cleaned_data['message']

        pipe_space_calculator_form = PipeSpaceCalculatorForm(request.POST)
        if pipe_space_calculator_form.is_valid():
            context['dn_1'] = pipe_space_calculator_form.cleaned_data['dn_1']
            context['dn_2'] = pipe_space_calculator_form.cleaned_data['dn_2']
            context['flange'] = pipe_space_calculator_form.cleaned_data['flange']
            context['min_gap'] = pipe_space_calculator_form.cleaned_data['min_gap']


            # context['pipe_space'] = 123
            context['pipe_space'] = calculate_pipe_space(context['dn_1'], context['dn_2'], context['flange'], context['min_gap'])

    else:
        form = MyForm()
        pipe_space_calculator_form = PipeSpaceCalculatorForm()

    def calculate_spacing(dn_flange=10, dn_pipe=10, gap_value=50, pn='PN10'):
        flange_od = flange_dimensions[pn][f'{dn_flange}']['OD']
        pipe_od = pipe_dimensions[f'{dn_pipe}']['OD']
        return math.ceil((flange_od/2 + pipe_od/2 + gap_value) / 10) * 10
    
    def get_row(dn_flange=10, gap_value=50):
        # lll = []
        # for dn in pipe_dimensions.keys():
        #     lll.append(calculate_spacing(dn_flange, int(dn), gap_value))
        return list(calculate_spacing(dn_flange, int(dn), gap_value) for dn in pipe_dimensions.keys())
    
    # print(get_row(20))
    
        
    context['variablee'] = {}
    for dn in list(int(d) for d in pipe_dimensions.keys()):
        context['variablee'][f'{dn}'] = get_row(dn)
    
    context['form'] = form
    context['pipe_space_calculator_form'] = pipe_space_calculator_form
    context['pipe_dimensions'] = pipe_dimensions
    print(f'{pipe_dimensions.keys}')
    context['flange_dimensions'] = flange_dimensions[context['flange']]

    return render(request, 'bbb.html', context)


