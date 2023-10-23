from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import requests

logger = logging.getLogger(__name__)

@csrf_exempt
def registration_proxy(request):
    if request.method == "POST":
        post_data = json.loads(request.body.decode('utf-8'))
        logger.info("POST data: %s", post_data)

        external_api_url = "https://www.comet.com/api/auth/new"

        response = requests.post(external_api_url, data=post_data)

        # Forward the status code and content from the external service to your client
        return JsonResponse(response.json(), status=response.status_code)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
