from django.urls import path
from goodbyeapp.views import GoodbyeView

urlpatterns = [
    # goodbye/
    path('', GoodbyeView.as_view(), name='goodbye_all'),
    path('<name>', GoodbyeView.as_view(), name='goodbye_name'),

]