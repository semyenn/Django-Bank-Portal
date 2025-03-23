from django.shortcuts import render, redirect
from bank.models import Loan, User_reg , Transactions , Supports, BillPayment
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import logout

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

# Create your views here.
@login_required()
@user_passes_test(is_manager)
def manager(request):
    loans = Loan.objects.all()
    users = User_reg.objects.all()
    transactions = Transactions.objects.all()
    supports = Supports.objects.all()
    billpayments = BillPayment.objects.all()
    total_loans = Loan.Loan_count(self=loans)
    total_transactions = transactions.count()
    context = {
        'loans':loans, 
        'users':users, 
        'transactions':transactions,
        'supports':supports,
        'billpayments':billpayments,
        'total_loans':total_loans,
        'total_transactions':total_transactions
        }
    return render(request,'manager.html',context)

def Logout(request):
    logout(request)
    messages.success(request,"You are now logged out")
    return redirect('login page')

def loan_approve(request, id):
    if request.method == 'POST':
        try:
            loan = Loan.objects.get(id=id)
            if loan.loan_status != 'PENDING':
                messages.error(request, 'Loan has already been processed.')
                return redirect('Manager')
            user = User_reg.objects.get(user=request.user)
            transactions = Transactions.objects.create(user=user,transaction_type='Loan',amount=loan.loan_amount,about=f'Loan for {loan.loan_type} approved',receiptent=loan.loan_amount,receiptent_no='Bank')
            user.balance += loan.loan_amount
            loan.loan_status = 'APPROVED'
            user.save()
            loan.save()
            return redirect('Manager')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return redirect('Manager')

def loan_reject(request, id):
    if request.method == 'POST':
        try:
            loan = Loan.objects.get(id=id)
            if loan.loan_status != 'PENDING':
                messages.error(request, 'Loan has already been processed.')
                return redirect('Manager')
            user = User_reg.objects.get(user=request.user)
            loan.loan_status = 'REJECTED'
            user.save()
            loan.save()
            return redirect('Manager')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return redirect('Manager')