from .models import MessageFeedBack 
from django.utils.timezone import now
from django.db.models import Count
from config.settings import MEDIA_ROOT

def get_user_messages(request):
    if request.user.is_authenticated:
        msg = MessageFeedBack.objects.filter(receiver =request.user, accepted = False).values('sender__username','sender__userprofile__profile_picture','msg_type').annotate(msg_count=Count('msg_type'))
        today = now()
        err_count = 0
        simple_count = 0
        message_list = list(msg)
        for item in message_list:    
            if item['msg_type'] == 1:
                err_count += item['msg_count']
            else:
                simple_count +=item['msg_count']
        total_count =err_count + simple_count
        return {'messages':msg,'count':total_count,'errors_count':err_count,'simple_count':simple_count,'today':today,}
    else:
        return {}

