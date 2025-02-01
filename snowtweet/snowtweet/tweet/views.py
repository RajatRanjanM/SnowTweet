from django.shortcuts import get_object_or_404, redirect, render
from .models import Tweet, TweetForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    tweets = Tweet.objects.all().order_by('-created_at')  # Retrieve all tweets, ordered by creation time
    return render(request, 'index.html', {'tweets': tweets})
def tweet_list(request) :
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets' : tweets})
@csrf_exempt

@login_required(login_url='/tweet/login/')  # Redirect to /tweet/login if not authenticated
def create_tweet(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Tweet.objects.create(text=text, user=request.user)  # Create a new Tweet
            return redirect('index')
    return redirect('index')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:  # Validate password match
            if User.objects.filter(username=username).exists():
                # Username already exists
                return render(request, 'register.html', {'error': 'Username already exists'})
            else:
                # Create new user
                user = User.objects.create_user(username=username, password=password)
                user.save()
                # Automatically log in the new user
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')
        else:
            # Passwords do not match
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    
    return render(request, 'register.html')
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the index page after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

@csrf_exempt  
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == 'POST':
        tweet.delete()
        return redirect('index')
    return render(request, 'index.html')

def custom_logout(request):
    logout(request)
    return redirect('index')