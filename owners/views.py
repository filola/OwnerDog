import json

from django.http import JsonResponse
from django.views import View

from owners.models import Dog, Owner
# Create your views here.

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(name=data['owner'], email=data['email'], age=data['o_age'])
        Dog.objects.create(name=data['dog'], age=data['d_age'], owner=owner)
        return JsonResponse({'MESSAGE':'CREATED'}, status=200)
