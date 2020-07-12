from django.shortcuts import render
from corona.models import patient
from corona.models import feedbackform
# Create your views here.
def welcome(request):

    return render(request,'welcome.html');
def registration(request):

    return render(request,'registration.html',{"data":[]})
def home(request):
    n=request.GET['name'];
    p = request.GET['password'];
    g = request.GET['gender'];
    a= request.GET['age'];
    b= request.GET['bloodgroup'];
    e= request.GET['email'];
    info=patient(name=n,password=p,age=a,bloodgroup=b,email=e,gender=g);
    info.save();
    return render(request, 'registration.html',{"data":[1],"name":n,"password":p})
def ownhome(request):
    employ = patient.objects.all();
    n=request.GET['name'];
    p=request.GET['password'];
    s=0
    for f in employ:
        if(f.name==n and  f.password==p):
            s=f;
            break;
    else:
        return render(request, 'login.html', {"data":[1]})
    return render(request, 'home.html',{"s":s});

def give(request):

    p=request.GET['password'];

    return render(request, 'form.html',{"pass":p});
def insert(request):
  try:
    print(request.GET["symptoms1"]);
    sym1=request.GET.getlist('symptoms1') #to get all values of checkbox use list
    sym2 = request.GET.getlist('symptoms2')

    if (sym1 and sym2):
        if (type(sym1) is not str or type(sym2) is not str):
            if (type(sym1) == str):
                sym1 = [sym1];
            elif (type(sym2) == str):
                sym2 = [sym2];
            if (len(sym1) > 1 or len(sym2) > 3):

                chance = "your sugg to be affected in coronavirus is 80% to 100%!!!!"

                sugg="suggetion:alert!stay at home and call immidiately 1800313444222/03323412600 on any of this no"
            elif (len(sym2) == 2):

                chance = "your sugg to be affected in coronavirus is 30% to 40%!!!!"
                sugg="Go to a doctor "
            else:

                chance = "your sugg to be affected in coronavirus is 50% to 60%!!!!"
                sugg="call on 911123978046 this no "
        else:

            chance = "your sugg to be affected in coronavirus is 10% to 20%!!!!"
            sugg="you are safe!you are safe :) keep update your situation in our app"
    elif (sym1):
        if (len(sym1) == 3):

            chance = "your sugg to be affected in coronavirus is 50% to 70%!!!!"
            sugg="Go to a doctor "
        else:

            chance = "your sugg to be affected in coronavirus is 10% to 20%!!!!"
            sugg="you are safe :) keep update your situation in our app"
    elif (sym2):
        if (len(sym2) == 5):

            chance = "your sugg to be affected in coronavirus is 50% to 70%!!!!"
            sugg="Go to a doctor "
        else:

            chance = "your sugg to be affected in coronavirus is 10% to 20%!!!!"
            sugg="you are safe :) keep update your situation in our app"
    else:

        chance = "your sugg to be affected in coronavirus is 10% to 20%!!!!"
        sugg="you are safe :) keep update your situation in our app"
  except:
     chance = "your sugg to be affected in coronavirus is 10% to 20%!!!!"
     sugg = "you are safe :) keep update your situation in our app"


  obj = patient.objects.get(password=request.GET["password"])
  obj.chance=chance;
  obj.sugg=sugg;
  obj.save();




  return render(request,'home.html',{"s":obj})
def login(request):
    return render(request, 'login.html', {"data":[]})

def feed(request):
    return render(request, 'feedback.html', {"data": []})

def save(request):
    info = feedbackform(feed=request.GET['feedback']);
    info.save();
    return render(request, 'feedback.html', {"data": [2]})
