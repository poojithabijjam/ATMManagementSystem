from django.db import models
from django.contrib.auth.models import User


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


# Create your models here
class carddet(models.Model):
    cardnum = models.CharField(max_length=128, null=False)
    pin = models.CharField(max_length=256, null=False)
    balance = models.CharField(max_length=16, default=0)

    def __str__(self):
        return self.cardnum

    def transact(self):
        return '/transact/' + self.cardnum

    def seltype(self):
        return '/seltype/'+self.cardnum

    def deposit(self):
        return '/deposit/'+self.cardnum

    def withdraw(self):
        return '/withdraw/'+self.cardnum

    def enquire(self):
        return '/enquire/'+self.cardnum

class MiniStat(models.Model):


    t1 = models.ForeignKey(carddet.balance)

#     t1 = models.CharField(max_length=16, default=0) 
#     t1 = models.CharField(max_length=16, default=0)
#     balance = models.CharField(max_length=16, default=0)
#     balance = models.CharField(max_length=16, default=0)
#     balance = models.CharField(max_length=16, default=0)
#     balance = models.CharField(max_length=16, default=0)


