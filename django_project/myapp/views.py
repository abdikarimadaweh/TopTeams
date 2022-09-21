from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Player

def index(request):
    return HttpResponse("Hello world!")

def get_players(request):
    players_bucks = Player.objects.raw('SELECT * FROM myapp_player WHERE team="Milwaukee Bucks" ORDER BY random() LIMIT 1')
    players_lakers = Player.objects.raw('SELECT * FROM myapp_player WHERE team="Los Angeles Lakers" ORDER BY random() LIMIT 1')
    players_raptors = Player.objects.raw('SELECT * FROM myapp_player WHERE team="Toronto Raptors" ORDER BY random() LIMIT 1')
    players_warriors = Player.objects.raw('SELECT * FROM myapp_player WHERE team="Golden State Warriors" ORDER BY random() LIMIT 1')
    players_rockets = Player.objects.raw('SELECT * FROM myapp_player WHERE team="Houston Rockets" ORDER BY random() LIMIT 1')
    players_cavaliers = Player.objects.raw('SELECT * FROM myapp_player WHERE team="Cleveland Cavaliers" ORDER BY random() LIMIT 1')
    players_thunder = Player.objects.raw('SELECT * FROM myapp_player WHERE team="OKC Thunder" ORDER BY random() LIMIT 1')
    players_spurs = Player.objects.raw('SELECT * FROM myapp_player WHERE team="San Antonio Spurs" ORDER BY random() LIMIT 1')
    players_heat = Player.objects.raw('SELECT * FROM myapp_player WHERE team="Miami Heat" ORDER BY random() LIMIT 1')
    players_mavericks = Player.objects.raw('SELECT * FROM myapp_player WHERE team="Dallas Mavericks" ORDER BY random() LIMIT 1')
    args = {'players_bucks': players_bucks, 'players_lakers': players_lakers, 'players_raptors': players_raptors, 'players_warriors': players_warriors,
            'players_rockets': players_rockets,'players_cavaliers': players_cavaliers,'players_thunder': players_thunder,'players_spurs': players_spurs,
            'players_heat': players_heat,'players_mavericks': players_mavericks,}
    return render(request, 'player_details.html', args)