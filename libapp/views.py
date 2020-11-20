from django.shortcuts import render
from libapp.models import Author
from libapp.models import Book
# Create your views here.
from django.http import HttpResponse

def aboutus(request):
	query_results_author = Author.objects.all()
	query_results_book=Book.objects.all()
	context= {'query_results_author': query_results_author,
	'query_results_book':query_results_book
	}

	return render(request,"about_us.html",context)