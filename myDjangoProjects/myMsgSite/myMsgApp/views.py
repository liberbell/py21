from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "myMsgApp/home.html",
                {'message_1':'Some content on Home page.',
                 'message_2':'More detail on content of Home page.'
                 })
                #   {'h1Text': 'MessageBox',
                #   'pText': 'Welcome to the Message Box App! Click Login button below to begin.'})