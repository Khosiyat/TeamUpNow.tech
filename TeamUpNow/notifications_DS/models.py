from django.db import models
from django.contrib.auth.models import User


class Notification_DS(models.Model):
	NOTIFICATION_TYPES = ((1,'Like'),(2,'Comment'), (3,'Follow'))

	post = models.ForeignKey('post_DS.Post_DS', on_delete=models.CASCADE, related_name="noti_DS", blank=True, null=True)
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noti_from_user_DS")
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noti_to_user_DS")
	notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
	text_preview = models.CharField(max_length=90, blank=True)

	request_talents = models.CharField(max_length=90, blank=True)
	sdls_phase = models.CharField(max_length=90, blank=True)
	ocuppation = models.CharField(max_length=90, blank=True)

	
	date = models.DateTimeField(auto_now_add=True)
	is_seen = models.BooleanField(default=False)
