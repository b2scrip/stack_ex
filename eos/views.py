from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Question,Answer

class EosDetail(DetailView):
    model = Question
    context_object_name = "question"
    template_name = "eos/detail.html"
    def get_context_data(self, **kwargs):
        super(EosDetail, self).get_object().increase_views()
        context = super().get_context_data(**kwargs) 
        postid  = super(EosDetail, self).get_object().postid
        _tags  = super(EosDetail, self).get_object().tags.split(";")[1::2]
        if _tags:
            try:tags = [x.split("&")[0] for x in _tags]
            except Exception:tags=[]
        context["answers"] = Answer.objects.filter(parentid=postid)
        context["tags"] = tags
        context["re_posts"] = Question.objects.all().order_by('?')[:20]
        return context

class EosHome(ListView):
    model = Question
    context_object_name = "questions"
    template_name = "eos/home.html"
    paginate_by = 20
    ordering = ["-id"]
