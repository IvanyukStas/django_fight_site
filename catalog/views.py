from django.shortcuts import render

# Create your views here.
from django.views import generic

from catalog.models import Fighter


def index(request):
    num_fighters = Fighter.objects.all().count()
    print(num_fighters)
    return render(request, 'index.html', context={'num_fighters': num_fighters}, )

class FighterViewList(generic.ListView):
    model = Fighter


class FighterViewDetail(generic.DetailView):
    model = Fighter