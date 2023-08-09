from .models import UserProfile

def user_profile(request):
    user = request.user
    if user.is_authenticated:
        user_profile = UserProfile.objects.get(user =user)
    else:
        user_profile = None
    return {'user_profile':user_profile}

ROLE_CHOICES ={
    1:'moderator',
    2:'user1',
    3:'user2',
    4:'only_razlovka'
}

def get_user_role(request):
    if request.user.is_authenticated:
        user_role =request.user.role
        if user_role ==None:
            user_role='nan'
        else:
            user_role =ROLE_CHOICES[user_role]
    else:
        user_role ='nan'
    return {'user_role':str(user_role)}