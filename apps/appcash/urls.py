from django.urls import path
from apps.appcash.views import IndexView,TransanctionView, TransanctionDetailView,TransanctionAddView,TransanctionCloseCashView 

urlpatterns = [
    path('', IndexView.as_view(), name='appcash_index'),
    path('transactions/', TransanctionView.as_view(), name='transactions'),
    #path('transaction/<int:pk>', views.TransanctionDetailView.as_view(), name='transaction-detail'),
    path('transactionadd/', TransanctionAddView.as_view(), name='transaction-add'),
    path('closecash/', TransanctionCloseCashView.as_view(), name='transaction-closecash'),
]