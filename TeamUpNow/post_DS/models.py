import uuid
from django.db import models
from django.contrib.auth.models import User


from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify
from django.urls import reverse
from pkg_resources import evaluate_marker


from notifications_DS.models import Notification_DS

from django.utils import timezone 


from django.core.validators import MinValueValidator, MaxValueValidator



from OptionField_DS.models import *

from skills_TaggingField.models import *


################################################################################################ MODELS

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Tag_DS(models.Model):
	title = models.CharField(max_length=75, verbose_name='Tag_DS')
	slug = models.SlugField(null=False, unique=True)

	class Meta:
		verbose_name='Tag'
		verbose_name_plural = 'Tags'

	def get_absolute_url(self):
		return reverse('tags', args=[self.slug])
		
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)

class PostFileContent_DS(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_owner_DS')
	file = models.FileField(upload_to=user_directory_path)



class Experience_chart(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience_chart_DS')
	
	# technical_task = models.CharField(default="Technical Task", max_length=20) 
	technical_task=models.CharField(max_length=300, blank=True,null=True)

	
	# responsible = models.ForeignKey(User, on_delete=models.CASCADE)
	# responsible = models.ManyToManyField(ProvidedBenefits, blank=True)
	technical_ocuppation=models.CharField(max_length=300, blank=True,null=True)
	


	week_number = models.CharField(max_length=2, blank=True)
	start_date = models.DateField(default=timezone.now)
	finish_date = models.DateField(default=timezone.now)
	posted = models.DateTimeField(default=timezone.now, blank=True,null=True,)
	
	def __str__(self):
		return str(self.posted)
		
		#overiding the save method
	def save(self, *args, **kwargs):
		print(self.start_date.isocalendar()[1])
		if self.week_number == "":
			self.week_number = self.start_date.isocalendar()[1]
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('postdetails_DS', args=[str(self.id)])





class Post_DS(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_DS_DS')
	# evaluator=models.IntegerField('Evaluator', blank=False, default=1)
	# evaluator=models.IntegerField('user', blank=False, default=1)

	posted = models.DateTimeField(default=timezone.now, blank=True,null=True,)

	# # tags = models.ManyToManyField(Tag, related_name='tags')
	# # attendees_evaluated = models.ManyToManyField(User, blank=True,null=True, related_name="attendees_evaluated_DS")
	attendees_evaluated = models.ForeignKey(User, blank=True,null=True, on_delete= models.SET_NULL, related_name="attendees_DS")


	#######################################---------->>> SOFT SKILLSMETHOD TYPES
	task_choice=models.CharField(max_length=300, blank=True,null=True, choices=TASK_CHOICE)

	project_choice=models.CharField(max_length=300, blank=True,null=True, choices=PROJECT_CHOICE)

	examine_types=models.CharField(max_length=300, blank=True,null=True, choices=EXAMINE_TYPE)

	task_method=models.CharField(max_length=300, blank=True,null=True, choices=INTERVIEW_METHOD)

	task_completion=models.CharField(max_length=300, blank=True,null=True, choices=TASK_COMPLETION)

	sdls_phase=models.CharField(max_length=300, blank=True,null=True, choices=SDLC_PHASES)

	evaluation_duration=models.CharField(max_length=300, blank=True,null=True, choices=EVALUATION_DURATION)



#######################################---------->>> Tech Skills

	#SCORE SYSTEM:
	# 0='No experience'
	# 1='Low experienced'
	# 2='Midium experienced'
	# 3='Higly experienced'
	# 4='Expert'

	#CODE QUALITY

	clean_SCORE = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	clean_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Clean')

	refactored_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	refactored_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Refactored') 

	well_documented_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	well_documented_NOTE =models.TextField(max_length=200, null=True, blank=True, verbose_name='well documented')

	unit_tested_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	unit_tested_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Unit Tested')

	debuged_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	debuged_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Debuged')

	debuged_with_other_team_members_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	debuged_with_other_team_members_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Debuged with other team members')
	
	debuged_other_team_members_bugs_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	debuged_other_team_members_bugs_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Debuged other team members bugs') 

	#PROCESS QUALITY

	analyzed_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	analyzed_NOTE =  models.TextField(max_length=200, null=True, blank=True, verbose_name='Analyzed')

	analyzed_with_other_team_members_SCORE  = models.IntegerField(default=1, null=True, blank=True,  validators=[MinValueValidator(1), MaxValueValidator(4)])
	analyzed_with_other_team_members_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Analyzed with other team members')

	analyzed_other_team_members_script_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	analyzed_other_team_members_script_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Analyzed other team members script') 


	discussed_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	discussed_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Discussed') 

	discussed_with_other_team_members_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	discussed_with_other_team_members_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Discussed with other team members')


	expected_problems_are_reasoned_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	expected_problems_are_reasoned_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Expected problems are reasoned')  

	arbitrary_problems_are_reasoned_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	arbitrary_problems_are_reasoned_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Arbitrary problems are reasoned') 


	expected_constraints_are_reasoned_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	expected_constraints_are_reasoned_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Expected constraints are reasoned') 

	arbitrary_constraints_are_reasoned_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	arbitrary_constraints_are_reasoned_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Arbitrary constraints are reasoned') 


	designed_with_one_approach_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	designed_with_one_approach_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Designed with one approach') 

	designed_with_multiple_possible_approaches_SCORE  = models.IntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
	designed_with_multiple_possible_approaches_NOTE = models.TextField(max_length=200, null=True, blank=True, verbose_name='Designed with multiple possible approaches')
	
	
	# codingQuality = models.ManyToManyField(CodingQuality)
	# codingQuality_OPTION=models.CharField(max_length=300, blank=True,null=True, choices=CODING_QUALITY)
	# note_coding_quality = models.TextField(max_length=500, null=True, blank=True, verbose_name='note_coding_quality_DS')
	# score_codingQuality = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])


	#Scoring
	likes = models.IntegerField(default=0)
	conciseness = models.IntegerField(default=0) # conciseness rating
	relevancy = models.IntegerField(default=0) # relevancy rating





	# clean_SCORE
	# clean_NOTE

	# refactored_SCORE
	# refactored_NOTE

	# well_documented_SCORE
	# well_documented_NOTE

	# unit_tested_SCORE
	# unit_tested_NOTE

	# debuged_SCORE
	# debuged_NOTE

	# debuged_with_other_team_members_SCORE
	# debuged_with_other_team_members_NOTE
	
	# debuged_other_team_members_bugs_SCORE
	# debuged_other_team_members_bugs_NOTE

	# #PROCESS QUALITY

	# analyzed_SCORE
	# analyzed_NOTE

	# analyzed_with_other_team_members_SCORE
	# analyzed_with_other_team_members_NOTE

	# analyzed_other_team_members_script_SCORE
	# analyzed_other_team_members_script_NOTE


	# discussed_SCORE
	# discussed_NOTE 

	# discussed_with_other_team_members_SCORE
	# discussed_with_other_team_members_NOTE


	# expected_problems_are_reasoned_SCORE
	# expected_problems_are_reasoned_NOTE

	# arbitrary_problems_are_reasoned_SCORE
	# arbitrary_problems_are_reasoned_NOTE


	# expected_constraints_are_reasoned_SCORE
	# expected_constraints_are_reasoned_NOTE

	# arbitrary_constraints_are_reasoned_SCORE
	# arbitrary_constraints_are_reasoned


	# designed_with_one_approach_SCORE
	# designed_with_one_approach_NOTE

	# designed_with_multiple_possible_approaches_SCORE
	# designed_with_multiple_possible_approaches_NOTE

	def get_absolute_url(self):
		return reverse('postdetails_DS', args=[str(self.id)])

	def __str__(self):
		return str(self.id)


class Follow_DS(models.Model):
	follower = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='follower_DS')
	following = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='following_DS')

	def user_follow(sender, instance, *args, **kwargs):
		follow = instance
		sender = follow.follower
		following = follow.following
		notify = Notification_DS(sender=sender, user=following, notification_type=3)
		notify.save()

	def user_unfollow(sender, instance, *args, **kwargs):
		follow = instance
		sender = follow.follower
		following = follow.following

		notify = Notification_DS.objects.filter(sender=sender, user=following, notification_type=3)
		notify.delete()

class Stream_DS(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='stream_following_DS')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_user_DS')   
    post = models.ForeignKey(Post_DS, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()

    def add_post(sender, instance, *args, **kwargs):
    	post = instance
    	user = post.user
    	followers = Follow_DS.objects.all().filter(following=user)
    	for follower in followers:
    		stream = Stream_DS(post=post, user=follower.follower, date=post.posted, following=user)
    		stream.save()

class Likes_DS(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like_DS')
	post = models.ForeignKey(Post_DS, on_delete=models.CASCADE, related_name='post_like_DS')

	def user_liked_post(sender, instance, *args, **kwargs):
		like = instance
		post = like.post
		sender = like.user
		notify = Notification_DS(post=post, sender=sender, user=post.user, notification_type=1)
		notify.save()

	def user_unlike_post(sender, instance, *args, **kwargs):
		like = instance
		post = like.post
		sender = like.user

		notify = Notification_DS.objects.filter(post=post, sender=sender, notification_type=1)
		notify.delete()

class Relevancy_DS(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_relevancy_DS')
	post = models.ForeignKey(Post_DS, on_delete=models.CASCADE, related_name='post_relevancy_DS')

	def user_liked_post(sender, instance, *args, **kwargs):
		relevancy = instance
		post = relevancy.post
		sender = relevancy.user
		notify = Notification_DS(post=post, sender=sender, user=post.user, notification_type=1)
		notify.save()

	def user_unlike_post(sender, instance, *args, **kwargs):
		relevancy = instance
		post = relevancy.post
		sender = relevancy.user

		notify = Notification_DS.objects.filter(post=post, sender=sender, notification_type=1)
		notify.delete()



class Conciseness_DS(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_conciseness_DS')
	post = models.ForeignKey(Post_DS, on_delete=models.CASCADE, related_name='post_conciseness_DS')

	def user_liked_post(sender, instance, *args, **kwargs):
		conciseness = instance
		post = conciseness.post
		sender = conciseness.user
		notify = Notification_DS(post=post, sender=sender, user=post.user, notification_type=1)
		notify.save()

	def user_unlike_post(sender, instance, *args, **kwargs):
		conciseness = instance
		post = conciseness.post
		sender = conciseness.user

		notify = Notification_DS.objects.filter(post=post, sender=sender, notification_type=1)
		notify.delete()




#Stream
post_save.connect(Stream_DS.add_post, sender=Post_DS)

#Likes
post_save.connect(Likes_DS.user_liked_post, sender=Likes_DS)
post_delete.connect(Likes_DS.user_unlike_post, sender=Likes_DS)


#Relevancy
post_save.connect(Relevancy_DS.user_liked_post, sender=Relevancy_DS)
post_delete.connect(Relevancy_DS.user_unlike_post, sender=Relevancy_DS)

#Conciseness
post_save.connect(Conciseness_DS.user_liked_post, sender=Conciseness_DS)
post_delete.connect(Conciseness_DS.user_unlike_post, sender=Conciseness_DS)

#Follow
post_save.connect(Follow_DS.user_follow, sender=Follow_DS)
post_delete.connect(Follow_DS.user_unfollow, sender=Follow_DS)

