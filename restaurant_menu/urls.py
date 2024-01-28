from django.urls import path
from . import views

urlpatterns = [
    path('',views.MenuList.as_view(),name="home"),
    path('item/<int:pk>',views.MenuListDetail.as_view(),name="menu_item_detail") #to make url more dynamic,we can add this syntax ie 'item/<int:pk>' ,we will expects integer from primary key(pk) of database.because each row of databse has primary key attached to it # after adding '<int:pk>' to url part we got out of error on web page
]



# we need to call as_view() method to render the mentioned page when user visit the url however we dont need to call this metod in function based views(views.py)
# ex of homepage url www.google.com/   so homepage has just '/'
# ex of other page inside google page www.google.com/about