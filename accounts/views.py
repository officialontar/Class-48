import email
import re

from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.

def index(request):

    return render(request, 'accounts/index.html')



def register(request):

    if request.method == 'POST':
        # Handle form submission and user registration logic here
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        profile_image = request.FILES.get('profile_image')
        role = request.POST['role']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if not re.match(pattern, password):
            messages.error(request, "Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            return redirect('register')
        if User.objects.filter(username = user_name).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')
        
        if User.objects.filter(email = email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')
        
        if User.objects.filter(phone = phone).exists():
            messages.error(request, "Phone number already exists.")
            return redirect('register')
        
        user = User.objects.create_user(
            first_name=fname,
            last_name=lname,
            username=user_name,
            email=email,
            phone=phone,
            profile_image=profile_image,
            role=role,
            password=password
        )
        
        user.save()
        messages.success(request, "Registration successful. You can now login.")
        return redirect('login')

    return render(request, 'accounts/register.html')


# def login_view(request):

#     if request.method == 'POST':

#         user_input = request.POST.get('username_email_phone')
#         password = request.POST.get('password')

#         user_obj = None

#         # check username
#         if User.objects.filter(username=user_input).exists():
#             user_obj = User.objects.get(username=user_input)

#         # check email
#         elif User.objects.filter(email=user_input).exists():
#             user_obj = User.objects.get(email=user_input)

#         # check phone
#         elif User.objects.filter(phone=user_input).exists():
#             user_obj = User.objects.get(phone=user_input)

#         if user_obj:
#             user = authenticate(request, username=user_obj.username, password=password)

#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Login Successful")
#                 return redirect('profile')

#             else:
#                 messages.error(request, "Invalid Password")

#         else:
#             messages.error(request, "User not found")

#     return render(request, 'accounts/login.html')




def login_view(request):

    if request.method == 'POST':

        # এখানে form থেকে username / email / phone যেটা user লিখবে সেটা নেওয়া হচ্ছে
        user_input = request.POST.get('username_email_phone')

        # এখানে password নেওয়া হচ্ছে
        password = request.POST.get('password')

        try:

            # এখানে database এ user খোঁজা হচ্ছে
            user_obj = User.objects.get(

                Q(username=user_input) |   # এখানে USERNAME check করবে

                Q(email=user_input) |      # এখানে EMAIL check করবে

                Q(phone=user_input)        # এখানে PHONE NUMBER check করবে

            )

            # এখানে authenticate করা হচ্ছে (login verify)
            user = authenticate(
                request,
                username=user_obj.username,  # authenticate সবসময় username দিয়ে হয়
                password=password
            )

            if user is not None:

                # login সফল হলে user session start হবে
                login(request, user)

                # success message
                messages.success(request, "Login Successful")

                # login হলে profile page এ redirect
                return redirect('profile')

            else:

                # password ভুল হলে এই message
                messages.error(request, "Invalid password")

        except User.DoesNotExist:

            # username / email / phone কোনটাই না মিললে এই message
            messages.error(request, "User not found")

    # GET request হলে login page show করবে
    return render(request, 'accounts/login.html')





def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


@login_required
def profile_page(request):
    
    return render(request, 'accounts/profile_page.html')