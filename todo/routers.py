from rest_framework import routers
from todo.views import TodoViewset

router = routers.DefaultRouter()
router.register(r'todo',TodoViewset)