from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import uuid



operation = [
    ('add', '1'),
    ('subtract', '-1'),
]


class cashapp_TransactionType(models.Model):  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    operation = models.IntegerField(null=True, blank='true')
    
    def __str__(self):
        return str(self.name)
    class Meta:
        managed = True
        db_table = 'cashapp_TransactionType'
        verbose_name = 'Transaction type'
        verbose_name_plural = 'Transaction Types'


class transactionAccount(models.Model):  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255)  # Field name made lowercase.
    Balance = models.FloatField(null=True, blank='true', default="0.00")

    def __str__(self):
        return str(self.name)
    class Meta:
        managed = True
        db_table = 'transactionAccount'
        verbose_name = 'Transaction Account'
        verbose_name_plural = 'Transaction Accounts'


class cashapp_CashTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    transactiontype = models.ForeignKey(cashapp_TransactionType, on_delete=models.CASCADE)
    transactionAccount = models.ForeignKey(transactionAccount, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    amount = models.FloatField(null=False)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return str(self.transactiontype) +"  "+ str(self.description) +"  "+ str(self.amount)

    class Meta:
        managed = True
        order_with_respect_to = 'amount'
        db_table = 'cashapp_CashTransaction'
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'


class cashapp_closecash(models.Model):
    accept_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    transaction = models.ForeignKey(cashapp_CashTransaction, on_delete=models.CASCADE)
    balance = models.FloatField(null=False)
    status = models.BooleanField(default=False)
    datecaptured = models.DateTimeField(auto_now_add=True)


    def __str__(self):
         return str(self.submit_user) +"  "+ str(self.datecaptured) +"  "+ str(self.balance)

    class Meta:
        managed = True
        order_with_respect_to = 'datecaptured'
        db_table = 'cashapp_closecash'
        verbose_name = 'close Cash'
        verbose_name_plural = 'close cash'