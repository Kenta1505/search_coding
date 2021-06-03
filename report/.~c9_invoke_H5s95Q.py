from django.shortcuts import render
from django.http import HttpResponse
from app2.forms import ReportForm
from report.samurai_search import Searching_samurai
# Create your views here.

def index(request):
    if request.method=='POST':
        context={'search':request.POST['search'],}
        return render(request, 'reportForm.html', context)
    else:
        f=ReportFrom({'title':'レポートタイトル',
            'body':'Hello. Django! Form',
            }
        )
        r
