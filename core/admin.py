from django.contrib import admin
from core.models import Transaction, CreditCard

class TransactionAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'status', 'transaction_type', 'recipient', 'sender']
    list_display = ['user', 'amount', 'status', 'transaction_type', 'recipient', 'sender']

class CreditCardAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'card_type']
    list_display = ['user', 'card_id', 'cvc', 'amount', 'card_type']

admin.site.register(Transaction, TransactionAdmin)

admin.site.register(CreditCard, CreditCardAdmin)
