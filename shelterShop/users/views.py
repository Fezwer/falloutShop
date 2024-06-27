from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomChangePasswordForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import CustomUser
from shop.models import Purchase
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import uuid
import json
from yookassa import Configuration, Payment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from decimal import Decimal # Это библиотека для расчетов используется, чтобы не возникало проблем с балансом

def profile(request):
    if request.user.is_authenticated:
        custom_user, created = CustomUser.objects.get_or_create(user=request.user)
        user_balance = custom_user.balance
        purchase_user = Purchase.objects.filter(user=request.user)
        return render(request, 'users/profile.html', {'username': request.user.username, 'balance': user_balance, 'purchase_user':purchase_user})
    else:
        return redirect('login')
    
def user_logout(request):
    logout(request)
    return redirect('profile')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Важно для предотвращения выхода из системы
            messages.success(request, 'Ваш пароль успешно изменен!')
            return redirect('profile')  # Замените 'profile' на имя вашего представления профиля
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибку ниже.')
    else:
        form = CustomChangePasswordForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@csrf_exempt
@require_POST
def payment_succed(request):
    data = json.loads(request.body)

    if data['type'] == 'notification' and data['event'] == 'payment.succeeded' and 'object' in data:
        payment_object = data['object']
        amount_value = payment_object['amount']['value']
        payment_description = payment_object.get('description', '')  # В описании содержится имя пользователя
        username = payment_description

        # Находим пользователя по имени и обновляем баланс
        try:
            user = CustomUser.objects.get(user__username=username)
            user.balance += Decimal(amount_value)
            user.save()
            return HttpResponse(status=200)

        except CustomUser.DoesNotExist:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)

@login_required
def user_payment(request):
    if request.method == 'POST':
        userAmount = request.POST.get('amount')
        Configuration.account_id = '399154'
        Configuration.secret_key = 'test_ZIsZSi43YeYLK8MdlTFIqTJEJgLgitpEPZWcF0lVgFo'
        idempotence_key = str(uuid.uuid4())

        payment = Payment.create({
            "amount": {
                "value": str(userAmount),
                "currency": "RUB" 
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://fezwer.ru/profile"
            },
            "capture": True,
            "description": str(request.user.username),
        }, idempotence_key)

        if payment:
            confirmation_url = payment.confirmation.confirmation_url
            return JsonResponse({'url': confirmation_url})  # Отправляем URL клиенту
        else:
            return JsonResponse({'error': 'Не удалось провести платеж'}, status=500)

    return JsonResponse({'error': 'Неизвестный метод request'}, status=405)