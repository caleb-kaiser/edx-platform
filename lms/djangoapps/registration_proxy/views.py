from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import requests
import json

logger = logging.getLogger(__name__)

@csrf_exempt
def registration_proxy(request):
    if request.method == "POST":
        post_data = json.loads(request.body.decode('utf-8'))

        headers = {
            'Content-type':'application/json', 
            'Accept':'application/json'
        }

        external_api_url = "https://www.comet.com/api/auth/new"

        response = requests.post(external_api_url, json=post_data, headers=headers)

        # Forward the status code and content from the external service to your client
        return JsonResponse(response.json(), status=response.status_code)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
