from django.shortcuts import render
from django.views import generic
from .models import Item


class MenuList(generic.ListView):
    queryset = Item.object.order_by("-date_created")
    template_name = "index.html"




class MenuListDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"



# two types of pages, 1.ListView -ex menu meals list,or front page of blog,which will have many links
#                     2.DetailView- ex details about that particular meal














#purpose of views is to get data from models of database and dispaly it on html(front-end)page
# 2 types of views we can define in views.py
# 1.function based views-which has more code
# 2.class based views-which has less/clean code-use any of these two based on your project purpose

