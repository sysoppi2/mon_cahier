from django.shortcuts import render

# Create your views here:

def post_list(request):
	return render(request, 'arriere_boutique/post_list.html', {})