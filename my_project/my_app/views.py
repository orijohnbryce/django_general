from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# # Create your views here.
def home(request):
    return HttpResponse("hi")


def default(req):
    return render(template_name="index.html", request=req, context={"name": "ori"})


class MyView(View):

    def get(self, request):
        return HttpResponse("class based view - GET")

    def post(self, req):
        return HttpResponse("class based view - POST")


def serve_extend(req, num, bla):
    # return HttpResponse(num)
    return render(template_name="extended.html", request=req, context={"num1": num,
                                                                       "num2": req.GET.get('num2', bla)
                                                                       }
                  )


def serve_base(req):
    return render(template_name="base.html",
                  request=req)


# def serve_home(request):
#     return render(template_name="base.html", request=request,
#  			context={"title": "home"})
#
#
# def serve_suzuki(req):
#     return render(template_name="suzuki.html", request=req,
#  			context={'title': 'suzuki'})
#
#
# def serve_toyota(req):
#     return render(template_name="toyota.html", request=req,
#  			context={'title': 'toyota'})
