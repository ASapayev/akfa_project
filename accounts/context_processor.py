from .models import UserProfile

def user_profile(request):
    user = request.user
    if user.is_authenticated:
        user_profile = UserProfile.objects.get(user =user)
    else:
        user_profile = None
    return {'user_profile':user_profile}