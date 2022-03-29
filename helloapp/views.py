
from django.shortcuts import render


# Create your views here.
from django.views import View


class HelloView(View):
    '''index view for myapp'''

    def get(self, request, name = 'world!'):
        context = {'name' : name}
        return render(request=request, template_name="index.html", context = context)

