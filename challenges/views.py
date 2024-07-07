from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.


monthly_challenge={
    "january":"Walk for 15 minutes",
    "february":"Learn django for 30 mins",
    "march":"do 1 leetcode problem",
    "april":"Learn django for 30 mins",
    "may":"Walk for 15 minutes",
    "june":"do 1 leetcode problem",
    "july":"do 1 leetcode problem",
    "august":"Learn django for 30 mins",
    "september":"Walk for 15 minutes",
    "october":"do 1 leetcode problem",
    "november":"Learn django for 30 mins",
    "december":"Walk for 15 minutes"
}
def index(request):
    list_items=""
    months=list(monthly_challenge.keys())
    return render(request,"challenges/index.html",{
        "months":months
    })

def monthly_challenge_by_number(request,month):
    months=list(monthly_challenge.keys())#accessing only the keys and converting into list
    if month >len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month=months[month-1]
    redirect_path=reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)#redirecting that to challenges 
def monthly_challenges(request,month):
    try:
        challenge_text=monthly_challenge[month]
        return render(request,"challenges/challenge.html",
                      {"text":challenge_text,
                       "month_name":month.capitalize()
                        })
    except:
        raise Http404()