from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Account
from django.http import JsonResponse
import json

def generate_graph():
    """
    Generate graph on dict
    returns dict
    """
    nodes = []
    edges = []
    for ac in Account.objects.all():
        childs=ac.childs.all()
        nodes.append({'id':ac.id,'label': str(ac.id) })
        for c in childs:
            edges.append({'from':ac.id,'to':c.id})
    return {'nodes':nodes, 'edges':edges}

def add_node(parent, child):
    """
    Add child node to parent node
    """
    if parent.id != child.id:
        parent.childs.add(child)

def move_node(new_parent, child):
    """
    Move child node to new_parent node, deleting all previous edges of child
    """
    child.account_set.clear()
    new_parent.childs.add(child)


class Graph(TemplateView):
    template_name = 'index.html'


def addNode(request):
    response =  {}
    data = request.POST.get('label')
    parent = request.POST.get('parent')
    child = Account(data=data)
    child.save()
    if parent:
        try:
            parent = Account.objects.get(id=parent)
            add_node(parent, child)
        except Exception as identifier:
            response["error"] = str(identifier)
    response = generate_graph()
    return JsonResponse(response)

def moveNode(request):
    response =  {}
    pId = id=request.POST.get('child')
    cId = id=request.POST.get('parent')
    if pId and cId:
        try:
            child = Account.objects.get(id=pId)
            parent = Account.objects.get(id=cId)
            move_node(parent,child)
        except Exception as identifier:
            response["error"] = str(identifier)
    response = generate_graph()
    return JsonResponse(response)
