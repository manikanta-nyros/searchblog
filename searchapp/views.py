from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from searchapp.models import Note
from searchapp.forms import CreateNotesForm

from django.utils.safestring import mark_safe

from django.contrib import messages

# Create your views here.
def index(request):
    latest_notes_list = Note.objects.all().order_by('-timestamp')
    paginator = Paginator(latest_notes_list, 5) # Show 5 notes per page
    page = request.GET.get('page')
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        notes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        notes = paginator.page(paginator.num_pages)
    template = loader.get_template('searchapp/index.html')
    context = RequestContext(request, {'latest_notes_list': notes, })
    return HttpResponse(template.render(context))

def detail(request,note_id):
    try:
        note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        raise Http404
    return render_to_response('note_detail.html', {'note': note})

def create_note(request):
    if request.method == "GET":
        form = CreateNotesForm()
    else:
        form = CreateNotesForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            note = Note.objects.create(title=title,body=body)
            note.save()
            messages.success(request, 'Notes saved sucessfully')
            return redirect('/')
        return  render(request,'searchapp/create_note.html',{'form': form},context_instance=RequestContext(request))
    form = CreateNotesForm()
    return  render(request,'searchapp/create_note.html',{'form': form},context_instance=RequestContext(request))


