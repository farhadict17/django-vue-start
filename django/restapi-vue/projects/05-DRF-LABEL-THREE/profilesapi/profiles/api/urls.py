from django.urls import include,path
from rest_framework.routers import DefaultRouter # crate auto url
from profiles.api.views import (AvatarUpdateView, ProfileViewSet, 
                                ProfileStatusViewSet)

router = DefaultRouter ()
router.register(r"profiles", ProfileViewSet) # r means raw string
router.register(r"status", ProfileStatusViewSet, basename="status")
# profile_list = ProfileViewSet.as_view({"get":"list"}) #router class reduce this type of task
# profile_detail = ProfileViewSet.as_view({"get":"retrieve"}) #router class reduce this type of task

urlpatterns = [
    path("",include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update")
    # path("profiles/",profile_list,name="profile-list"),
    # path("profiles/<int:pk>/",profile_detail,name="profile-detail")
]
