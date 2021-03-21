from django.conf.urls import url
from robertBosch.mentorship.profile.views import UserProfileView


urlpatterns = [
    url(r'^profile', UserProfileView.as_view()),
    ]
