from django.contrib import admin
from .models import User_reg, Transactions, Supports, Loan, BillPayment

# User Data Model
admin.site.register(User_reg)

# Transaction Data Model
admin.site.register(Transactions)

# Support Data Model
admin.site.register(Supports)

# Loan Data Model
admin.site.register(Loan)

# Bill Application Data Model
admin.site.register(BillPayment)