from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


# def january(request):
#     return HttpResponse('Eat no meat for the entire month!')


# def february(request):
#     return HttpResponse('Walk for at least 20 minutes every day!')


# def march(request):
#     return HttpResponse('Learn Django for at least 20 minutes every day!')

monthly_challenges = {
    'january' : 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Eat no meat for the entire month!',
    'may': 'Walk for at least 20 minutes every day!',
    'june': 'Eat no meat for the entire month!',
    'july': 'Walk for at least 20 minutes every day!',
    'august': 'Learn Django for at least 20 minutes every day!',
    'september': 'Walk for at least 20 minutes every day!',
    'october': 'Learn Django for at least 20 minutes every day!',
    'november': 'Walk for at least 20 minutes every day!',
    'december' : 'Learn Django for at least 20 minutes every day!',
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/month
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound('This month is not supported')
    return HttpResponse(challenge_text)
