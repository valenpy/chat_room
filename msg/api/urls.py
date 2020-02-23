from django.urls import path
from msg.api.views import MessageListCreateAPIView, MessageDetailAPIView

urlpatterns = [
    path("messages/list", MessageListCreateAPIView.as_view(), name="messages-list"),
    path("messages/single/<str:slug>", MessageDetailAPIView.as_view(), name="message-details"),

]
