from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Work
from .serializers import WorkSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def work_list(request):
    if request.method == 'GET':
        works = Work.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            works = works.filter(title__icontains=title)

        works_serializer = WorkSerializer(works, many=True)
        return JsonResponse(works_serializer.data, safe=False)
    elif request.method == 'POST':
        work_data = JSONParser().parse(request)
        work_serializer = WorkSerializer(data=work_data)
        if work_serializer.is_valid():
            work_serializer.save()
            return JsonResponse(work_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(work_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def work_detail(request, id):
    try:
        work = Work.objects.get(id=id)
    except Work.DoesNotExist:
        return JsonResponse({'message': 'The work does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        work_serializer = WorkSerializer(work)
        return JsonResponse(work_serializer.data)
    elif request.method == 'PUT':
        work_data = JSONParser().parse(request)
        work_serializer = WorkSerializer(work, data=work_data)
        if work_serializer.is_valid():
            work_serializer.save()
            return JsonResponse(work_serializer.data)
        return JsonResponse(work_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def work_active(request):
    works = Work.objects.filter(active=True)

    if request.method == 'GET':
        work_serializer =WorkSerializer(works, many=True)
        return JsonResponse(work_serializer.data, safe=False)
