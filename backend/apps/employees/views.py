from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EmployeeData
from .serializers import EmployeeDataSerializer


class EmployeeListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employees = EmployeeData.objects.filter(created_by=request.user)
        serializer = EmployeeDataSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeDataSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            employee = EmployeeData.objects.get(id=pk, created_by=request.user)
            employee.delete()
            return Response({"message": "Deleted successfully"})
        except EmployeeData.DoesNotExist:
            return Response({"error": "Not found"}, status=404)
