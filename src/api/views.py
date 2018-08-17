from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Risk
from .serializers import RiskAllSerializer, Risk1Serializer


@api_view(['GET'])
def get_risk_type(request, pk):
    risk = Risk.objects.filter(pk=pk)
    if not risk:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of risk
    if request.method == 'GET':
        serializer = Risk1Serializer(risk, many=True, read_only=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_risks(request):
    # get all risks
    if request.method == 'GET':
        risks = Risk.objects.all()
        serializer = RiskAllSerializer(risks, many=True)
        return Response(serializer.data)
