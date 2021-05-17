from django.shortcuts import render
from .models import ServiceData


def test(request):
    obj = ServiceData.objects.get(id=1)
    return render(request, 'index.html', {'object': obj})
