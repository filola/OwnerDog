import json

from django.http import JsonResponse
from django.views import View

from owners.models import Dog, Owner
# Create your views here.
# 주인 post
class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(name=data['owner'], email=data['email'], age=data['o_age'])
        return JsonResponse({'MESSAGE':'OWNER CREATED'}, status=200)

# 강아지 post
class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(name=data['name'])
        dog = Dog.objects.create(name=data['dog'], age=data['d_age'],owner=owner)
        return JsonResponse({'MESSAGE':'Dog CREATED'}, status=200)

# 주인 목록 get
class OwnerListView(View):
    def get(self, request):
        owners = Owner.objects.all()
        result=[]
        for owner in owners:
            dog = Dog.objects.filter(owner=owner)
            result.append(
                {
                    "name" : owner.name,
                    "age" : owner.age,
                    "email" : owner.email,
                    "dog" : list(dog.values())
                }
            )
        return JsonResponse({'results':result}, status=200)
        
# 강아지 목록 get
class DogListView(View):
    def get(self, request):
        dogs = Dog.objects.all()
        result=[]
        for dog in dogs:
            result.append(
                {
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" : dog.owner.name
                }
            )
        return JsonResponse({'results':result}, status=200)
