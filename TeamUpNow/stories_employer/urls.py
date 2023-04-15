from django.urls import path

from stories_employer.views import (NewStory_employer, 
						   ShowMedia_employer,
						   )
						   
urlpatterns = [
	path('newstory_employer/', NewStory_employer, name='newstory_employer'),
	path('showmedia_employer/<stream_id>', ShowMedia_employer, name='showmedia_employer'),
]