from .models import Project,Tag
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def searchProjects(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    tags=Tag.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(Q(title__icontains=search_query) | Q(tags__in=tags))
    return projects,search_query

def paginateProject(request,projects,results):

    paginator=Paginator(projects,results)
    try:
        page=request.GET.get('page')
        projects= paginator.page(page)
    except PageNotAnInteger:
        page=1
        projects= paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        projects= paginator.page(page)
    leftIndex=(int(page)-1)
    if leftIndex<1:
        leftIndex=1
    rightIndex= int(page)+2
    if rightIndex>paginator.num_pages:
        rightIndex=paginator.num_pages+1
    custome_range=range(leftIndex,rightIndex)
    return projects,custome_range
    