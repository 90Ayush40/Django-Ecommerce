from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm



def home_page(request):
	# print(request.session.get("first_name", "Unknown"))
	context = {
		"title": "Thankyou World!",
		"content": "Welcome to the Home Page",
		"premium_content": "YYYYYEEEEEEEAAAAAAHHHHHHH"
	}
	return render(request, "home_page.html", context)


def about_page(request):
	context = {
		"title": "About World!",
		"content": "Welcome to the About Page"
	}

	return render(request, "home_page.html", context)


def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title": "Contact World!",
		"content": "Welcome to the Contact Page",
		"form": contact_form

	}

	if contact_form. is_valid():
		print(contact_form.cleaned_data)

	# if request.method == 'POST':
	# 	# print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
   		


	return render(request, "contact/view.html", context)


def home_page_old(request):

	html_="""
			<!doctype html>
				<html lang="en">
				  <head>
				    <!-- Required meta tags -->
				    <meta charset="utf-8">
				    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

				    <!-- Bootstrap CSS -->
				    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
                    
				    <title>Hello, world!</title>

				  </head>
				  <body>
				  <div class="text-center">
				    <h1>Hello, world! we are working.</h1>
                   </div>
				    <!-- Optional JavaScript -->
				    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
				    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
				    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
				    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
				  </body>
				</html>
            """
	return HttpResponse(html_)