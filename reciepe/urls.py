"""
URL configuration for reciepe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path , include
from django.conf import settings
from django.urls import re_path

from django.conf.urls.static import static
from user.viewsets import CustomTokenObtainPairView , CustomTokenRefereshview, EmailVerificationView
from apis.views import RecipeReviews , ReciepelistAPIview
# from apis.views import (
#     CategoryRecipes,
#     SingleCategoryRecipe,  PublicRecipes,
#     PublicRecipesDetail, RecipeReviews, UpVoteViewSet, ReciepelistAPIview
# )



urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/users/", include(("routers", "apis"), namespace="apis")),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefereshview.as_view(), name='token_refresh'),
    path('api/verify-email/', EmailVerificationView.as_view(), name='email-verify'),
    path('api/recipe/<int:id>/', ReciepelistAPIview.as_view(), name='user-reciepe'),

    # re_path(r'categories/(?P<category_pk>\d+)/recipes$',
    #     CategoryRecipes.as_view(), name='category_recipes'),
    # re_path(r'categories/(?P<category_pk>\d+)/recipes/(?P<pk>\d+)$',
    #     SingleCategoryRecipe.as_view(), name='single_category_recipe'),
    # re_path(r'public-recipes/$', PublicRecipes.as_view(), name='public_recipes'),
    # re_path(r'public-recipes/(?P<pk>\d+)/$', PublicRecipesDetail.as_view(),
    #     name='public_recipes_detail'),
    # re_path(r'public-recipes/(?P<pk>\d+)/reviews/$',
    #     RecipeReviews.as_view({'get': 'list', 'post': 'create'}),
    #     name='recipe_reviews'),
    # re_path(r'public-recipes/(?P<pk>\d+)/upvotes/$',
    #     UpVoteViewSet.as_view({'get': 'list', 'post': 'create'}),
    #     name='recipe_upvotes'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
