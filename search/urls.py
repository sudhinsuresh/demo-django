from search import views
from django.urls import path
app_name="search"

urlpatterns = [
    path('search/',views.searchresult,name="searchresult")
    

]