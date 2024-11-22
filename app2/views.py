from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def test2(request):
    return HttpResponse('Testing the test1')
 
def test3(request):
    return HttpResponse('<h1> This is testing of test3 using H1 tag </h1>')

def test4(request):
    return HttpResponse('<marquee> This is testing of test4 using marquee tag </marquee>')

def test5(request):
    return HttpResponse('''<h1>Name: Chaicode</h1>
                        <i>Web: <a href="https://chaicode.com/">Chaicode</a></i><br>
                        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTD6SSM2SX8Lvvp4POc8I4hmT2AOx29ZudYQQ&s'>''')