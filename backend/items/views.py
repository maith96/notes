from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import SchoolID, NationalID
from .serializers import SchoolIDSerializer, NationalIDSerializer

from rest_framework.response import Response
from rest_framework import status


class SchoolIDListCreate(generics.ListCreateAPIView):
    serializer_class = SchoolIDSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SchoolID.objects.filter(found_by=self.request.user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(found_by=self.request.user)
        else:
            print(serializer.errors)

class SchoolIDDelete(generics.DestroyAPIView):
    serializer_class = SchoolIDSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SchoolID.objects.filter(found_by=self.request.user)

class NationalIDListCreate(generics.ListCreateAPIView):
    serializer_class = NationalIDSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return NationalID.objects.filter(found_by=self.request.user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(found_by=self.request.user)
        else:
            print(serializer.errors)

class NationalIDDelete(generics.DestroyAPIView):
    serializer_class = NationalIDSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return NationalID.objects.filter(found_by=self.request.user)

class SearchItemByIdentifier(APIView):
    permission_classes = [AllowAny]

    def get(self, request, item_type, identifier):
        if item_type == 'school_id':
            # Search in SchoolID
            item = SchoolID.objects.filter(identifier=identifier).first()
            if item:
                serializer = SchoolIDSerializer(item)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        elif item_type == 'national_id':
            # Search in NationalID
            item = NationalID.objects.filter(identifier=identifier).first()
            if item:
                serializer = NationalIDSerializer(item)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # If item_type is not valid
            return Response({"detail": "Invalid item type."}, status=status.HTTP_400_BAD_REQUEST)

        # If no item found
        return Response({"detail": "Item not found."}, status=status.HTTP_404_NOT_FOUND)