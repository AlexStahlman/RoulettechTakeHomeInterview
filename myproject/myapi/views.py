from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import ContactForm
from .serializers import ContactFormSerializer


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello! Welcome to my webpage, this is showcasing a basic knowlege of DJango!'})

@api_view(['GET'])
def greetings_traveler(request):
    return Response({'message': 'Please send a form!'})

class SubmitContactFormView(APIView):
    def post(self, request, format=None):
        serializer = ContactFormSerializer(data=request.data)
 
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Form submitted successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)