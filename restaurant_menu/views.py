from django.shortcuts import render
from django.views import generic
from .models import Item


class MenuList(generic.ListView):
    queryset = Item.object.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self):
        context = {"meals":["Pizza","Burger"],
                   "starter":"gobi"}
        return context




class MenuListDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"


# django will detects all html files inside "templates" folder/directory inside app directory,
#if templates directory will placed somewhere else other than inside app directory then in settings.py (project)
# mention/include ' in here as below
#   TEMPLATES = [
#     {templates'
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [templates'],            # Here include as name of template directory
#         'APP_DIRS': True,


# two types of pages, 1.ListView -ex menu meals list,or front page of blog,which will have many links
#                     2.DetailView- ex details about that particular meal



#purpose of views is to get data from models of database and dispaly it on html(front-end)page
# 2 types of views we can define in views.py
# 1.function based views-which has more code
# 2.class based views-which has less/clean code-use any of these two based on your project purpose

# get_context_data(exact name) is predefined method of ListView class
# context is a dictionary made up of keys and values and from html page we can access values by using keys of that context

