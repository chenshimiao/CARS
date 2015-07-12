# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext,loader

from .models import TutorialItem

def index(request):
    cars_list=TutorialItem.objects.order_by('level')[:]
    level_list=['全部',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    gearbox_list=['全部','自动','手动','手自一体']
    title_web=('UsedCars Query')
    template=loader.get_template('polls/index.html')
    context=RequestContext(request,{
        'cars_list':cars_list,
        'title_web':title_web,
        'level_list':level_list,
        'gearbox_list':gearbox_list,
    })
    return HttpResponse(template.render(context))

def detail(request,tutorialitem_id):
    return HttpResponse("You're looking at tutorialitem %s." % tutorialitem_id)

def results(request,tutorialitem_id):
    response="You're looking at the results of tutorialitem %s."
    return HttpResponse(response % tutorialitem_id)

def vote(request,tutorialitem_id):
    return HttpResponse("You're voting on tutorialitem %s." % tutorialitem_id)

