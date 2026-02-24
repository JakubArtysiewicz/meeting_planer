from django.shortcuts import render, get_object_or_404

from meetingapp.models import Meeting

#
# def welcome(request):
#     return render(request, 'website/welcome.html')

def welcome(request):
    meeting = Meeting.objects.count()
    return render(request, 'website/welcome.html', {'meeting': meeting})

def details(request,id):
    # meeting = Meeting.objects.all().get(pk=id)
    meeting = get_object_or_404(Meeting,pk=id)
    return render(request, 'website/detail.html', {'meeting': meeting})