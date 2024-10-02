
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home', get_feedbacks),
    path('postData', postFeedback),
    
]
