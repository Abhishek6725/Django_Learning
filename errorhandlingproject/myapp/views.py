from django.http import HttpResponse
from django.shortcuts import render

# Home Page
def home(request):
    return HttpResponse("✅ Welcome to Django Error Handling Example!")


def divide_numbers(request):
    try:
        a = int(request.GET.get("a", 10))
        b = int(request.GET.get("b", 0))  
        result = a / b
        return HttpResponse(f"Result is: {result}")
    except ZeroDivisionError:
        return HttpResponse("❌ Error: Division by zero not allowed!")
    except Exception as e:
        return HttpResponse(f"⚠️ Unexpected Error: {str(e)}")

# Custom 404 Page
def custom_404(request, exception):
    return render(request, "404.html", status=404)

# Custom 500 Page
def custom_500(request):
    return render(request, "500.html", status=500)
