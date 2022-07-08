from django.shortcuts import render


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


