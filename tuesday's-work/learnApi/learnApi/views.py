from django.http import HttpResponse,JsonResponse

def home_page(req):
    
    friendlist = [
        'saurav joshi',
        'gourav soni',
        'zeeshan ahmad',
        'sadique hussain'
    ]
    
    return JsonResponse(friendlist,safe=False)