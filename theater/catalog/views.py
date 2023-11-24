from django.db.models import Q
from rest_framework import permissions, viewsets
from django.shortcuts import render
from django.views import generic    
from .models import Play, Actor, Ticket, Genre, Viewer, Review, Booking
from catalog.serializers import GenreSerializer, PlaySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

def index(request):
    
    num_plays=Play.objects.all().count()
    num_actors=Actor.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_plays':num_plays,'num_actors':num_actors},
    )
    
from .forms import AddPlayForm
   
def add_play(request):
  
    if request.method == 'POST':
        form = AddPlayForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('plays')
            except:
                form.add_error(None, "Ошибка добавления спектакля")
    else:
        form = AddPlayForm(request.POST)


    form = AddPlayForm()
  
    return render(
        request,
        'add_play.html',
        context={'form':form},
    )

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class PlayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Play.objects.filter(Q(name__startswith='О'))
    serializer_class = PlaySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['get']) 
    def get_last_play(self, request, *args, **kwargs): 
        queryset = Play.objects.latest('id') 
        serializer = PlaySerializer(queryset) 
        return Response(serializer.data) 
    
    
    
class PlayListView(generic.ListView):
    model = Play
    paginate_by = 5

class PlayDetailView(generic.DetailView):
    model = Play

class ActorListView(generic.ListView):
    model = Actor
    paginate_by = 5

class ActorDetailView(generic.DetailView):
    model = Actor
