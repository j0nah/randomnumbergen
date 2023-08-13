from randomnumbers.models import RandomNumber
from django.http import JsonResponse

def random_number_request(request):
    rn = RandomNumber.objects.create()
    return JsonResponse({"id": rn.id})

def random_number_status(request, id):
    rn = RandomNumber.objects.get(id=id)
    response = {
        "id": rn.id,
        "status": "in_progress",
        "number" : None
    }

    if rn.number:
        response["status"] = "complete"
        response["number"] = rn.number

    return JsonResponse(response)