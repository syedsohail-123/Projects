from django.urls import path
from .views import ChatBotView, ChatHistoryView

urlpatterns = [
    path('chat/', ChatBotView.as_view(), name='chatbot'),
    path('history/', ChatHistoryView.as_view(), name='history'),

]
