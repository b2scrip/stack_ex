from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from post.models import Question,Answer
from eth.models import Question as ethqn
from eos.models import Question as eosqn

from django.views import View
from django.shortcuts import render

class Detail(DetailView):
    model = Question
    context_object_name = "question"
    template_name = "post/detail.html"

    def get_context_data(self, **kwargs):
        super(Detail, self).get_object().increase_views()
        context = super().get_context_data(**kwargs)
        postid  = super(Detail, self).get_object().postid
        _tags  = super(Detail, self).get_object().tags.split(";")[1::2]
        if _tags:
            try:tags = [x.split("&")[0] for x in _tags]
            except Exception:tags=[]
        context["tags"] = tags
        context["re_posts"] = Question.objects.all().order_by('?')[:20]
        context["answers"] = Answer.objects.filter(parentid=postid)
        return context


class Home(ListView):
    model = Question
    context_object_name = "questions"
    template_name = "post/home.html"
    paginate_by = 20
    ordering = ["-id"]

class Price(View):
    template_name = "post/price.html"
    def get(self, request, *args, **kwargs):
        if self.kwargs["type"] == "btc":
            return render(request, self.template_name)

class RootPage(View):
    template_name = "post/rootpage.html"
    context  =  {
            "top_btc": Question.objects.order_by('-answercount')[:10],
            "top_eos": eosqn.objects.order_by('-answercount')[:10],
            "top_eth": ethqn.objects.order_by('-answercount')[:10],
                }
    def get(self, request):
            return render(request, self.template_name,context=self.context)
