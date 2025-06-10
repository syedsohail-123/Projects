from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatMessage
from .serializers import ChatMessageSerializer
class ChatBotView(APIView):
    def post(self, request):
        user_message = request.data.get("user_message", "")
        bot_response = self.generate_response(user_message)

        chat = ChatMessage.objects.create(
            user_message=user_message,
            bot_response=bot_response
        )
        serializer = ChatMessageSerializer(chat)
        return Response(serializer.data)

    def generate_response(self, msg):
        if "hello" in msg.lower():
            return "Hi there! How can I assist you?"
        elif "bye" in msg.lower():
            return "Goodbye! Have a nice day."
        return "I'm just a demo bot. Try saying 'hello'."

class ChatHistoryView(APIView):
    def get(self, request):
        chats = ChatMessage.objects.all().order_by('-timestamp')
        serializer = ChatMessageSerializer(chats, many=True)
        return Response(serializer.data)
