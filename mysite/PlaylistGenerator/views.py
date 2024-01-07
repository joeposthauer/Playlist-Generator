from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from . import credentials

import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
#this is a random change

# View for when a user enters site- needs to authenticate
def index(request):
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

# View for when a user authenticates- choosing parameters
def parameters(request):
    return HttpResponse("hello")
