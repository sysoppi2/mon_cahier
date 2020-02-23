from django.urls import path
from . import views

urlpatterns = [
	path('', views.memos_linux,name='memos_linux'),
	path('<int:pk>/',views.detail_memo,name='detail_memo'),
	path('nouveau/',views.nouveau_memo,name='nouveau_memo'),
	path('<int:pk>/editer/', views.editer_memo,name='editer_memo'),
	path('contact/',views.contact,name='contact'),
]