from calendar import calendar
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max
from django.utils import timezone 
from datetime import datetime

from OptionField_DS.models import *

# Create your models here.
class Message_DS(models.Model):


	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_DS')
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user_DS')
	recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user_DS')
	# body = models.TextField(max_length=1000, blank=True, null=True)

	start_date=models.DateField(default=timezone.now)
	end_date=models.DateField(default=timezone.now)
	start_time=models.DateField(default=timezone.now)
	end_time=models.DateField(default=timezone.now)


	# body=models.ManyToManyField(BehaviouralChallange)
	body=models.CharField(max_length=300, blank=True,null=True, choices=EXAM_TYPE)
	body2=models.CharField(max_length=300, blank=True,null=True, choices=SCHEDULE_STATUS)

	task_choice=models.CharField(max_length=300, blank=True,null=True, choices=TASK_CHOICE)

	project_choice=models.CharField(max_length=300, blank=True,null=True, choices=PROJECT_CHOICE)

	examine_types=models.CharField(max_length=300, blank=True,null=True, choices=EXAMINE_TYPE)

	task_method=models.CharField(max_length=300, blank=True,null=True, choices=INTERVIEW_METHOD)

	task_completion=models.CharField(max_length=300, blank=True,null=True, choices=TASK_COMPLETION)

	sdls_phase=models.CharField(max_length=300, blank=True,null=True, choices=SDLC_PHASES)

	evaluation_duration=models.CharField(max_length=300, blank=True,null=True, choices=EVALUATION_DURATION)



	date = models.DateTimeField(auto_now_add=True)
	is_read = models.BooleanField(default=False)

	def send_message(from_user, to_user, body, body2, task_choice, project_choice,  examine_types,  task_method,  task_completion,  sdls_phase,  evaluation_duration):
		sender_message = Message_DS(
			user=from_user,
			sender=from_user,
			recipient=to_user,
			body=body,
			body2=body2,

			task_choice=task_choice,
			project_choice=project_choice,
			examine_types=examine_types,
			task_method=task_method,
			task_completion=task_completion,
			sdls_phase=sdls_phase,
			evaluation_duration=evaluation_duration,


			is_read=True)
		sender_message.save()


		recipient_message = Message_DS(
			user=to_user,
			sender=from_user,
			body=body,
			body2=body2,

			task_choice=task_choice,
			project_choice=project_choice,
			examine_types=examine_types,
			task_method=task_method,
			task_completion=task_completion,
			sdls_phase=sdls_phase,
			evaluation_duration=evaluation_duration,
			

			recipient=from_user,)
			
		recipient_message.save()
		return sender_message

	def get_messages(user):
		messages = Message_DS.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
		users = []
		for message in messages:
			users.append({
				'user': User.objects.get(pk=message['recipient']),
				'last': message['last'],
				'unread': Message_DS.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()
				})
		return users

	