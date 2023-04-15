from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from .models import *

def admin_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = Group.objects.get(user = request.user)
        if group.name == 'admin_owner':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_func 


# ##############################################################################

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('index_DS')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def unauthenticated_group(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('index_DS')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func


# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             print(allowed_roles)
#             return view_func(request, *args, **kwargs)
            
#         return wrapper_func
#     return decorator

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print(allowed_roles)
                
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
                
            else:
                return HttpResponse('You are not authorized to view this page')
                # return HttpResponse(allowed_roles)
                
        print(allowed_roles)
        return wrapper_func
        
        
    return decorator


# dataScientist
# webDeveloper
# mobileDeveloper
# gameDeveloper

def dataScientist_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'dataScientist':
            return view_func(request, *args, **kwargs)

        else:
            return redirect('index_DS')
            
    return wrapper_function


def webDeveloper_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'webDeveloper':
            return view_func(request, *args, **kwargs)

        else:
            return redirect('index_DS')
            
    return wrapper_function



def mobileDeveloper_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'mobileDeveloper':
            return view_func(request, *args, **kwargs)

        else:
            return redirect('index_DS')
            
    return wrapper_function


def gameDeveloper_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'gameDeveloper':
            return view_func(request, *args, **kwargs)

        else:
            return redirect('index_DS')
            
    return wrapper_function
