from django.db import models
from django.contrib.auth.models import User

class Shelters(models.Model):
    name = models.CharField('Название', max_length=50, default='Согласование...')
    imgPath = models.ImageField('Изображение', upload_to='imgShelters')
    shortDescription = models.TextField('Краткое описание', max_length=100, default='Описание пока отсутствует, обратитесь к администратору с этой проблемой.')
    description = models.TextField('Описание', default='Описание пока отсутствует, обратитесь к администратору с этой проблемой.')
    price = models.PositiveIntegerField('Цена', default=999999999)
    available_quantity = models.PositiveIntegerField('Свободные места', default=0)

    class Meta:
        verbose_name = 'Убежищe'
        verbose_name_plural = 'Убежища'
    
    def __str__(self):
        return f"{self.name} (Цена: {self.price})"

class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shelters = models.ManyToManyField(Shelters, through='Reservation')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"{self.user}"

class Reservation(models.Model):
    user_cart = models.ForeignKey(UserCart, on_delete=models.CASCADE)
    shelter = models.ForeignKey(Shelters, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return f"{self.user_cart.user} (Кол-во: {self.quantity})"

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shelter = models.ForeignKey(Shelters, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return f"{self.user} (Кол-во: {self.quantity})"