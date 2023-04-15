from django.contrib import admin

# from stories.models import Story, StoryStream
from stories_employer.models import Story_employer, StoryStream_employer

# Register your models here.

admin.site.register(Story_employer)
admin.site.register(StoryStream_employer)