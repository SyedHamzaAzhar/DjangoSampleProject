import datetime
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from new_project.register.model import TODO
from new_project.register.serializer import TODOSerializer

class TODOs(APIView):
    # #To create a new TODO, send a POST request to /todos/ with the title and subject fields in the request body.
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        todo = TODO.objects.create(title=body['title'], subject=body['subject'], created_at=datetime.datetime.now(), updated_at=None)
        todo.save()
        serializer = TODOSerializer(todo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # #To retrieve all TODOs, send a GET request to /todos/.
    def get(self, request):
        todos = TODO.objects.all()
        serializer = TODOSerializer(todos, many=True)
        return Response(serializer.data)

    # #To update a TODO, send a PUT request to /todos/?title=<title> with the updated subject field in the request body.
    def put(self, request):
        title = request.GET.get('title', '')
        todo = TODO.objects.get(title=title)
        content = request.data
        todo.subject = content['subject']
        todo.updated_at = datetime.datetime.now()
        todo.save()
        serializer = TODOSerializer(todo)
        return Response(serializer.data)

    # #To delete a TODO, send a DELETE request to /todos/?title=<title>.
    def delete(self, request):
        title = request.GET.get('title', '')
        todo = TODO.objects.get(title=title)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    