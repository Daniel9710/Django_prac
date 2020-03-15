from django.http import JsonResponse
from .serializers import TextSerializer, ColorSerializer
from rest_framework.parsers import JSONParser
from .models import Text, Color
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# Create your views here.


@csrf_exempt
def color_get(request, pk):
    try:
        obj = Color.objects.get(pk=pk)
    except Color.DoesNotExist:
        return JsonResponse({"error": 0}, safe=False)
    else:
        obj.access_time = timezone.localtime()
        obj.save()
        serializer = ColorSerializer(obj)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def color_patch(request, pk):
    data = JSONParser().parse(request)
    try:
        obj = Color.objects.get(pk=pk)
    except Color.DoesNotExist:
        return JsonResponse({"error": 3, "cid": data["cid"], "color": data["color"]}, status=201)
    else:
        data["access_time"] = timezone.localtime()
        if obj.color == data["color"]:
            s = {"error": 3, "cid": obj.cid, "color": obj.color}
        else:
            s = {"cid": obj.cid, "color": obj.color}
            data["update_time"] = data["access_time"]
        serializer = ColorSerializer(obj, data=data, partial=True)
        serializer.is_valid()
        serializer.save()
        return JsonResponse(s, status=201)


@csrf_exempt
def text_get(request, pk):
    data = JSONParser().parse(request)
    try:
        obj = Text.objects.get(pk=pk)
    except Text.DoesNotExist:
        return JsonResponse({"error": 0}, safe=False)
    else:
        serializer = TextSerializer(obj)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def text_put(request, pk):
    data = JSONParser().parse(request)
    serializer = TextSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    obj = Text.objects.get(pk=pk)
    return JsonResponse({"error": 1, "tid": obj.tid, "txt": obj.txt}, status=201)


@csrf_exempt
def text_patch(request, pk):
    data = JSONParser().parse(request)
    try:
        obj = Text.objects.get(pk=pk)
    except Text.DoesNotExist:
        return JsonResponse({"error": 4, "tid": data["tid"]}, status=201)
    else:
        serializer = TextSerializer(obj, data=data)
        if serializer.is_valid():
            if obj.txt == data["txt"]:
                return JsonResponse({"error": 2, "tid": obj.tid, "txt": obj.txt}, status=201)
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def text_delete(request, pk):
    try:
        obj = Text.objects.get(pk=pk)
    except Text.DoesNotExist:
        return JsonResponse({"error": 4, "tid": data["tid"]}, safe=False)
    else:
        obj.delete()
        return JsonResponse({"tid": obj.tid, "txt": obj.txt}, safe=False)
