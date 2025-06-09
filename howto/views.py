from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import HowTo, Recommendation
from .forms import Recommendation

# View to return 'How To ...' page
class HowToList(generic.ListView):
    """
    Returns all published 'How To ...' links and displays them
    """
    queryset = HowTo.objects.filter(status=1)
    template_name = "howto/howto.html"


def howto_part(request):
    """
    Renders 'How To ...' page
    """
    howto = HowTo.objects.all().order_by('title')

    return render(
        request,
        "howto/howto.html",
        {
            "howto": howto,
        },
    )
