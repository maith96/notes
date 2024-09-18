from django.urls import path
from .views import TestSTK,stk_callback, TransactionCreateView, TransactionListView

urlpatterns = [
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('request_stk_push', TransactionCreateView.as_view(), name='transaction-create'),
    path('test_stk_push', TestSTK.as_view(), name='transaction-create'),
    path(route='stk_callback/',view=stk_callback , name='stk_callback'),
]
