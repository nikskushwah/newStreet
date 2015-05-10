from django.shortcuts import render
from django.http import HttpResponse

from newstreet.forms import UserForm, UserProfileForm,newsform



from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from django.core import serializers

from django.core.context_processors import csrf
from models import *
# Import the built-in password reset view and password reset confirmation view.
from django.contrib.auth.views import password_reset, password_reset_confirm


from django.shortcuts import render_to_response
from newstreet.models import ContactForm
from django.template import  Context
from django import forms as forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError


def index(request):
  


    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'newstreet/index.html', context_dict)
def about(request):
   
    return render(request, 'newstreet/Untitled Document.html')


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            #if 'picture' in request.FILES:
               # profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'newstreet/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                response = tasks_json(request)
                login(request, user)
                response = tasks_json(request)
                return HttpResponseRedirect('/newstreet/main')
                response = tasks_json(request)
                
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'newstreet/login.html', {})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/newstreet/login/')
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/newstreet/')
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

# This view handles the password reset form URL /.
def reset(request):
    # Wrap the built-in password reset view and pass it the arguments
    # like the template name, email template name, subject template name
    # and the url to redirect after the password reset is initiated.
    return password_reset(request, template_name='reset.html',
        email_template_name='reset_email.html',
        subject_template_name='reset_subject.txt',
        post_reset_redirect=reverse('success'))

# This view handles password reset confirmation links. See urls.py file for the mapping.
# This view is not used here because the password reset emails with confirmation links
# cannot be sent from this application.
def reset_confirm(request, uidb64=None, token=None):
    # Wrap the built-in reset confirmation view and pass to it all the captured parameters like uidb64, token
    # and template name, url to redirect after password reset is confirmed.
    return password_reset_confirm(request, template_name='reset_confirm.html',
        uidb36=uidb36, token=token, post_reset_redirect=reverse('success'))

# This view renders a page with success message.
def success(request):
  return render(request, "success.html")


@login_required(login_url='/newstreet/login/')
def gps_news(request):
    
    response = refresh(request)
    if request.method == 'POST':
        
        
        
        news_form = newsform(data=request.POST)
        response = tasks_json(request)
        if news_form.is_valid():
            response = tasks_json(request)
            newws = news_form.save()
            return HttpResponseRedirect('/newstreet/main/gps/')
            response = tasks_json(request)
        else:
            response = tasks_json(request)
            print news_form.errors
            response = tasks_json(request)
    else:
        news_form = newsform()
        response = tasks_json(request)
    return render(request,"gps.html",{'news_form': news_form})
@login_required(login_url='/newstreet/login/')
def news(request):
    response = tasks_json(request)
    
    if request.method == 'POST':
         news_form = newsform(data=request.POST)
	 if news_form.is_valid():
             newws = news_form.save()
             response = tasks_json(request)
             return HttpResponseRedirect('/newstreet/main')
             response = tasks_json(request)
         else:
             response = tasks_json(request)
             print news_form.errors
    else:
        news_form = newsform()
        response = tasks_json(request)
    return render(request,"main.html",{'news_form': news_form})

@login_required(login_url='/newstreet/login/')
def tasks_json(request):
    with open("file.json", "w") as out:
        tasks = newws.objects.all()
        data = serializers.serialize("json", tasks)
        out.write(data)
    return HttpResponse(data, content_type='newstreet/json')
    out.write(data)
@login_required(login_url='/newstreet/login/')
def refresh(request):
    response = tasks_json(request)
    return HttpResponseRedirect('/newstreet/main/gps')


    
@login_required(login_url='/newstreet/login/')
def update_user(request):

    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return HttpResponse("invalid user_profile!")

    if request.method == "POST":
        update_user_form = UserForm(data=request.POST, instance=request.user)
        update_profile_form = UserProfileForm(data=request.POST, instance=user_profile)

        if update_user_form.is_valid() and update_profile_form.is_valid():
            user = update_user_form.save()
            profile = update_profile_form.save(commit=False)
            profile.user = user

            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']

            profile.save()

        else:
            print(update_user_form.errors, update_profile_form.errors)
    else:
        update_user_form = UserForm(instance=request.user)
        update_profile_form = UserProfileForm(instance=user_profile)

    return render(request,
            'newstreet/update_user.html',
            {'update_user_form': update_user_form, 'update_profile_form': update_profile_form}
    )


def thankyou(request):
        return render_to_response('thankyou.html')

def contactview(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/contact/thankyou/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
    

        recipients = ['anamhabeeb11@gmail.com']
   
        from django.core.mail import send_mail
        send_mail(subject, message, sender, recipients)

        return HttpResponseRedirect('/contact/thankyou') # Redirect after POST



    
    

    

