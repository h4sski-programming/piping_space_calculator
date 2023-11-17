from django.shortcuts import render
from django.http import HttpResponse

from .forms import MyForm, PipeSpaceCalculatorForm
from .calculations import calculate_pipe_space
from .pipe_db import flange_dimensions_pn10, flange_dimensions_pn16, flange_dimensions_pn25, flange_dimensions_pn40
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

    return render(request, 'aaa.html', context)


