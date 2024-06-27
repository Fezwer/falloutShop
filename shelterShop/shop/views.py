from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum
import json
from .models import UserCart, Shelters, Reservation, Purchase
from users.models import CustomUser

def storage(request):
    dataShelters = Shelters.objects.all()
    dataSheltersJS = json.dumps(list(dataShelters.values()))  

    # Получаем данные о количестве уже занятых мест для каждого убежища
    occupied_counts = {}
    for shelter in dataShelters:
        occupied_count = Purchase.objects.filter(shelter=shelter).aggregate(total=Sum('quantity'))['total'] or 0
        occupied_counts[shelter.id] = occupied_count
    
    occupied_counts = json.dumps(list(occupied_counts.values()))

    if request.method == 'POST':  
        json_data = json.loads(request.body)
        shelter_id = json_data.get('shelter_id')

        user = request.user
        user_cart, created = UserCart.objects.get_or_create(user=user)

        shelter_instance = Shelters.objects.get(id=shelter_id)

        existing_reservation = Reservation.objects.filter(user_cart=user_cart, shelter=shelter_instance).first()
        if existing_reservation:
            existing_reservation.quantity += 1
            existing_reservation.save()
            return JsonResponse({'message': 'Количество убежища в корзине было обновлено.'})
        else:
            reservation = Reservation.objects.create(user_cart=user_cart, shelter=shelter_instance, quantity=1)
            return JsonResponse({'message': 'Убежище было добавлено в корзину.'})

    return render(request, 'shop/storage.html', {'dataShelters': dataShelters, 'dataSheltersJS': dataSheltersJS, 'occupied_counts': occupied_counts})
    
@login_required
def cart(request):
    user_reservations = Reservation.objects.filter(user_cart__user=request.user)
    data_reservations_js = json.dumps(list(user_reservations.values()))
    total_cost = sum(reservation.shelter.price * reservation.quantity for reservation in user_reservations)
    occupied_counts = {}

    if request.method == 'POST':
        user = request.user
        custom_user = get_object_or_404(CustomUser, user=user)
        dataShelters = Shelters.objects.all()
        
        for shelter in dataShelters:
            occupied_count = Purchase.objects.filter(shelter=shelter).aggregate(total=Sum('quantity'))['total'] or 0
            occupied_counts[shelter.id] = occupied_count
        
        if not user_reservations.exists():
            return JsonResponse({'message': 'Ваша корзина пуста.'})
        
        successful_purchases = []
        failed_purchases = []

        for reservation in user_reservations:
            shelter_instance = reservation.shelter
            shelter_price = shelter_instance.price * reservation.quantity

            if reservation.quantity > (shelter_instance.available_quantity - occupied_counts.get(shelter_instance.id, 0)):
                failed_purchases.append(f"Убежище {shelter_instance.name}: Недостаточно свободных мест")
            else:
                if custom_user.balance >= shelter_price:
                    custom_user.balance -= shelter_price
                    custom_user.save()
                    existing_purchase = Purchase.objects.filter(user=user, shelter=shelter_instance).first()
                    
                    if existing_purchase:
                        existing_purchase.quantity += reservation.quantity
                        existing_purchase.save()
                        successful_purchases.append(f"{shelter_instance.name} - количество увеличено на {reservation.quantity}")
                    else:
                        Purchase.objects.create(user=user, shelter=shelter_instance, quantity=reservation.quantity)
                        successful_purchases.append(f"{shelter_instance.name} - количество: {reservation.quantity}")
                    
                    reservation.delete()
                else:
                    failed_purchases.append(f"Убежище {shelter_instance.name}: Недостаточно средств")

        if failed_purchases:
            message = f"Произошла ошибка при покупке: {', '.join(failed_purchases)}"
        else:
            message = f"Покупка успешно совершена для: {', '.join(successful_purchases)}."

        return JsonResponse({'message': message})

    return render(request, 'shop/cart.html', {'user_reservations': user_reservations, 'dataReservationsJS': data_reservations_js, 'total_cost': total_cost})

@login_required
def delete_reservation(request, reservation_id):
    user = request.user
    try:
        reservation = Reservation.objects.get(id=reservation_id, user_cart__user=user)
        reservation.delete()
        return JsonResponse({'message': 'Резерв успешно удален.'})
    except Reservation.DoesNotExist:
        return JsonResponse({'message': 'Резерв не найден или не принадлежит вам.'})