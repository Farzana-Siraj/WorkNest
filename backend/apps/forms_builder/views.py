from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Form, FormField
from .serializers import FormFieldSerializer, FormSerializer


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


class FormFieldListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, form_id):
        fields = FormField.objects.filter(form_id=form_id).order_by("order")
        serializer = FormFieldSerializer(fields, many=True)
        return Response(serializer.data)

    def post(self, request, form_id):
        try:
            Form.objects.get(id=form_id, created_by=request.user)
        except Form.DoesNotExist:
            return Response({"error": "Not allowed"}, status=403)

        serializer = FormFieldSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(form_id=form_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
