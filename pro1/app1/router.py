"""
from .views import userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'app1', userviewsets, 'app1')
"""