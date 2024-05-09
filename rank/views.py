from django.shortcuts import render
from .models import Rank  # Certifique-se de ter importado o modelo Rank
from rest_framework.decorators import api_view
import requests
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .serializers import RankSerializer

@api_view(['POST'])
@csrf_exempt
def get_rank(request, usuario, tag):
    api_key = 'RGAPI-f0541262-e972-406b-9ef7-b17a4cfc625c'  # Sua chave API

    # Obter PUUID
    account_url = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{usuario}/{tag}?api_key={api_key}'
    account_response = requests.get(account_url)
    if account_response.status_code == 200:
        puuid = account_response.json()['puuid']

        # Obter SummonerID
        summoner_url = f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={api_key}'
        summoner_response = requests.get(summoner_url)
        if summoner_response.status_code == 200:
            summoner_id = summoner_response.json()['id']
            
            # Obter ranking usando SummonerID
            rank_url = f'https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={api_key}'
            rank_response = requests.get(rank_url)
            if rank_response.status_code == 200:
                rank_data = rank_response.json()
                filtered_rank_data = []
                for entry in rank_data:
                    if entry['queueType'] == 'RANKED_SOLO_5x5':
                        rank_details = {
                            'tier': entry['tier'],
                            'rank': entry['rank'],
                            'leaguePoints': entry['leaguePoints']
                        }
                        filtered_rank_data.append(rank_details)
                
                # Salvar dados no banco de dados
                save_rank_data(usuario, tag, filtered_rank_data)
                
                return Response(filtered_rank_data)
            else:
                return Response({'error': 'Erro ao buscar ranking'}, status=rank_response.status_code)
        else:
            return Response({'error': 'Não foi possível obter informações do invocador'}, status=summoner_response.status_code)
    else:
        return Response({'error': 'Não foi possível obter o PUUID'}, status=account_response.status_code)

def save_rank_data(usuario, tag, rank_details):
    for detail in rank_details:
        Rank.objects.create(
            usuario=usuario,
            tag=tag,
            tier=detail['tier'],
            rank=detail['rank'],
            league_points=detail['leaguePoints']
        )


@api_view(['GET'])
def get_all_ranks(request):
    ranks = Rank.objects.all()
    serializer = RankSerializer(ranks, many=True)
    return Response(serializer.data)