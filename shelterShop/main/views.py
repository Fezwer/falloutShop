from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import UsersRecords
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def custom_404(request, exception):
    return render(request, 'main/404.html', status=404)

@csrf_exempt
def users_records(request):
    if request.method == 'GET':
        users_records = UsersRecords.objects.order_by('-record')
        data = [{"nickname": user.nickname, "record": user.record} for user in users_records]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        user = data.get('user')
        record = data.get('record')

        if UsersRecords.objects.filter(nickname=user).exists():
            existing_user = UsersRecords.objects.get(nickname=user)
            if record > existing_user.record:
                existing_user.record = record
                existing_user.save()
        else:
            if UsersRecords.objects.count() < 10:
                new_user = UsersRecords(nickname=user, record=record)
                new_user.save()
            else:
                min_record_user = UsersRecords.objects.order_by('record').first()
                if record > min_record_user.record:
                    min_record_user.delete()
                    new_user = UsersRecords(nickname=user, record=record)
                    new_user.save()

        return JsonResponse({"message": "Рекорд успешно добавлен."})