from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from test_app import views  #
from test_app.views import ResultApiView, TestedUserApiView, AnswerApi

router = SimpleRouter()
router.register(r'user', TestedUserApiView)
router.register(r'result', ResultApiView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('testing/', views.Testing.as_view()),
    path('answer/', views.AnswerApi.as_view()),
]

urlpatterns += router.urls
