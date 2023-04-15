from django.urls import path


from post_DS.views import ( 
						index_DS, 

						index_DS_CreateProject,  
						

						PostDetails_DS, 

						PostDetails_category_TechSKILLS_DS,
						

						PostDetails_category_SOFT_SKILLS_DS, 

						PostDetails_category_ALL_SKILLS_DS, 

						PostDetails_category_PROBLEM_SOLVING_APROACH_DS, 

						NewPost_DS, 

						EditPost_DS,

						EditPost_DS, 

						PostDetails_reqeustTalent_DS, 

						comment_DS, 

						EditExperience_chart_DS, 

						DeleteExperience_chart_DS, 

						pre_DeleteExperience_chart_DS, 

						DeletePost_DS, 

						pre_DeletePost_DS, 



						tags_DS, 

						conciseness_DS,
						relevancy_DS,

						favorite_DS, 

						Experience_chart_DS,
						
						Experience_chart_FirstProject_DS,
						
						
						)


urlpatterns = [ 

	path('index_DS/', index_DS, name='index_DS'), 

	path('index_DS_CreateProject/', index_DS_CreateProject, name='index_DS_CreateProject'), 
	
   	path('NewPost_DS/', NewPost_DS, name='NewPost_DS'), 
	
	path('<uuid:event_id>/EditPost_DS', EditPost_DS, name='EditPost_DS'), 

   	# path('<uuid:post_id>', PostDetails_DS, name='PostDetails_DS'),
	path('<uuid:post_id>/PostDetails_DS', PostDetails_DS, name='PostDetails_DS'),  

	# path('<uuid:post_id>/', Experience_chart_Details_DS, name='Experience_chart_Details_DS'),
	path('<uuid:post_id>/PostDetails_category_SOFT_SKILLS_DS', PostDetails_category_SOFT_SKILLS_DS, name='PostDetails_category_SOFT_SKILLS_DS'), 
	
	path('<uuid:post_id>/PostDetails_category_ALL_SKILLS_DS', PostDetails_category_ALL_SKILLS_DS, name='PostDetails_category_ALL_SKILLS_DS'), 
	
	path('<uuid:post_id>/PostDetails_category_TechSKILLS_DS', PostDetails_category_TechSKILLS_DS, name='PostDetails_category_TechSKILLS_DS'), 
	
	path('<uuid:post_id>/PostDetails_category_PROBLEM_SOLVING_APROACH_DS', PostDetails_category_PROBLEM_SOLVING_APROACH_DS, name='PostDetails_category_PROBLEM_SOLVING_APROACH_DS'), 

   	path('<uuid:post_id>/comment_DS', comment_DS, name='comment_DS'), 
   

   

	path('<uuid:post_id>/conciseness_DS', conciseness_DS, name='conciseness_DS'),
	path('<uuid:post_id>/relevancy_DS', relevancy_DS, name='relevancy_DS'),
	

   	path('<uuid:post_id>/favorite_DS', favorite_DS, name='postfavorite_DS'),
   	path('tags_DS/<slug:tag_slug>', tags_DS, name='tags_DS'),


	path('Experience_chart_DS/', Experience_chart_DS, name='Experience_chart_DS'), 

	path('Experience_chart_FirstProject_DS/', Experience_chart_FirstProject_DS, name='Experience_chart_FirstProject_DS'), 
	
	path('<uuid:post_id>/PostDetails_reqeustTalent_DS', PostDetails_reqeustTalent_DS, name='PostDetails_reqeustTalent_DS'), 
	
	path('<uuid:event_id>/EditPost_DS', EditPost_DS, name='EditPost_DS'), 
	
	path('<uuid:event_id>/pre_DeletePost_DS', pre_DeletePost_DS, name='pre_DeletePost_DS'), 
	
	path('<uuid:event_id>/DeletePost_DS', DeletePost_DS, name='DeletePost_DS'), 
	
	path('<uuid:event_id>/EditExperience_chart_DS', EditExperience_chart_DS, name='EditExperience_chart_DS'), 
	
	path('<uuid:event_id>/pre_DeleteExperience_chart_DS', pre_DeleteExperience_chart_DS, name='pre_DeleteExperience_chart_DS'), 
	
	path('<uuid:event_id>/DeleteExperience_chart_DS', DeleteExperience_chart_DS, name='DeleteExperience_chart_DS'), 


]
