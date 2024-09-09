from django.shortcuts import render

# Create your views here.
def set(request):
    data = render(request,'set.html')
    data.set_cookie('name','priya',max_age=5*24*60*60,httponly=True,secure=True)
    data.set_cookie('age','27',max_age=4*24*60*60,httponly=True,secure=True)
    data.set_cookie('city','bhopal',max_age=3*24*60*60,httponly=True,secure=True)
    return data

def get(request):
    print(request.COOKIES)
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    city = request.COOKIES['city']

    data = {
        'name':name,
        'age':age,
        'city':city,
    }
    return render(request,'get.html',data)