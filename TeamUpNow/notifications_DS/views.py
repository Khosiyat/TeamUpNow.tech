from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from notifications_DS.models import Notification_DS
from post_DS.models import Follow_DS,Stream_DS,Stream_DS, Post_DS, Experience_chart

from direct_DS.models import Message_DS
from direct_DS.forms import MessageSendForm_DS

from .utils import *
from TeamUpNow.model_objects_DS import (Post_Objects_DS, 
											 Post_Objects_SkillsIllustrations_DS,
											Post_Display_DS, 
											Post_Display_contextList_DS, 
											Profile_Objects_DS, 
											Profile_dateCalculations_DS, 
											Profile_activityCalculations_DS,
											Profile_Illustrations_DS, 
											Profile_ProjectsIllustrations_DS, 
											Profile_Display_contextList_DS)


from datetime import date, timedelta,datetime


# ##########################################################################################################################################################################################

def ShowNOtifications_DS_evaluated_and_teamedUp(request,username):
	
	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/direct/notifications_DS_evaluated_and_teamedUp.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################
def DeleteNotification_DS(request, noti_id):
	user = request.user
	Notification_DS.objects.filter(id=noti_id, user=user).delete()
	return redirect('ShowNOtifications_DS_evaluated_and_teamedUp')

##########################################################################################################################################################################################

def CountNotifications_DS(request):
	count_notifications = 0
	if request.user.is_authenticated:
		count_notifications = Notification_DS.objects.filter(user=request.user, is_seen=False).count()

	return {'count_notifications':count_notifications}
	