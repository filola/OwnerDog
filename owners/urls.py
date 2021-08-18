from django.urls import path

from owners.views import OwnerView, DogView, OwnerListView, DogListView
urlpatterns = [
    path('owner', OwnerView.as_view()),
    path('dog', DogView.as_view()),
    path('ownerlist', OwnerListView.as_view()),
    path('doglist', DogListView.as_view()),
]
