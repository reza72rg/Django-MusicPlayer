from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views import View
# Create your views here.


class Songlist(View):
    template_name = "song/home.html"
    def get(self, request):
        return render(request, self.template_name)
    