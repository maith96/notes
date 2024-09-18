from urllib import response
from django.shortcuts import render, HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.serialzers import NoteSerializer
from api.models import Note
from .models import Transaction
from .serializers import TransactionSerializer
import requests
from requests.auth import HTTPBasicAuth

items_amount = {'national_id': 100, 'school_id': 100}

class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def requst_stk_push(self, phone_number, amount):
        mpesa_endpoint = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate'
        access_token = get_access_token()  
        headers = { 'Authorization': f'Bearer {access_token}' }
        body = {
            'ShortCode': 174379,  
            'CommandID': "CustomerPayBillOnline",
            'BillRefNumber': 'TestPay1',
            'Msisdn': phone_number,
            'Amount': amount
        }

        # response = requests.post(mpesa_endpoint, json=body, headers=headers)
        import mpesa
        c2b = mpesa.api.c2b.C2B()
        
        return response.json()

    def perform_create(self, serializer):
        phone_number = serializer.validated_data['phone_number']
        amount = serializer.validated_data['amount']
        
        # Simulate the payment process
        payment_response = self.requst_stk_push(phone_number, amount)
        print(payment_response)
        # Check if payment was successful
        if payment_response.get('ResponseCode') == '0':  # Assuming '0' is success code
            serializer.save(initiated_by=self.request.user)
        else:
            return Response({'error': 'Payment failed'}, status=status.HTTP_400_BAD_REQUEST)

class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(initiated_by=self.request.user)

def get_access_token():
    import mpesa
    mpesa.api.auth.MpesaBase.authenticate(env='sandbox', app_key ='', app_secret='', sandbox_url='https://sandbox.safaricom.co.ke', live_url='https://api.safaricom.co.ke')
    return get_access_token()

class TestSTK(generics.ListAPIView):
    # queryset = Transaction.objects.all()
    
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        import mpesa
        from mpesa.api.mpesa_express import MpesaExpress
        express = MpesaExpress(app_key='KCWHKhtGepVflCODS1BU2PIzFCoFSh7qhdNvp5VHFsyI26PP', app_secret='ogFLt2E4rvjV4AwnBm3PkNWfGJo7K1OnAzEBZk3yclPc7v52jhE8RRynlu95Oi99')
        res = express.stk_push(business_shortcode="174379",
                         reference_code="CustomerPayBillOnline",
                         passcode="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919", 
                         phone_number='254748075877', 
                         amount=1, 
                         callback_url='https://508c-197-136-134-5.ngrok-free.app/api/transactions/stk_callback',
                         description="Test Payment",
                         )
        print(res)
        return Note.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

def stk_callback(request):
    # print(request)
    return HTTPResponse('Hello')