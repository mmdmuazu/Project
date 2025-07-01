from ledger.models import Transaction

def create_transaction(user, data):
    return Transaction.objects.create(user=user, **data)

def list_user_transactions(user):
    return Transaction.objects.filter(user=user).order_by('-created_at')
