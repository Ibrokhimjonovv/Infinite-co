from django.urls import path 
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('portfolio/<int:portfolio_id>', portfolio_detail, name="portfolio_detail")
]