
from django .http import HttpResponse, JsonResponse

def home_page(request):
    print("home pages requested")
    friends=[
        'Raj',
        'Meet',
        'Mahekraj'
    ]
    return JsonResponse(friends,safe=False)