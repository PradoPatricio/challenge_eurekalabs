from market.alpha import get_market_data
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .tests import *


class MarketDataView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        symbol = self.request.query_params.get("symbol")
        if symbol.upper() not in ["META", "AAPL", "MSFT", "GOOGL", "AMZN"]:
            return Response("Symbol not supported", status=status.HTTP_400_BAD_REQUEST)
        data = get_market_data(symbol)
        serializer_class = MarketDataSerializer(data)
        return Response(serializer_class.data)
