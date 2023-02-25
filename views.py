from django.shortcuts import render
from .forms import client
from .models import Client
from django.db.models.signals import pre_init
from django.contrib.auth.models import User
from rest_framework import generics, filters,serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Client, Artist, Work
from .serializers import ClientSerializer, ArtistSerializer, WorkSerializer
#to use rest framework below mentioned classes are to be included
from rest_framework import generics,filters
from .models import Client,Work,Artist
from .serializers import ClientSerializer,WorkSerializer,ArtistSerializer
# Create your views here.
def registration(request):
    if request.method=='POST':
        form_instance=client(data=request.POST)
        if form_instance.is_valid():
            cd=form_instance.cleaned_data
            print(cd)
            saved=form_instance.save()
            obj=Client.objects.create(user=saved,name=cd['first_name'])
            obj.save()
    else:
        form_instance=client()
    return render(request,"display.html",{'form':form_instance})

class Client_list_create_api_view(generics.ListCreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

class Artist_list_create_api_view(generics.ListCreateAPIView):
    queryset=Artist.objects.all()
    serializer_class=ArtistSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['name']

class Work_list_create_api_view(generics.ListCreateAPIView):
    queryset=Work.objects.all()
    serializer_class=WorkSerializer
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=['artist_name']
    ordering_fields=['id','link','work_type']

class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.Serializer

    def create(self, request, *args, **kwargs):
        # Hash the password before creating the user
        password = make_password(request.data.get('password'))
        data = {**request.data, 'password': password}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Create a Client object for the user
        client = Client.objects.create(user=user, name=request.data.get('name'))
        client_serializer = ClientSerializer(client)

        headers = self.get_success_headers(serializer.data)
        return Response(client_serializer.data, status=status.HTTP_201_CREATED, headers=headers)