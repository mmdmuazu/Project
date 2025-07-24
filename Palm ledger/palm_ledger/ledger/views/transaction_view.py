from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from ledger.serializers.transaction_serializer import TransactionSerializer
from ledger.services.transaction_service import create_transaction, list_user_transactions

class TransactionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = list_user_transactions(request.user)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction = create_transaction(request.user, serializer.validated_data)
            return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
