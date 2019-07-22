# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Create_Place, Create_Location, Create_View_Videos_Location, Vote_for_video

urlpatterns = {

    url(r'^location/(?P<place_id>[\w\ ]+)/$$', Create_Location.as_view(), name="create"),

    url(r'^videos_location/(?P<location_id>[\w\ ]+)/$', Create_View_Videos_Location.as_view(), name="create"),

	url(r'^place/$', Create_Place.as_view(), name="create_place"),

	# Add vote to video
	url(r'^vote_by_video/(?P<video_id>[\w\ ]+)/$', Vote_for_video.as_view(), name="vote_by_video"),

}

urlpatterns = format_suffix_patterns(urlpatterns)