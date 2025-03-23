from django.urls import path
from . import views

urlpatterns = [
    path('',views.manager,name='Manager'),
    path('loan_approve/<int:id>/',views.loan_approve,name='loan_approve'),
    path('loan_reject/<int:id>/',views.loan_reject,name='loan_reject'),
    path('logout/',views.Logout,name='logout'),
    ]