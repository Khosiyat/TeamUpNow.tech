from django.urls import path

from direct_DS.views import(  			
							Inbox_DS, 

							Directs_DS, 

							UserSearch_DS, 

							Directs_DS, 

							NewConversation_DS, 

							SendDirect_DS, 

							# checkDirects_DS, 

							)
							

urlpatterns = [ 
   	path('', Inbox_DS, name='Inbox_DS'), 

   	path('Directs_DS/<username>', Directs_DS, name='Directs_DS'), 
	
   	path('UserSearch_DS/', UserSearch_DS, name='UserSearch_DS'), 
	
   	path('UserSearch_DS/<username>', NewConversation_DS, name='NewConversation_DS'), 
	
   	path('send_DS/', SendDirect_DS, name='send_direct_DS'), 

]