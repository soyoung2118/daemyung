from django.shortcuts import render
from .models import Carousel
# Create your views here.
def main(request):
    carousel = Carousel.objects.all()
    context = {
        'carousel': carousel
    }
    return render(request, 'main/main_page.html', context)
