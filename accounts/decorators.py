from django.http import HttpResponse
from django.shortcuts import redirect



def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func 

def allowed_users(allowed_roles =[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        role = request.user.role
        if role =='customer':
            return redirect('client_index')
        elif role in ['admin','user1','moderator','only_razlovka','razlovka','user_accessuar']:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to view this page.')
    return wrapper_func

def customer_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        role = request.user.role
        if role =='customer':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to view this page.')
    return wrapper_func

def moderator_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        role = request.user.role
        if role =='moderator':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to view this page.')
    return wrapper_func