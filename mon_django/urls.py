from django.urls import path
from . import views

urlpatterns = [
	path('', views.mon_django,name='mon_django'),
	path('<int:pk>/',views.detail_sujet,name='detail_sujet'),
	path('nouveau/',views.nouveau_sujet,name='nouveau_sujet'),
	path('<int:pk>/editer',views.editer_sujet,name='editer_sujet'),
]