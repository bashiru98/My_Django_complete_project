from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'user/registers.html', {'form': form})

# def register(request):
#     form= UserCreationForm(request, Post)
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, f'Username already exist')
#                 return redirect('registers')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, f'email already exist')
#                 return redirect('registers')
#             else:
#                 user = User.objects.create_user(
#                     username=username, email=email, password=password1)
#                 user.save()
#                 messages.success(request, f'your new account has been created')
#                 return redirect('blog-home')

#         else:
#             messages.info(request, f'password mismatch')
#             return redirect('registers')
#     else:
#         return render(request, 'user/registers.html')


@login_required
def profile(request):
    if request.method == 'POST':
        ur_form = UserUpdateForm(request.POST, instance=request.user)
        pr_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if ur_form.is_valid() and pr_form.is_valid():
            ur_form.save()
            pr_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('blog-home')
    else:
        ur_form = UserUpdateForm(instance=request.user)
        pr_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'ur_form': ur_form,
        'pr_form': pr_form
    }
    return render(request, 'user/profile.html', context)


def contactview(request):
    Fullname = ''
    email = ''
    comment = ''

    form = ContactForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        comment = form.cleaned_data.get("comment")

        if request.user.is_authenticated:
            subject = str(request.user) + "'s Comment"
        else:
            subject = "A Visitor's Comment"

        comment = name + " with the email, " + email + \
            ", sent the following message:\n\n" + comment
        send_mail(subject, comment, 'bukariatulebashiru@gmail.com', [email])
        messages.success(request, f'your comment has been sent successfully !')

        # context= {'form': form}

        return render(request, 'blog/home.html')

    else:
        context = {'form': form}
        return render(request, 'user/contact.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog-home')

        else:
            messages.info(request, f'Username Or password is incorrect')
            return redirect('login')

    context = {}
    return render(request, 'login', context)
