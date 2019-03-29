from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Task
from api.serializers import TaskSerializer

# Create your views here.

def home(request):
	return render(request, 'api.html')

@api_view(['POST'])
def create(request):
	task = Task()
	task.title = request.POST.get('title')
	task.description = request.POST.get('description')
	task.save()
	return Response("saved")

@api_view(['GET'])
def list(request):
	tasks = Task.objects.all()
	serializer = TaskSerializer(tasks, many=True, read_only=True)		
	return Response(serializer.data)

@api_view(['GET'])
def show(request, pk):
	tasks = Task.objects.get(pk=pk)
	serializer = TaskSerializer(tasks, read_only=True)	
	return Response(serializer.data)


@api_view(['PUT'])
def update(request, pk):
	task = Task.objects.get(pk=pk)
	task.title = request.POST.get('title')
	task.description = request.POST.get('description')
	task.save()
	return Response('updated')

@api_view(['DELETE'])
def delete(request, pk):
	task = Task.objects.get(pk=pk)
	task.delete()
	return Response('deleted')