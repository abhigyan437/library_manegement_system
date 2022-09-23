from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.authtoken import views as view
#from .router import router as route

router = routers.DefaultRouter()
router.register(r'company',views.MemberViewSet)
router.register(r'team',views.BooksViewSet)

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('', views.home, name='home'),
    path('signin/register/register/signin/', views.register_login, name='reglogin'),
    path('signin/', views.login, name='login'),
    path('signin/register/', views.register, name='register'),
    path('signin/register/registering/', views.registering, name='registering'),
    path('delete/',views.delete_account,name = 'delete'),
    path('index/booking/<str:book_name>',views.booking,name = 'booking'),
    path('index/returning/<str:book_name>',views.returning, name = 'returning'),
    path('delete/deleting/',views.deleting,name = 'deleting'),

]