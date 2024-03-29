from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse

from . import credentials
from .forms import ParamsForm

import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

# View for when a user enters site- needs to authenticate
def landing(request):
    args = {}
    # Create a SpotifyOAuth object
    sp_oauth = SpotifyOAuth(client_id=credentials.client_ID, client_secret=credentials.client_SECRET, redirect_uri=credentials.redirect_URI, scope = credentials.scope)

    # Print the sp_oauth object to the console
    print("\n\nSP_OAuth Object:" ,sp_oauth, "\n\n")

    # Redirect the user to the Spotify login page
    # Get the authorization URL
    url = sp_oauth.get_authorize_url()
    # Print the authorization url to the console
    print(url)
    args['url'] = url

    access_token = request.session.get("access_token")
    print('\n\n ACCESS TOKEN: ', access_token, '\n\n')
    
    # Redirect the user to the Spotify login page
    return render(request, "landing.html", args)


# View for reauthentication after redirect
def callback(request):
    # Create a SpotifyOAuth object
    sp_oauth = SpotifyOAuth(client_id=credentials.client_ID, client_secret=credentials.client_SECRET, redirect_uri=credentials.redirect_URI, scope=credentials.scope)

    # Get the authorization code from the query parameters
    code = request.GET.get("code")

    # Request an access token using the authorization code
    token_info = sp_oauth.get_access_token(code)

    # Extract the access token
    access_token = token_info["access_token"]

    # Store the access token in a secure way (e.g. in a session or database)
    request.session["access_token"] = access_token

    # Redirect the user to the top tracks page
    return HttpResponseRedirect("/PlaylistGenerator/parameters/")


# View for when a user authenticates- choosing parameters
def parameters(request):
    args = {}

    token = request.session.get("access_token")

    sp = spotipy.Spotify(auth=token)

    response = sp.me()
    if response is not None:
        print("The access token is valid.\n\n")
    else:
        print("The access token is invalid or has expired.\n\n")

    # if this is a POST request we need to process the form data
    print("right before post conditional")
    

    # if a GET (or any other method) we'll create a blank form
   
    form = ParamsForm()                              #only ever enters this case

    args['form'] = form
    return render(request, "parameters.html", args)

# View for calculating parameters for playlist
def calculate(request, *args):

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ParamsForm(request.POST)
        # check whether it's valid:
        print("right before valid conditional")
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.cleaned_data)
            print(form.cleaned_data['genres'])
            # url = reverse("/calculate/", form={'data': form})
            return HttpResponse('thanks')

    print(args)
    return render(request, "calculate.html")


