from django.shortcuts import render
from .models import Reviews
from .forms import ReviewForm

# Create your views here.


def index(request):
    return render(request, "reviews/index.html")
