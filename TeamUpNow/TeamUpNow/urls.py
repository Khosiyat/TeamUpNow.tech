"""TeamUpNow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]



from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from TeamUpNow.views import teamUpNowTech_login, teamUpNowTech


########################## PROFILE EMPLOYER
from authy_DS.views import ( 
                        follow_DS,

                        UserProfile_DS,
                        
                        UserProfile_category_DAYS_DS,

                        UserProfile_category_MONTHS_DS,
                        
                        UserProfile_category_YEARS_DS,
                        
                        UserProfile_category_WORK_HISTORY_DS,
                        
                        UserProfile_category_ExperienceList_DS,
                        
                        UserProfile_category_EvaluationList_DS,
                        
                        UserProfile_notifications_DS_evaluated,
                        
                        UserProfile_notifications_DS_requested,
                        
                        UserProfile_notifications_DS_scored,
                        
                        UserProfile_notifications_DS_teamedUp,
                        
                        FriendProfile_notifications_DS_evaluated,
                        
                        FriendProfile_notifications_DS_requested,
                        
                        FriendProfile_notifications_DS_scored,
                        
                        FriendProfile_notifications_DS_teamedUp,
                        
                        )
   
 

urlpatterns = [
    # #MAIN FOLDER URL ROUTES
    # ####################### admin
    path('admin/', admin.site.urls),

	
	path('teamUpNowTech_login/', teamUpNowTech_login, name="teamUpNowTech_login"),

    path('teamUpNowTech/', teamUpNowTech, name="teamUpNowTech"),


    # # ####################### candidate
    # path('post_candidate/', include('post_candidate.urls')),
    # path('user/', include('authy_candidate.urls')),
    # path('direct_candidate/', include('direct_candidate.urls')),
    # path('stories_candidate/', include('stories_candidate.urls')),
    # path('notifications_candidate/', include('notifications_candidate.urls')),

    # ####################### stories
    path('stories_employer/', include('stories_employer.urls')),

    # ####################### DS
    path('post_DS/', include('post_DS.urls')),
    path('user/', include('authy_DS.urls')),
    path('direct_DS/', include('direct_DS.urls')),
    path('notifications_DS/', include('notifications_DS.urls')),


    # ####################### evaluator
    # path('post_evaluator/', include('post_evaluator.urls')),
    # path('user/', include('authy_evaluator.urls')),
    # path('direct_evaluator/', include('direct_evaluator.urls')),
    # path('stories_evaluator/', include('stories_evaluator.urls')),
    # path('notifications_evaluator/', include('notifications_evaluator.urls')),


    # #PROFILE
    # ########################## PROFILE CANDIDATE
    # ######## PROFILE CATEGORY
    # path('<username>/UserProfile_category_EDUCATION_candidate', UserProfile_category_EDUCATION_candidate, name='UserProfile_category_EDUCATION_candidate'),
    # path('<username>/UserProfile_category_TECH_STACK_candidate', UserProfile_category_TECH_STACK_candidate, name='UserProfile_category_TECH_STACK_candidate'),
    # path('<username>/UserProfile_category_WORK_HISTORY_candidate', UserProfile_category_WORK_HISTORY_candidate, name='UserProfile_category_WORK_HISTORY_candidate'),
    # path('<username>/UserProfile_category_PROJECTS_candidate', UserProfile_category_PROJECTS_candidate, name='UserProfile_category_PROJECTS_candidate'),
    # ######## PROFILE DASHBOARD UNITS
    # path('<username>/', UserProfile_candidate, name='profile_candidate'),
    # path('<username>/UserProfile_dashboard_candidate', UserProfile_dashboard_candidate, name='UserProfile_dashboard_candidate'),
    # path('<username>/saved_candidate', UserProfile_candidate, name='profilefavorites_candidate'),
    # path('<username>/chart_candidate', UserProfile_candidate, name='profile_chart_candidate'),

    # path('<username>/follow_candidate/<option>', follow_candidate, name='follow_candidate'),


    ########################## PROFILE EMPLOYER
    ######## PROFILE CATEGORY
    
    path('<username>/UserProfile_category_DAYS_DS', UserProfile_category_DAYS_DS, name='UserProfile_category_DAYS_DS'), 

    path('<username>/UserProfile_category_MONTHS_DS', UserProfile_category_MONTHS_DS, name='UserProfile_category_MONTHS_DS'), 

    path('<username>/UserProfile_category_YEARS_DS', UserProfile_category_YEARS_DS, name='UserProfile_category_YEARS_DS'), 

    path('<username>/UserProfile_category_WORK_HISTORY_DS', UserProfile_category_WORK_HISTORY_DS, name='UserProfile_category_WORK_HISTORY_DS'), 

    path('<username>/UserProfile_category_ExperienceList_DS', UserProfile_category_ExperienceList_DS, name='UserProfile_category_ExperienceList_DS'), 

    path('<username>/UserProfile_category_EvaluationList_DS', UserProfile_category_EvaluationList_DS, name='UserProfile_category_EvaluationList_DS'), 



    path('<username>/UserProfile_notifications_DS_evaluated', UserProfile_notifications_DS_evaluated, name='UserProfile_notifications_DS_evaluated'), 

    path('<username>/UserProfile_notifications_DS_requested', UserProfile_notifications_DS_requested, name='UserProfile_notifications_DS_requested'), 

    path('<username>/UserProfile_notifications_DS_scored', UserProfile_notifications_DS_scored, name='UserProfile_notifications_DS_scored'), 

    path('<username>/UserProfile_notifications_DS_teamedUp', UserProfile_notifications_DS_teamedUp, name='UserProfile_notifications_DS_teamedUp'), 

    
    path('<username>/FriendProfile_notifications_DS_evaluated', FriendProfile_notifications_DS_evaluated, name='FriendProfile_notifications_DS_evaluated'), 

    path('<username>/FriendProfile_notifications_DS_requested', FriendProfile_notifications_DS_requested, name='FriendProfile_notifications_DS_requested'), 
 
    path('<username>/FriendProfile_notifications_DS_scored', FriendProfile_notifications_DS_scored, name='FriendProfile_notifications_DS_scored'), 
    
    path('<username>/FriendProfile_notifications_DS_teamedUp', FriendProfile_notifications_DS_teamedUp, name='FriendProfile_notifications_DS_teamedUp'), 



    ######## PROFILE DASHBOARD UNITS | profile_employer
    path('<username>/UserProfile_DS', UserProfile_DS, name='UserProfile_DS'),


    # path('<username>/UserProfile_dashboard_DS', UserProfile_dashboard_DS, name='UserProfile_dashboard_DS'), 
    

    path('<username>/saved_DS', UserProfile_DS, name='profilefavorites_DS'),
    path('<username>/chart_DS', UserProfile_DS, name='profile_chart_DS'),
    path('<username>/follow_DS/<option>', follow_DS, name='follow_DS'),

    # ########################## PROFILE EVALUATOR
    # ######## PROFILE CATEGORY
    # path('<username>/UserProfile_category_EDUCATION_evaluator', UserProfile_category_EDUCATION_evaluator, name='UserProfile_category_EDUCATION_evaluator'),
    # path('<username>/UserProfile_category_TECH_STACK_evaluator', UserProfile_category_TECH_STACK_evaluator, name='UserProfile_category_TECH_STACK_evaluator'),
    # path('<username>/UserProfile_category_WORK_HISTORY_evaluator', UserProfile_category_WORK_HISTORY_evaluator, name='UserProfile_category_WORK_HISTORY_evaluator'),
    # path('<username>/UserProfile_category_PROJECTS_evaluator', UserProfile_category_PROJECTS_evaluator, name='UserProfile_category_PROJECTS_evaluator'),
    # ######## PROFILE DASHBOARD UNITS
    # path('<username>/', UserProfile_evaluator, name='profile_evaluator'),
    # path('<username>/UserProfile_dashboard_evaluator', UserProfile_dashboard_evaluator, name='UserProfile_dashboard_evaluator'),
    # path('<username>/saved_evaluator', UserProfile_evaluator, name='profilefavorites_evaluator'),
    # path('<username>/chart_evaluator', UserProfile_evaluator, name='profile_chart_evaluator'),

    # path('<username>/follow_evaluator/<option>', follow_evaluator, name='follow_evaluator'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)