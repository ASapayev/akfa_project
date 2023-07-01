from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User,UserProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance,**kwargs):
    if not UserProfile.objects.filter(user =instance).exists():
        user_profile = UserProfile(user =instance,profile_picture='assets/images/faces/face2.jpg')
        user_profile.save()
    
    