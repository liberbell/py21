from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "myMsgApp/home.html",
                  {'h1Text': 'MessageBox',
                  'pText': 'Welcome to the Message Box App! Click Login button below to begin.'})