from decimal import Decimal
from django.shortcuts import render
from django.http import JsonResponse
from .models import Account, Transaction
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def deposit(request):
    if request.method == 'POST':
        iban = request.POST.get('iban')
        amount = Decimal(request.POST.get('amount')) 
        try:
            account = Account.objects.get(iban=iban)
            account.balance += amount
            account.save()
            Transaction.objects.create(
                account=account,
                transaction_type='DEPOSIT',
                amount=amount,
                balance_after=account.balance
            )
            return JsonResponse({'status': 'success', 'message': f'Deposited {amount} into account {iban}.'})
        except Account.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Account not found.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

@csrf_exempt
def withdraw(request):
    if request.method == 'POST':
        iban = request.POST.get('iban')
        amount = Decimal(request.POST.get('amount'))  
        try:
            account = Account.objects.get(iban=iban)
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                Transaction.objects.create(
                    account=account,
                    transaction_type='WITHDRAWAL',
                    amount=amount,
                    balance_after=account.balance
                )
                return JsonResponse({'status': 'success', 'message': f'Withdrew {amount} from account {iban}.'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Insufficient funds.'})
        except Account.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Account not found.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

@csrf_exempt
def transfer(request):
    if request.method == 'POST':
        from_iban = request.POST.get('from_iban')
        to_iban = request.POST.get('to_iban')
        amount = Decimal(request.POST.get('amount')) 
        try:
            from_account = Account.objects.get(iban=from_iban)
            to_account = Account.objects.get(iban=to_iban)
            if from_account.balance >= amount:
                from_account.balance -= amount
                to_account.balance += amount
                from_account.save()
                to_account.save()
                Transaction.objects.create(
                    account=from_account,
                    transaction_type='TRANSFER',
                    amount=-amount,
                    balance_after=from_account.balance
                )
                Transaction.objects.create(
                    account=to_account,
                    transaction_type='TRANSFER',
                    amount=amount,
                    balance_after=to_account.balance
                )
                return JsonResponse({'status': 'success', 'message': f'Transferred {amount} from account {from_iban} to account {to_iban}.'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Insufficient funds.'})
        except Account.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Account not found.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Account, Transaction

@login_required
def statement(request):
    user = request.user
    if user.is_staff:  
        transactions = Transaction.objects.all().order_by('-date')
    else:
        iban = request.GET.get('iban')
        try:
            account = Account.objects.get(iban=iban)
            transactions = Transaction.objects.filter(account=account).order_by('-date')
        except Account.DoesNotExist:
            return JsonResponse({'transactions': [], 'message': 'Account not found.'})

    transactions_list = [
        {
            'date': str(tx.date),
            'transaction_type': tx.transaction_type,
            'amount': str(tx.amount),
            'balance': str(tx.balance_after)
        }
        for tx in transactions
    ]
    return JsonResponse({'transactions': transactions_list})
