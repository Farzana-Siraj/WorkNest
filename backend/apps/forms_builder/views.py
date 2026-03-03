from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Form
from .serializers import FormSerializer


class FormListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        forms = Form.objects.filter(created_by=request.user)
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FormSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
