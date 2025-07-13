# Answer for the first sections

# from django.http import HttpResponse
#
# # View for home page
# def home(request):
#     return HttpResponse("""
#         <h1>Welcome to the Greeting App!</h1>
#         <p>To get a personalized greeting, go to: /greet/yourname/</p>
#         <p>Example: <a href="/greet/Yael/">/greet/Yael/</a></p>
#     """)
#
# # View for greeting page with a name
# def greet(request, name):
#     return HttpResponse(f"<h1>Hello, {name.capitalize()}! 👋</h1><p>Nice to see you!</p>")


# Answer for the section 5
from django.shortcuts import render

def home(request):
    return render(request, 'greeting_app/home.html')

# def greet(request, name):
#     return render(request, 'greeting_app/greet.html', {'name': name})

def greet(request, name=None):
    if not name:
        name = request.GET.get("name", "Guest")
    return render(request, 'greeting_app/greet.html', {'name': name})