from django.shortcuts import render


def index (reqest):
    return render(reqest,"CV/index.html")

# Create your views here.
