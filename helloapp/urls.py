from django.urls import path, include
from helloapp.views import HelloView

urlpatterns = [
    # helloapp/
    path('', HelloView.as_view(), name='hello_world'),
    path('<name>', HelloView.as_view(), name='hello_name'),
    # helloapp/goodbye
    path('goodbye/', include('goodbyeapp.urls')),

]