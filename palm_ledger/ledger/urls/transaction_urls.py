from django.urls import path
from ledger.views.transaction_view import TransactionView

urlpatterns = [
    path('transactions/', TransactionView.as_view(), name='transaction')
]
