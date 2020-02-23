from django.urls import path
from msg.api.views import MessageListCreateAPIView, MessageDetailAPIView, MessageListPagingAPIView

urlpatterns = [
    path("messages/list", MessageListCreateAPIView.as_view(), name="messages-list"),
    path("messages/list/<int:page>", MessageListPagingAPIView.as_view(), name="messages-list-paging"),
    path("messages/single/<str:slug>", MessageDetailAPIView.as_view(), name="message-details"),

]
