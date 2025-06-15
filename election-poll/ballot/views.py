from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Candidate
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    spl_candidate_list_boys = Candidate.objects.filter(student_class = "XI", gender="M")
    spl_candidate_list_girls = Candidate.objects.filter(student_class = "XI", gender="F")
    aspl_candidate_list_boys = Candidate.objects.filter(student_class = "IX", gender="M")
    aspl_candidate_list_girls = Candidate.objects.filter(student_class = "IX", gender="F")
    template = loader.get_template("ballot/index.html")
    context = {
        "spl_candidate_list_boys": spl_candidate_list_boys,
        "spl_candidate_list_girls": spl_candidate_list_girls,
        "aspl_candidate_list_boys": aspl_candidate_list_boys,
        "aspl_candidate_list_girls": aspl_candidate_list_girls
    }
    return HttpResponse(template.render(context, request))

def welcome(request):
    return render(request, "ballot/welcome.html")

@require_POST
def vote(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    candidate.number_of_votes += 1
    candidate.save()
    return HttpResponse(f"Vote cast for {candidate.name} ({candidate.uid})")