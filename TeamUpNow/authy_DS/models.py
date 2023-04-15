from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.utils import timezone 
from PIL import Image
import os

from OptionField_DS.models import *

from skills_TaggingField.models import *

from post_DS.models import (
						Post_DS,
                        Tag_DS, 
                        Follow_DS, 
                        Stream_DS, 
                        Likes_DS,
                        )



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
    	os.remove(full_path)

    return profile_pic_name


# Create your models here.
class Profile_DS(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile_DS')
	first_name=models.CharField(max_length=80, blank=False,null=False, verbose_name='first_name')
	last_name=models.CharField(max_length=80, blank=False,null=False, verbose_name='last_name')
	picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Picture2_DS')	
	favorites = models.ManyToManyField(Post_DS, blank=True)
	# favorites = models.ManyToManyField(Chart, blank=True)
	created =models.DateTimeField(default=timezone.now, blank=False,null=False)

	industry_and_projects = models.TextField( null=False,  blank=False, choices=INDUSTRY_AND_PROJECT_TYPES)
	## CONTACT DETAILS
	location = models.CharField(max_length=150, blank=False,null=False, verbose_name='address')
	telephone = models.CharField(max_length=80, null=True, blank=True)

	kaggle = models.CharField(max_length=80, null=True, blank=True)
	github = models.CharField(max_length=80, null=True, blank=True)
	linkedInn = models.CharField(max_length=80, null=True, blank=True)
	previous_CTO_linkedInn_link = models.CharField(max_length=80, null=True, blank=True)
	previous_HRmanager_linkedInn_link = models.CharField(max_length=80, null=True, blank=True)
	

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		SIZE = 250, 250

		if self.picture:
			pic = Image.open(self.picture.path)
			pic.thumbnail(SIZE, Image.LANCZOS)
			pic.save(self.picture.path)

	def __str__(self):
		return self.user.username
		

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		user_profile=Profile_DS.objects.create(user=instance)
		user_profile.save()

post_save.connect(create_user_profile, sender=User)
