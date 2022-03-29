from django.shortcuts import render

# Create your views here.
from django.views import View


# Create your views here.
class GoodbyeView(View):
    def get(self, request, name='Everyone!'):
        context = {'name':name}
        return render(request=request, template_name="goodbye.html", context = context)