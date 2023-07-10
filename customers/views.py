from customers.models import Customer
from django.http.response import JsonResponse, Http404
from customers.serializers import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers': serializer.data})

@api_view(['GET', 'POST', 'DELETE'])
def customer(request, id):
    try: 
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(data)
    return Response({'customer': serializer.data})

    