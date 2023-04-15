from django.urls import path

from notifications_DS.views import ( 
								# ShowNOtifications_DS_scored_and_requested, 

								ShowNOtifications_DS_evaluated_and_teamedUp, 

								DeleteNotification_DS, 

								CountNotifications_DS, 


								 )

								 


urlpatterns = [ 
	# path('ShowNOtifications_DS_scored_and_requested/', ShowNOtifications_DS_scored_and_requested, name='ShowNOtifications_DS_scored_and_requested'), 
	
	path('ShowNOtifications_DS_evaluated_and_teamedUp/', ShowNOtifications_DS_evaluated_and_teamedUp, name='ShowNOtifications_DS_evaluated_and_teamedUp'), 
	
   	# path('', ShowNOtifications_employer, name='show-notifications_employer'),
   	path('<noti_id>/DeleteNotification_DS', DeleteNotification_DS, name='delete-DeleteNotification_DS'), 
]