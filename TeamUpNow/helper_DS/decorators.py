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
			return redirect('index')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def unauthenticated_group(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('index')
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



def employer_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'Employer':
            return view_func(request, *args, **kwargs)

        else:
            return redirect('index')
            
    return wrapper_function


def candidate_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'Candidate':
            return view_func(request, *args, **kwargs)

        else:
            return redirect('index')
            
    return wrapper_function



def recruiter_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'Recruiter':
            return view_func(request, *args, **kwargs)

        else:
            return redirect('index')
            
    return wrapper_function
