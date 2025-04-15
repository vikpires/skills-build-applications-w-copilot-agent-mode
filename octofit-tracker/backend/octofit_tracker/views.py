from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "codespace_url": "https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev",
        "localhost_url": "http://localhost:8000"
    })