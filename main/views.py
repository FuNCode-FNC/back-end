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

