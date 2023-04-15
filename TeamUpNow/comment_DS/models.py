from email.policy import default
from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save, post_delete

from post_DS.models import Post_DS
from notifications_DS.models import Notification_DS
from OptionField_DS.models import *


class Comment_DS(models.Model):
	post = models.ForeignKey(Post_DS, on_delete=models.CASCADE, related_name='comments_DS')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_user_DS')

	request_talents=models.CharField(max_length=300, blank=True,null=True, default='talent is requested', choices=REQUEST_TALENTS)
	sdls_phase=models.CharField(max_length=300, blank=True,null=True, default='SDLS Phase is not defined', choices=SDLC_PHASES)
	ocuppation=models.CharField(max_length=300, blank=True,null=True, default='Ocuppation is not defined', choices=OCCUPATION)


	date = models.DateTimeField(auto_now_add=True)

	def user_comment_post(sender, instance, *args, **kwargs):
		comment = instance
		post = comment.post

		request_talents=comment.request_talents
		sdls_phase=comment.sdls_phase
		ocuppation=comment.ocuppation


		sender = comment.user
		notify = Notification_DS(post=post, 
									   sender=sender, 
									   user=post.user, 
									   
									   request_talents=request_talents, 
									   sdls_phase=sdls_phase, 
									   ocuppation=ocuppation,
									   
									   notification_type=2,)
		notify.save()

	def user_del_comment_post(sender, instance, *args, **kwargs):
		like = instance
		post = like.post
		sender = like.user

		notify = Notification_DS.objects.filter(post=post, sender=sender, notification_type=2)
		notify.delete()

#Comment
post_save.connect(Comment_DS.user_comment_post, sender=Comment_DS)
post_delete.connect(Comment_DS.user_del_comment_post, sender=Comment_DS)












