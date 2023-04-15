from django.contrib import admin


from post_DS.models import (Post_DS, 
                        Tag_DS, 
                        Follow_DS, 
                        Stream_DS, 
                        Likes_DS, 
                        Relevancy_DS,
                        Conciseness_DS,
                        Experience_chart,
                        
                        )
# models for post
admin.site.register(Tag_DS)
admin.site.register(Post_DS)
admin.site.register(Experience_chart)
admin.site.register(Follow_DS)
admin.site.register(Stream_DS)
admin.site.register(Likes_DS)
admin.site.register(Relevancy_DS)
admin.site.register(Conciseness_DS)

