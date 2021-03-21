from django.conf.urls import url
from robertBosch.mentorship.user.views import UserRegistrationView
from robertBosch.mentorship.user.views import UserLoginView

urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin', UserLoginView.as_view()),
    ]
