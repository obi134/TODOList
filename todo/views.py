# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from todo.models import List
from todo.models import Item
from todo.forms import EditEntryForm, NewEntryForm, DeleteEntryForm

# Create your views here.
  
def status_report(request):  
    todo_listing = []  
    for todo_list in List.objects.all():  
        todo_dict = {}  
        todo_dict['list_object'] = todo_list  
        todo_dict['item_count'] = todo_list.item_set.count()  
        todo_dict['items'] = todo_list.item_set.all()
        todo_dict['items_complete'] = todo_list.item_set.filter(completed=True).count()
        todo_dict['items_niedrig'] = todo_list.item_set.filter(completed=False,priority=1).count()
        todo_dict['items_mittel'] = todo_list.item_set.filter(completed=False,priority=2).count()
        todo_dict['items_hoch'] = todo_list.item_set.filter(completed=False,priority=3).count()
        todo_dict['items_woche'] = todo_list.item_set.filter(completed=False,priority=4).count()
        if todo_dict['item_count'] > 0:
            todo_dict['percent_complete'] = int(float(todo_dict['items_complete']) / todo_dict['item_count'] * 100) 
        else:
            todo_dict['percent_complete'] = 0
        todo_listing.append(todo_dict)  
    return render_to_response('status_report.html', { 'todo_listing': todo_listing })

def status_report_list(request):  
    todo_items = {}
    todo_items["items"] = Item.objects.order_by("completed", "-priority","todo_list")
    todo_items["item_count"] = len(todo_items["items"])
    todo_items["items_complete"] = len(Item.objects.filter(completed=True))
    todo_items['items_niedrig'] = len(Item.objects.filter(completed=False,priority=1))
    todo_items['items_mittel'] = len(Item.objects.filter(completed=False,priority=2))
    todo_items['items_hoch'] = len(Item.objects.filter(completed=False,priority=3))
    todo_items['items_woche'] = len(Item.objects.filter(completed=False,priority=4))
    if todo_items['item_count'] > 0:
        todo_items["percent_complete"] = int(float(todo_items['items_complete']) / todo_items['item_count'] * 100) 
    else:
        todo_items["percent_complete"] = 0
        
    return render_to_response('status_report_list.html', { 'todo_items': todo_items })

def edit_entry(request, entry_id, redirect):
    """View function for renewing a specific BookInstance by librarian."""
    entry_instance = get_object_or_404(Item, id=entry_id)
    print request.method

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = EditEntryForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            completed = form.cleaned_data["completed"]
            # process the data in form.cleaned_data as required
            if entry_instance.completed != completed:
                if completed == True:
                    entry_instance.date_finished = datetime.datetime.now()
                else:
                    entry_instance.date_finished = datetime.datetime.fromtimestamp(0)
            entry_instance.title                = form.cleaned_data["title"]
            entry_instance.priority             = form.cleaned_data["priority"]
            entry_instance.completed            = form.cleaned_data["completed"]
            entry_instance.estimation           = form.cleaned_data["estimation"]
            entry_instance.remaining_estimation = form.cleaned_data["remaining_estimation"]
            entry_instance.todo_list            = form.cleaned_data["todo_list"]
            entry_instance.save()

            list_completed_entries = list(Item.objects.filter(completed=True))
            for single_entry in list_completed_entries:
                if single_entry.date_finished.replace(tzinfo=None) != datetime.datetime.fromtimestamp(0):
                    #raise Http404("Diff: %s" % ((datetime.datetime.now()-single_entry.date_finished.replace(tzinfo=None)).seconds//3600))
                    if (datetime.datetime.now() - single_entry.date_finished.replace(tzinfo=None)).days > 10:
                        single_entry.delete()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse(redirect))

    # If this is a GET (or any other method) create the default form.
    else:
        form = EditEntryForm(initial={"title":                  entry_instance.title,
                                      "priority":               entry_instance.priority,
                                      "completed":              entry_instance.completed,
                                      "estimation":             entry_instance.estimation,
                                      "todo_list":              entry_instance.todo_list,
                                      "remaining_estimation":   entry_instance.remaining_estimation})
        
    context = {
        'form': form,
        'entry_instance': entry_instance,
    }

    return render(request, 'edit_entry.html', context)

def edit_entry_bylist(request, entry_id):
    return edit_entry(request, entry_id, "status-report")
    
def edit_entry_one(request, entry_id):
    return edit_entry(request, entry_id, "status-report-list")

def delete_entry(request, entry_id, redirect):
    """View function for renewing a specific BookInstance by librarian."""
    entry_instance = get_object_or_404(Item, id=entry_id)
    print request.method

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = DeleteEntryForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            entry_instance.delete()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse(redirect))

    # If this is a GET (or any other method) create the default form.
    else:
        form = DeleteEntryForm()
        
    context = {
        'form': form,
        'entry_instance': entry_instance,
    }

    return render(request, 'delete_entry.html', context)

def delete_entry_bylist(request, entry_id):
    return delete_entry(request, entry_id, "status-report")
    
def delete_entry_one(request, entry_id):
    return delete_entry(request, entry_id, "status-report-list")

def new_entry(request, redirect):
    """View function for renewing a specific BookInstance by librarian."""

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = NewEntryForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            entry_instance = Item()
            # process the data in form.cleaned_data as required
            entry_instance.title                = form.cleaned_data["title"]
            entry_instance.created_date         = datetime.datetime.now()
            entry_instance.priority             = form.cleaned_data["priority"]
            entry_instance.completed            = False
            entry_instance.todo_list            = form.cleaned_data["todo_list"]
            entry_instance.estimation           = form.cleaned_data["estimation"]
            entry_instance.remaining_estimation = form.cleaned_data["estimation"]            
            entry_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse(redirect))

    # If this is a GET (or any other method) create the default form.
    else:
        form = NewEntryForm(initial={"priority": 2})
        
    context = {
        'form': form,
    }

    return render(request, 'new_entry.html', context)

def new_entry_bylist(request):
    return new_entry(request, "status-report")
    
def new_entry_one(request):
    return new_entry(request,  "status-report-list")
