from django.views.generic import TemplateView, CreateView
from django.views import generic
from .models import cashapp_CashTransaction
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "appcash/cashapp_base.html"


class TransanctionView(generic.ListView):
    paginate_by = 15
    model = cashapp_CashTransaction
    context_object_name = 'transactions_object'
    template_name = 'appcash/transactions.html'

class TransanctionDetailView(generic.DetailView):
    model = cashapp_CashTransaction


class TransanctionAddView(CreateView):
    model = cashapp_CashTransaction 
    fields = ['transactionAccount','transactiontype','amount']
    template_name = "appcash/transactionadd.html"
    success_url = reverse_lazy('transactions')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class TransanctionCloseCashView(TemplateView):
    model = cashapp_CashTransaction 
    template_name = "appcash/closecash.html"

        