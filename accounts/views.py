from django.shortcuts import redirect, render
from .forms import SignupForm , UserForm , ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    form = SignupForm()
    try:
        if request.method=="POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username,password=password)
                login(request,user)
                return redirect('accounts:profile')
        else:
            form = SignupForm()
    except Exception as e:
        print(f'Error : {e}')
    return render(request,'registration/signup.html',{'form':form})


def logged_out(request):
    return render(request, 'registration/logged_out.html', {'user': request.user})


def profile(request):
    profile = None
    try:
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
        else:
            return redirect('accounts:login')
            
    except Exception as e:
        print(f'Error : {e}')
    
    return render(request, 'accounts/profile.html', {'profile': profile , 'user': request.user})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    try:
        if request.method=='POST':
            userform = UserForm(request.POST,instance=request.user)
            profileform = ProfileForm(request.POST,request.FILES,instance=profile )
            if userform.is_valid() and profileform.is_valid():
                userform.save()
                myprofile = profileform.save(commit=False)
                myprofile.user = request.user
                myprofile.save()
                return redirect(reverse('accounts:profile'))
        else :
            userform = UserForm(instance=request.user)
            profileform = ProfileForm(instance=profile)
    except Exception as e:
        print(f'Error : {e}')
    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform })