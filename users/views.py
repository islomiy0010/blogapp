from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


from .forms import SignUpForm
def signup(request):
    if request.method=='POST':
        forms=SignUpForm(request.POST)
        print(forms)
        if forms.is_valid():
            forms.save()
            return redirect('users-login')
    else:
        forms = SignUpForm()
    context={
        'forms':forms
    }
    return render(request,'users/signup.html',context)
@login_required
def profile(request):
    return render(request,'users/profile.html')

from django.core.mail import EmailMessage
def send_email(request):
        em = EmailMessage('subject', 'This is test msg', to=['islomiy1101@gmail.com'])
        em.send()
        return HttpResponse('JONADI')

