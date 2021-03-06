from . import views
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from gimnasio.views import ExcerciseViewSet, RoutineViewSet, RegisterView, me

router = routers.DefaultRouter()
router.register(r'Recipes', ExcerciseViewSet)
router.register(r'Products', RoutineViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('me/', me)
]