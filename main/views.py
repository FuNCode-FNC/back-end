
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import Customer
import json
from django.views.decorators.http import require_http_methods
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import send_mail,EmailMessage

from django.contrib.auth.decorators import login_required
from datetime import datetime,timedelta
import pytz

utc=pytz.UTC
expiration_time = 1

def  index(request):
    return render(request,'login.html')

@login_required()
def profile(request):
    return  render(request,"profile.html")

@require_http_methods(['POST'])
def logIn(request):
    data = json.loads(request.body)
    user = authenticate(username=data['email'], password=data['password'])
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse('Authenticated successfully')
        else:
            return HttpResponse('Disabled account')
    else:
        return HttpResponse('Invalid login')

    return HttpResponse(200)



@require_http_methods(['POST'])
def signUp(request):
    data = json.loads(request.body)
    print(data)
    user =Customer.objects.create_user(email=data['email'],password=data['password'],username = data['username'])
    user.is_active = False
    table_expire_datetime = datetime.now() + timedelta(minutes=expiration_time)
    expired_on = table_expire_datetime.replace(tzinfo=utc)
    user.verif_time = expired_on
    user.save()
    current_site = get_current_site(request)
    mail_subject = 'Activation link has been sent to your email id'
    message = render_to_string('acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
    })

    send_mail(
        mail_subject,
        message,
        'trofimov.vlad-1234@yandex.ru',
        [data['email']],
        fail_silently=False,
    )

    return HttpResponse(200)
    
    
def logOut(request):
    logout(request)
    return HttpResponse(200)
    
    
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        if datetime.now().replace(tzinfo=utc) > user.verif_time:
            user.verif_time = None
            return HttpResponse('Activation link has expired!')

        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def main_page(request):
    return render(request, 'main/main_page.html')


def account(request):
    return render(request, 'main/account.html')


def filmpage(request):
    return render(request, 'main/filmpage.html')


def list_of_films(request):
    return render(request, "main/List of films from user's account.html")


def recovery_new_password(request):
    return render(request, "main/recovery-new-password.html")


def change_new_password(request):
    return render(request, "main/change-new-password.html")


def sign_up_page(request):
    return render(request, "main/sign-up-page.html")


def films_genres(request):
    return render(request, 'main/Films sorted by genre.html')


def moderator(request):
    return render(request, 'main/moderator account.html')


def recovery_page(request):
    return render(request, 'main/recovery-page.html')


def sign_in_page(request):
    return render(request, 'main/sign-in-page.html')


def sign_up_email(request):
    return render(request, 'main/sign-up-email.html')

