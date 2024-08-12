from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from users.models import CustomUser
from codes.forms import CodeFactorForms
from codes.models import CodesFactor


# Create your views here.
def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('verify-account')
    return render(request, 'login.html', {'form': form})


def verify_account(request):
    form = CodeFactorForms(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = CustomUser.objects.get(pk=pk)
        if request.method == 'POST' and form.is_valid():
            code_input = form.cleaned_data['number']
            code = CodesFactor.objects.get(user=pk)
            if str(code_input) == str(code.number):
                login(request, user)
                return redirect('success-factor')
        return render(request, 'verify.html', {'form': form})


@login_required()
def login_success(request):
    return render(request,'success.html')

