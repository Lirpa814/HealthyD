from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Membership
from .serializers import MemebershipSerializer
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from django.db import connections



@csrf_exempt
def login(request):
    if request.method == 'POST':
        print("리퀘스트로그 : " + str(request.body))
        id = request.POST.get("userid", "")
        pw = request.POST.get("userpw", "")
        print("id = " + id + "/ pw = " + pw)

        result = authenticate(username=id, password=pw)

        if result:
            print("로그인 성공 !")
            return JsonResponse({'code': '0000', 'msg': '로그인 성공입니다.'}, status=200)
        else:
            print("실패")
            return JsonResponse({'code': '1001', 'msg': '로그인 실패입니다.'}, status=200)


@csrf_exempt
def app_login(request, cursor=None):
    if request.method == 'POST':
        print("리퀘스트 로그" + str(request.body))
        id = request.POST.get('userid', '')
        pw = request.POST.get('userpw', '')
        name = request.POST.get('name', '')
        print("id = " + id + " pw = " + pw + "/ name = " + name)

        result = authenticate(username=id, password=pw)

        if result:
            print("로그인 성공!")
            rs = Membership.objects.filter(name=name)
            rsList = []

            for re in rs:
                lst = str(re.address)
                rsList.append(lst)

            print(rsList)
            data = {'name': str(rsList)}
            return JsonResponse(data, safe=False, status=200)
        else:
            print("실패")
            return JsonResponse({'code': '1001', 'msg': '로그인실패입니다.'}, status=200)


@csrf_exempt
def app_get_info(request, cursor=None):
    if request.method == 'POST':
        print("Info : 리퀘스트 로그" + str(request.body))
        name = request.POST.get('name', '')
        print("name = " + name)

        result = Membership.objects.filter(name=name)

        if result:
            print("회원정보를 찾았습니다.")
            rs = Membership.objects.filter(name=name)
            rsList = []

            for re in rs:
                lst = str(re.name)
                rsList.append(lst)

            data = {'name': re.name, 'gender': re.gender, 'height': re.height, 'weight': re.weight}
            return JsonResponse(data, safe=False, status=200)
        else:
            print("회원정보를 찾을 수 없습니다.")
            data = {'name': '회원정보를 찾을 수 없습니다.'}
            return JsonResponse(data, safe=False, status=200)


@csrf_exempt
def app_post_info(request, cursor=None):
    if request.method == 'POST':
        print("Info : 회원정보 입력" + str(request.body))
        new_name = request.POST.get('name', '')
        new_gender = request.POST.get('gender', '')
        new_height = request.POST.get('height', '')
        new_weight = request.POST.get('weight', '')

        Membership.objects.create(name=new_name, gender=new_gender, height=new_height, weight=new_weight)

        data = {'name': '회원가입에 성공하였습니다.'}
        return JsonResponse(data, safe=False, status=200)


@csrf_exempt
def login_page(request):
    return render(request, "membership/login.html")