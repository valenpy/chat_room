from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from msg.api.serializers import MessageSerializer
from msg.forms import MessageForm
from msg.models import Message


class MessageListCreateAPIView(APIView):

    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # save data to db
        msg_form = MessageForm(request.data)
        if msg_form.is_valid():
            new_msg = msg_form.save()
            new_msg.save()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageListPagingAPIView(APIView):

    def get(self, request, page):
        messages = Message.objects.all()

        paginator = Paginator(messages, settings.MSG_PER_PAGE)

        try:
            messages = paginator.page(page)
        except PageNotAnInteger:
            messages = paginator.page(1)
        except EmptyPage:
            messages = paginator.page(paginator.num_pages)

        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


class MessageDetailAPIView(APIView):

    def get_object(self, slug):
        message = get_object_or_404(Message, slug=slug)
        return message

    def get(self, request, slug):
        message = self.get_object(slug)
        serializer = MessageSerializer(message)
        return Response(serializer.data)
