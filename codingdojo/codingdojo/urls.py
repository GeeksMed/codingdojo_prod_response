"""codingdojo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from codingdojo import views

urlpatterns = [
    path('', views.produto, name='home'),
    path('produto/<int:id>',views.ver_produto, name='produto'),
    path('produto/adicionar/', views.adicionar_produto, name="produto_adicionar"),
    path('deletar/<int:id>', views.deletar_produto, name="produto_deletar")
]
