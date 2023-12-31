from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


# def january(request):
#     return HttpResponse('Eat no meat for the entire month!')


# def february(request):
#     return HttpResponse('Walk for at least 20 minutes every day!')


# def march(request):
#     return HttpResponse('Learn Django for at least 20 minutes every day!')

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
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
    'december': None,
}


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     # /challenges/month
    #     month_path = reverse("month-challenge", args=[month])
    #     # absolute_month_path = request.build_absolute_uri(month_path) #localhost:8000/challenges/month
    #     list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    #     response_data = f'<ul>{list_items}</ul>'
    # return HttpResponse(response_data)
    return render(request, 'challenges/index.html', {
        'months': months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    redirect_path = reverse(
        'month-challenge', args=[redirect_month])  # /challenge/month
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month': month
        })
    except:
        raise Http404()
        # return HttpResponseNotFound('This month is not supported')
    # return HttpResponse(challenge_text)
