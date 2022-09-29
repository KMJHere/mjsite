from asyncore import write
from csv import writer
from json import load
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import member, board, like
from django.template import loader
from django.http import Http404
from django.urls import reverse

# Create your views here.

def index(request):
    desc_user = member.objects.order_by('-member_id')[:5]
    # output = ', '.join([a.name for a in desc_user])
    tpl = loader.get_template("newp/index.html")
    context = {
        'desc_user': desc_user
    }
    # return HttpResponse(output)
    # return HttpResponse(tpl.render(context, request))
    return render(request, 'newp/index.html', context)
def detail(request, member_id):
    # return HttpResponse("This Is Detail Page Who Id? %s" % member_id)
    """
    shortcuts 코드로 변경
    try:
        info = member.objects.get(pk=member_id)
        content = board.objects.get(writer=member_id)
    except member.DoesNotExist:
        raise Http404("No Data")
    """
    info = get_object_or_404(board, writer=member_id)
    other_member = member.objects.exclude(member_id=member_id)
    return render(request, 'newp/detail.html', {'info':info, 'other_member':other_member}) 
def modify(request, member_id):
    return HttpResponse("This Is Modify Page Who Id? %s" % member_id)
def like(request, board_id):
    item = get_object_or_404(board, pk=board_id)
    try:
        selected_like = item.like_set.get(pk=request.POST['like']) # key, value 값으로 데이터 받아옴.. 
    except (KeyError, like.DoesNotExist):
        # reload like form
        return render(request, 'newp/detail.html', {
            'board': item,
            'error_message': "Like Select Plz"
        })
    else:
        selected_like.like += 1
        selected_like.save()
        
        return HttpResponseRedirect(reverse('newp:result', args=(item.id,)))
def result(request, board_id):
    data = get_object_or_404(board, pk=board_id)

    return render(request, 'newp/result.html', {'board': data})

