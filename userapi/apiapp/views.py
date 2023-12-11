from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserProfile, Warehouse
from .serializers import UserProfileSerializer, WarehouseSerializer

@api_view(['POST'])
def register_user(request):
    # print("request data------", request.data)
    serializer = UserProfileSerializer(data=request.data)
    # print("serializer data -----", serializer)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': status.HTTP_201_CREATED, 'issaved': True, 'status_msg': 'User registered successfully'})
    else:
        print('serializers error data--------,', serializer.errors)
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'issaved': False, 'status_msg': 'Invalid data'  }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def warehouse_list(request):
    if request.method == 'GET':
        warehouses = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_201_CREATED, 'issaved': True, 'status_msg': 'Warehouse created successfully'})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'issaved': False, 'status_msg': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def warehouse_detail(request, pk):
    try:
        warehouse = Warehouse.objects.get(pk=pk)
    except Warehouse.DoesNotExist:
        return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Warehouse not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WarehouseSerializer(warehouse)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WarehouseSerializer(warehouse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_200_OK, 'issaved': True, 'status_msg': 'Warehouse updated successfully'})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'issaved': False, 'status_msg': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        warehouse.delete()
        return Response({'status': status.HTTP_204_NO_CONTENT, 'message': 'Warehouse deleted successfully'})