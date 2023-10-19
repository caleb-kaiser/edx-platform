from django.http import JsonResponse
import requests

def registration_proxy(request):
    if request.method == "POST":
        external_api_url = "https://www.comet.com/api/auth/new"

        response = requests.post(external_api_url, data=request.POST)

        # Forward the status code and content from the external service to your client
        return JsonResponse(response.json(), status=response.status_code)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
