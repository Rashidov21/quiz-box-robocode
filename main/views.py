from django.shortcuts import render
from .models import Contact
import telebot
from .config import TOKEN 

# Create your views here.
bot = telebot.TeleBot(TOKEN)


def home_page(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        if name and phone and message:
            Contact.objects.create(fullname=name, phone=phone, message=message)
            msg = f"""
                Ism Sharifi : {name} \nTelefon : {phone} \nXabar : {message}        
                """
            bot.send_message(-1001289148392, msg)
    return render(request, "index/index.html")
