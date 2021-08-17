import json

from django.http import JsonResponse
from django.views import View

from owners.models import Dog, Owner
# Create your views here.

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(name=data['owner'], email=data['email'], age=data['o_age'], dog=dog)
        return JsonResponse({'MESSAGE':'OWNER CREATED'}, status=200)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(name=data['name'])
        dog = Dog.objects.create(name=data['dog'], age=data['d_age'],owner=owner)
        return JsonResponse({'MESSAGE':'Dog CREATED'}, status=200)







    # def get(self, request):
    #     owners = Owner.objects.all()
    #     result=[]
    #     for owner in owners:
    #         result.append(
    #             {
    #                 "name" : owner.name,
    #                 "age" : owner.age,
    #                 "email" : owner.email,
    #                 # "dog" : {
    #                 #     "name" : owner.dog.dog,
    #                 #     "age" : owner.dog.age 
    #                 # }
    #             }
    #         )
    #     return JsonResponse({'results':result}, status=200)
