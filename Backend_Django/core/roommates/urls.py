from django.urls import path
from django.views.generic import TemplateView

app_name = 'roommates'

urlpatterns = [
    # Homepage
    path('', TemplateView.as_view(template_name='roommates/index.html'))
]