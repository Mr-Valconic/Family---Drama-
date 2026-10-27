from django.urls import path
from . import views


urlpatterns = [

    # Home
    path(
        "",
        views.home,
        name="home"
    ),


    # Dashboard
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),


    # Add Family Member
    path(
        "add-member/",
        views.add_member,
        name="add_member"
    ),


    # Add Story
    path(
        "add-story/",
        views.add_story,
        name="add_story"
    ),


    # Edit Family Member
    path(
        "edit-member/<int:id>/",
        views.edit_member,
        name="edit_member"
    ),


    # Delete Family Member
    path(
        "delete-member/<int:id>/",
        views.delete_member,
        name="delete_member"
    ),


    # Register
    path(
        "register/",
        views.register,
        name="register"
    ),


    # Login
    path(
        "login/",
        views.login_view,
        name="login"
    ),

]