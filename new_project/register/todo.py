import datetime
import json

from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from .serializer import TODOSerializer
from .models import TODO

class TODOs(ListAPIView):

    serializer_class = TODOSerializer

    def todo(self):
        body_unicode = self.request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['content']

        #create todo
        if self.request.method == "POST":

            todo = TODO.objects.create(title=content['titile'], subject=content['subject'], created_at= datetime.now())
            todo.save()
        
        #get todo
        if  self.request.method == "GET":

             todo = TODO.objects.get_object_or_404(TODO, title=content['titile'])

        #update todo
        if  self.request.method == "PUT" or self.request.method == "PATCH":
            title = self.request.GET.get('title', '')

            todo = TODO.objects.get_object_or_404(TODO, title=title)
            todo['subject'] = content['subject']
            todo.save()

        #delete todo
        if  self.request.method =="DELETE":

            title = self.request.GET.get('title', '')
            todo = TODO.objects.get_object_or_404(TODO, title=title)
            todo.delete()

        return HttpResponse(todo)




