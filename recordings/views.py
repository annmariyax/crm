from django.shortcuts import render

from django.views import View

# Create your views here.

class RecordingsView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"recordings/recordings.html")

