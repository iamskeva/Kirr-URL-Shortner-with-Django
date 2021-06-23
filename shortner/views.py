from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from analytics.models import ClickEvent
from django.views import View
from .models import KirrURL
from .forms import SubmitUrlForm


# Create your views here.

# def home_view_fbv(request, *args, **kwargs):
#     if request.method == "POST":
#         print(render.POST)
#     return render(request, "shortner/home.html", {})

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "obr.com",
            "form": the_form
        }
        return render(request, "shortner/home.html", context)


    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "obr.com",
            "form": form
        }

        template = "shortner/home.html"

        if form.is_valid():
            print(form.cleaned_data.get("url"))
            new_url = form.cleaned_data.get("url")
            obj, created =KirrURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "create": created
            }
            if created:
                template = "shortner/success.html"
            else:
                template = "shortner/already-exist.html"

        return render(request, template, context)


class URLRediectView(View):  # Class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)



'''
    #Use method if you want something else to happen if url not found
    try:
        obj = KirrURL.objects.get(shortcode=shortcode)
    except:
        obj = KirrURL.objects.all().first()

'''