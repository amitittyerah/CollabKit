import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from quiz.models import *
from api.common import *


def set_add(request):
    pass


def set_delete(request):
    pass


def set_update(request):
    pass


def set_list(request):
    response = {
        'status': True,
        'data': []
    }
    sets = Set.objects.all()
    set_json = [set.as_json() for set in sets]
    response['data'] = set_json
    return HttpResponse(json.dumps(response), content_type="application/json")


def qc_add(request):
    pass


def qc_delete(request):
    pass


def qc_update(request):
    pass


def qc_list(request):
    response = {
        'status': True,
        'data': []
    }
    qac = QuestionAnswerChoice.objects.all()
    qac_json = [qac_o.as_json() for qac_o in qac]
    response['data'] = qac_json
    return HttpResponse(json.dumps(response), content_type="application/json")


def question_add(request):
    pass


def question_delete(request):
    pass


def question_update(request):
    pass


@csrf_exempt
def question_check_mcq(request):
    response = {
        'status': False
    }
    question_id = request.POST['question_id']
    answer_id = request.POST['answer']
    response['status'] = Question.check_mcq(get_object_or_404(Question, pk=question_id), answer_id)
    return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def question_check_fb(request):
    response = {
        'status': False
    }
    question_id = request.POST['question_id']
    answer = request.POST['answer']
    response['status'] = Question.check_fb(get_object_or_404(Question, pk=question_id), answer)
    return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def question_check_tf(request):
    response = {
        'status': False
    }
    question_id = request.POST['question_id']
    answer = request.POST['answer']

    response['status'] = Question.check_tf(get_object_or_404(Question, pk=question_id), answer)
    return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def question_get_answer(request):
    question = request.POST['data']
    return HttpResponse(json.dumps(get_object_or_404(Question, pk=question).as_json()), content_type="application/json")

def question_list(request):
    response = {
        'status': True,
        'data': []
    }
    qs = Question.objects.all()
    qs_json = [q.as_json() for q in qs]
    response['data'] = qs_json
    print qs_json
    return HttpResponse(json.dumps(response), content_type="application/json")