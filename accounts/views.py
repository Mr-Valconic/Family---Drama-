from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import FamilyMember, Story



# Home Page

def home(request):

    return render(request, "home.html")





# Dashboard

def dashboard(request):

    members = FamilyMember.objects.filter(
        user=request.user
    )

    stories = Story.objects.filter(
        user=request.user
    )

    context = {

        "members": members,

        "member_count": members.count(),

        "stories": stories,

        "story_count": stories.count(),

    }

    return render(
        request,
        "dashboard.html",
        context
    )

# Register

def register(request):

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]


        User.objects.create_user(

            username=username,

            password=password

        )


        return redirect("login")


    return render(request, "register.html")






# Login

def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]


        user = authenticate(

            username=username,

            password=password

        )


        if user:

            login(request, user)

            return redirect("dashboard")


    return render(request, "login.html")







# Add Family Member

def add_member(request):

    if request.method == "POST":

        name = request.POST["name"]

        relation = request.POST["relation"]

        image = request.FILES.get("image")



        FamilyMember.objects.create(

            user=request.user,

            name=name,

            relation=relation,

            image=image

        )


        return redirect("dashboard")



    return render(request, "add_member.html")








# Delete Family Member

def delete_member(request, id):

    member = FamilyMember.objects.get(id=id)

    member.delete()


    return redirect("dashboard")








# Edit Family Member

def edit_member(request, id):

    member = FamilyMember.objects.get(id=id)



    if request.method == "POST":


        member.name = request.POST["name"]

        member.relation = request.POST["relation"]



        if request.FILES.get("image"):

            member.image = request.FILES.get("image")



        member.save()



        return redirect("dashboard")




    return render(

        request,

        "edit_member.html",

        {

            "member": member

        }

    )
# Add Story

def add_story(request):

    if request.method == "POST":

        title = request.POST["title"]

        description = request.POST["description"]

        image = request.FILES.get("image")


        Story.objects.create(

            user=request.user,

            title=title,

            description=description,

            image=image

        )


        return redirect("dashboard")



    return render(request, "add_story.html")