from django.urls import URLPattern, path, include
from django.contrib import admin
from doli import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('post', views.PostViewSet, basename='post')
router.register('comment', views.CommentViewSet, basename='comment')
router.register('like', views.LikeViewSet, basename='like')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.UserCreateAPIView.as_view()),
    path('auth/', include('rest_framework.urls')),
    path('get-token/', obtain_auth_token),
    path('', include(router.urls))
]
