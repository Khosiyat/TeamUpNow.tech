from django.urls import path
from django.contrib.auth import views as authViews 

from authy_DS.views import ( 
						PasswordChange, 
						PasswordChangeDone, 

						Signup_DS, 
						
						EditProfile_DS, 

						login_DS, 

						login_DS_CreateProject, 

						Delete_accoundt_DS,
						pre_Delete_accoundt_DS,


						)

urlpatterns = [
   	
    path('profile/EditProfile_DS', EditProfile_DS, name='edit-profile_DS'), 
 
	path('Signup_DS/', Signup_DS, name='Signup_DS'), 
	   
	path('login_DS/', login_DS, name="login_DS"),   

	path('login_DS_CreateProject/', login_DS_CreateProject, name="login_DS_CreateProject"),   
	   
   	path('logout_DS/', authViews.LogoutView.as_view(), {'next_page' : 'index_DS'}, name='logout_DS'),
   	path('changepassword/', PasswordChange, name='change_password'),
   	path('changepassword/done', PasswordChangeDone, name='change_password_done'),
   	path('passwordreset/', authViews.PasswordResetView.as_view(), name='password_reset'),
   	path('passwordreset/done', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
   	path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   	path('passwordreset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


	path('Delete_accoundt_DS/', Delete_accoundt_DS, name='Delete_accoundt_DS'), 
	path('pre_Delete_accoundt_DS/', pre_Delete_accoundt_DS, name='pre_Delete_accoundt_DS'), 

]