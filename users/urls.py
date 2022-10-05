from django.urls import path
from . import views

app_name = "users"   


urlpatterns = [
    path("source/<slug>/", views.UserDetailView.as_view(), name="user_detail"),
    path("all/sources/", views.UserListView.as_view(), name="user_list"),
    path("delete/user/<int:pk>/", views.UserDeleteView.as_view(), name="user_delete"),
    path("update/user/<slug>/", views.UserUpdateView.as_view(), name="user_update"),

    
]