from django.shortcuts import render,redirect,HttpResponse
from app.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import  csrf_exempt 
# Create your views here.

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, f'Your account has been created! You are now able to log in')
        
            return redirect('login-user')
    else:
        form = UserRegisterForm()

    return render(request,'app/register.html',{"form":form})


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create-events')
        else:
            messages.info(request, 'Try again! username or password is incorrect')

    context = {}
    return render(request, 'app/login.html', context)

    

# @login_required
def create_event(request):
    if request.method == 'POST':
        event_name = request.POST.get('events')
        event_date_time = request.POST.get('event-datetime')
        print(event_name,event_date_time,"---------49--")
        Events.objects.create(events_name=event_name,meeting_date_time=event_date_time)
        messages.success(request, f'User Events is created')
        return render(request, 'app/events.html')
    else:
        return render(request, 'app/events.html')
        
