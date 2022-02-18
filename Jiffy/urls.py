
from django.contrib import admin
from django.urls import path
from newsfeed import views as newsfeed_views
from chatbox import views as chatbox_views
from story import views as story_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', newsfeed_views.homepage),
    path('aboutpage/', newsfeed_views.aboutpage),
    path('contactpage/', newsfeed_views.contactpage),
    path('chathome/', chatbox_views.chathome),
    path('chatabout/', chatbox_views.chatabout),
    path('chatcontact/', chatbox_views.chatcontact),
    path('storyhome/', story_views.storyhome),
    path('storyabout/', story_views.storyabout),
    path('storycontact/', story_views.storycontact),
]
