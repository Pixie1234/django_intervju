# urls.py
from django.urls import path
from reviews.views import MyFormView

urlpatterns = [
    path("reviews-form", MyFormView.as_view(), name="myform"),
]
