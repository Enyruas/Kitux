# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from productRead import Product,getFarnellRequestUrl, getProductInfo
import requests
from models import useraccount

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html", {'wrongtry': 0,})
    elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        query = useraccount.objects.filter(username=username)
        if query.count() == 0:
            newuser = useraccount(username=username, password=password)
            newuser.save()
            response = HttpResponse()
            response.set_cookie('username', username)
            response.write("<script>window.location='/robots/search/'</script>")
            return response
        elif query.count() > 0:
            return render(request, "signup.html", {'wrongtry': 1,})

def tests(request):
    return render(request, "tests.html")

def signout(request):
    response = HttpResponseRedirect("/robots/search")
#    response.delete_cookie('username')
#    return response


def search(request, keyword='No values', page='0'):
#    if request.method == 'GET':  
#        page = request.GET.get("page", 'No values')
        sign = request.POST.get("sign", 0)
        if sign == "signin":
            username = request.POST.get("username")
            query = useraccount.objects.filter(username=username)
            if query.count() == 0:
                username = -1
            elif query.count() and query[0].password != request.POST.get("password"):
                username = -1

        elif sign == "signout":
            username = 0
        elif sign == 0:
            username = request.COOKIES.get('username', 0)

        if page == '0':
            response = render(request, 'search.html', 
                {'keywod': 0,
                'username': username},
                )
        else:
            url = getFarnellRequestUrl('keyword', keyword, (int(page)-1)*10)
            res = requests.get(url);
            text = res.json()

            result = getProductInfo(text)
            products = result.get('products', [])
            numberOfResults = result['numberOfResults']
            if len(products) == 0 and numberOfResults > 0:
                raise Http404

            numberPages = (numberOfResults+9)/10
            left = max(1, min(int(page)-5, max(1, numberPages - 9)))
            right = min(numberPages, max(int(page)+4, min(numberPages, 10)))
        
            response = render(request, "search.html",
                {'products': products,
                'keyword': keyword,
                'numberOfResults': numberOfResults,
                'pageRange': range(left, right+1),
                'page': int(page),
                'numberPages': numberPages,
                'left': left,
                'right': right,
                'username': username,}
                )
        
        if sign == "signin" and username:
            response.set_cookie('username', username)
        elif sign == "signout":
            response.delete_cookie('username')
        return response


