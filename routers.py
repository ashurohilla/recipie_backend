from user.viewsets import RegisterViewSet

from rest_framework import routers
from user.viewsets import UserViewSet
from apis.views import reciepicreateViewSet, Catogoriescreate


router = routers.SimpleRouter(trailing_slash=False)

router.register(r"edit", UserViewSet, basename="user-edit")

router.register(r"register", RegisterViewSet, basename="register")
router.register(r"createrecipie", reciepicreateViewSet, basename="createrecipie")

router.register(r"catogries", Catogoriescreate, basename="CategoryViewSet")

# router.register(r"recipesview", RecipesViewSet, basename="RecipesViewSet")









urlpatterns = [
    *router.urls,
]
