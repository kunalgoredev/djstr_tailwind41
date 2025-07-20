# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect, render


def add_note_view(request):
    if request.method == "POST":
        messages.success(request, "Note added successfully!")
        return redirect("app_note:add_note")

    return render(request, "app_note/add_note.html")
