"""apidatacount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Article.views import ArticleAPIView
from decision import views as view1
from homepage import views as view2

handler404 = 'Article.views.error_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/article', ArticleAPIView.as_view()),
    path('api/v1/article/', ArticleAPIView.as_view()),
    path('decision/', view1.decision),
    path('', view2.homepage),
    path('documentation/', view2.documentation),
]