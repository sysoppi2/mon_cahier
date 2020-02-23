"""e_cahier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from maison import views
from memos_linux import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('admin/', admin.site.urls),
	path('',include('accueil.urls')),
	path('/',include('accueil.urls')),
	path('arriere_boutique',include('arriere_boutique.urls')),
	path('arriere_boutique/',include('arriere_boutique.urls')),
	path('memos_linux',include('memos_linux.urls')),
	path('memos_linux/',include('memos_linux.urls')),
	path('maison',include('maison.urls')),
	path('maison/',include('maison.urls')),
	path('mini_url/',include('mini_url.urls')),
	path('blog/',include('blog.urls')),
	path('mon_django',include('mon_django.urls')),
	path('mon_django/',include('mon_django.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
