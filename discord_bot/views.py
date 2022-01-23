from django.shortcuts import render, get_object_or_404
from .models import Discord_bot

def all_discord_bots(request):

    # discord_bot_count =  Discord_bot.objects.count
    discord_bots = Discord_bot.objects.order_by('-date')
    return render(request, 'discord_bot/all_discord_bots.html', {'discord_bots':discord_bots})


def detail(request, discord_id):
    discord_bot = get_object_or_404(Discord_bot, pk=discord_id)
    return render(request, 'discord_bot/detail.html', {'discord_bot':discord_bot})

# Create your views here.
