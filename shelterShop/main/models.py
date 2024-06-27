from django.db import models

# Create your models here.
class UsersRecords(models.Model):
    nickname = models.CharField(max_length=20)
    record = models.IntegerField()

    class Meta:
        verbose_name = 'Рекорд'
        verbose_name_plural = 'Рекорды'

    def __str__(self):
        return f"{self.nickname} (Рекорд: {self.records})"
