"""work_space_1 URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from test_app import views  # ??????
from test_app.views import print_questions, ResultApiView, TestedUserApiView, AnswerApi

router = SimpleRouter()
router.register(r'user', TestedUserApiView)
router.register(r'result', ResultApiView)


urlpatterns = [
    path('', print_questions),
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('testing/', views.Testing.as_view()),
    path('answer/', views.AnswerApi.as_view()),
]

urlpatterns += router.urls
