from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    elif request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        registration_form_validators = {
            'username_taken':
                {
                    'is_invalid': User.objects.filter(username=username).exists(),
                    'show_message': lambda: messages.add_message(request, messages.ERROR, 'Username not available')
                },
            'passwords_not_match':
                {
                    'is_invalid': password != password2,
                    'show_message': lambda: messages.add_message(request, messages.ERROR, 'Passwords do not match')
                },
            'email_taken':
                {
                    'is_invalid': User.objects.filter(email=email).exists(),
                    'show_message': lambda: messages.add_message(request, messages.ERROR, 'Email address already taken')
                }
        }

        registration_is_valid = True

        for key in registration_form_validators.keys():
            field = registration_form_validators[key]
            if field['is_invalid']:
                field['show_message']()
                registration_is_valid = False

        if not registration_is_valid:
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Registration successful')
            return redirect('login')

            #auth.login(request, user)
            #messages.add_message(request, messages.SUCCESS, 'You are not logged in')
            #return redirect('index')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # TODO: enable messages on Dashboard
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
            auth.logout(request)
            messages.success(request, 'You have been logged out')
            return redirect('index')
    else:
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')