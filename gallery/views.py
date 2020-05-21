from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def gallery_of_day(request):
    date = dt.date.today()
    return render(request, 'gallery/today-gallery.html')

def past_days_gallery(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(gallery_today)

    gallery = Article.days_gallery(date)
    return render(request, 'gallery/past-gallery.html', {"date": date,"gallery":gallery})
    
def gallery_today(request):
    date = dt.date.today()
    gallery = Article.todays_gallery()
    return render(request, 'gallery/today-gallery.html', {"date": date,"gallery":gallery})