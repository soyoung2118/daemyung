from django.shortcuts import render

# Create your views here.
def interior(request):
    return render(request, 'interior/interior.html')