from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework import viewsets
from .serializers import DustSerializer
from .models import Fine_Dust
from django.shortcuts import render

# Create your views here.
"""
def status(request) :
    return render(request, 'api/status.html', {})
"""
class DustViewSet(viewsets.ModelViewSet):
    serializer_class = DustSerializer
    queryset = Fine_Dust.objects.all().order_by("-id")[:10]

    def list(self, request):
        return super().list(request)

    def create(self, request):
        serializer = DustSerializer(data=request.data)

        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse({'status': True, 'details': 'Success'}, safe=False)
        else:
            return JsonResponse({'status': False, 'details': 'serializer is not valid'}, safe=False)
