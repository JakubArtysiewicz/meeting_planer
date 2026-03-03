from django.shortcuts import render, get_object_or_404

from meetingapp.models import Meeting

def welcome(request):
    meetings_count = Meeting.objects.count()
    meetings = Meeting.objects.all()
    return render(request, 'website/welcome.html', {'meetings': meetings, 'meetingsCount': meetings_count})

def details(request,id):
    meeting = get_object_or_404(Meeting,pk=id)
    return render(request, 'website/detail.html', {'meeting': meeting})