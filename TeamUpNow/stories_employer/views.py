from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from stories_employer.models import Story_employer, StoryStream_employer
from stories_employer.forms import NewStoryForm_employer

from datetime import datetime, timedelta


@login_required
def NewStory_employer(request):
	user = request.user
	file_objs = []

	if request.method == "POST":
		form = NewStoryForm_employer(request.POST, request.FILES)
		if form.is_valid():
			file = request.FILES.get('content')
			caption = form.cleaned_data.get('caption')

			story = Story_employer(user=user, content=file, caption=caption)
			story.save()
			return redirect('index')
	else:
		form = NewStoryForm_employer()

	context = {
		'form': form,
	}

	return render(request, 'templates_employer/newstory_employer.html', context)


def ShowMedia_employer(request, stream_id):
	stories = StoryStream_employer.objects.get(id=stream_id)
	media_st = stories.story.all().values()

	stories_list = list(media_st)

	return JsonResponse(stories_list, safe=False)