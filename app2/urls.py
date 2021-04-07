from django.urls import path
from app2 import views
app_name="app2"

urlpatterns=[
    path('',views.index,name="index"),
    path('sample2/',views.sample,name="sample2"),
    path("sample_app2/",views.sample_view,name="sample_view"),
    path("<data>/",views.carry_data,name="carry_data"),
]