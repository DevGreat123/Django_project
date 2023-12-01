from django.urls import path
from app_list import views

urlpatterns = [
    path('student-data/', views.StudentView.as_view())
]

