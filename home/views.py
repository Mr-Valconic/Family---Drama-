from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Story


@login_required
def home(request):
    # Expired stories ko delete karo
    Story.objects.filter(expires_at__lte=timezone.now()).delete()

    # Sirf current user ki active stories dikhao
    stories = Story.objects.filter(
        user=request.user,
        expires_at__gt=timezone.now()
    ).order_by('-created_at')

    context = {
        "title": "Dashboard",
        "stories": stories,
    }

    return render(request, "home.html", context)


@login_required
def add_story(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if title and content:
            Story.objects.create(
                user=request.user,
                title=title,
                content=content,
            )

        return redirect("home")

    return redirect("home")