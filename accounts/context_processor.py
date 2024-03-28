from .models import UserProfile

def user_profile(request):
    user = request.user
    if user.is_authenticated:
        user_profile = UserProfile.objects.get(user =user)
    else:
        user_profile = None
    return {'user_profile':user_profile}



def get_user_role(request):
    if request.user.is_authenticated:
        user_role =request.user.role
        if user_role ==None:
            user_role='nan'
    else:
        user_role ='nan'
    return {'user_role':str(user_role)}