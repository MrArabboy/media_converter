import json
import datetime, pytz
from django.conf import settings
from rest_framework.response import Response
from telegram import Update, Bot
from telegram.ext import Dispatcher, MessageHandler, Filters, JobQueue
from rest_framework.views import APIView
import logging

from apps.bot.callback.start import conversation_handler


logger = logging.getLogger(__name__)
bot: Bot = Bot(token=settings.BOT_TOKEN)
dispatcher: Dispatcher = Dispatcher(bot, None)
dispatcher.add_handler(conversation_handler)


class BotView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode("utf-8"))
            update: Update = Update.de_json(data, bot=bot)
        except Exception as e:
            # logger.error("An uncaught error was raised while processing an update")
            return Response({"error": e})
        return Response("ok")
