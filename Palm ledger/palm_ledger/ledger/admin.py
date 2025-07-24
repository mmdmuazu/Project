from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'quantity', 'user', 'created_at')
    search_fields = ('name', 'description')
