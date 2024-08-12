from django.db import models
from users.models import CustomUser
import random


# Create your models here.
class CodesFactor(models.Model):
    number = models.CharField(max_length=5)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        code_list = [x for x in range(10)]
        code_items = []
        for i in range(5):
            num = random.choice(code_list)
            code_items.append(num)

        code = "".join(str(code) for code in code_items)
        self.number =code
        super().save(*args,**kwargs)
