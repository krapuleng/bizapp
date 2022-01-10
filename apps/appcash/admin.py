from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import cashapp_CashTransaction, cashapp_TransactionType , transactionAccount , cashapp_closecash


class CashTransactionAdmin(admin.ModelAdmin):
    fields =( "amount", ("transactionAccount", "transactiontype"),"description",'user')
    list_display =("transactionAccount", "transactiontype", "amount" ,"description")
    readonly_fields = ('user',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class transactionAccountAdmin(admin.ModelAdmin):
    readonly_fields = ('Balance',)
site_url = None
admin.site.register(cashapp_CashTransaction, CashTransactionAdmin)
admin.site.register(cashapp_closecash)
admin.site.register(cashapp_TransactionType)
admin.site.register(transactionAccount, transactionAccountAdmin)


