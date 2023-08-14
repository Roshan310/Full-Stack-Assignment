from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# Create your views here.


@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_task(request, id):
    try:
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)
    except:
        return Response("Task not found")

@api_view(['POST'])
def create_task(request):
    data = request.data
    task = Task.objects.create(title=data['title'], description=data['description'])
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update_task(request, id):
    data = request.data
    try:
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(instance=task, data=data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    except:
        return Response("Task Not found")

@api_view(['DELETE'])
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response("Sucessfully Deleted!!")