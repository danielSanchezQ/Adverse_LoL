__author__ = 'Netwave'



import requests as rq


class RiotRequester:
    northamerica = 'na'
    europewest = 'euw'
    europenortheast = 'eune'
    brazil = 'br'
    turkey = 'tr'
    russia = 'ru'
    latinamericanorth = 'lan'
    latinamericansouth = 'las'
    oceania = 'oce'

    baseurl = 'https://{zone}.api.pvp.net'

    def __init__(self, requester):
        self.requester = requester

    def test(self, zone):
        testurl = '/api/lol/{region}/v1.4/summoner/by-name/{summonerNames}'.format(region=RiotRequester.europewest, summonerNames='n3twave')
        payload = {'key': open("KeyFile").read()}
        fullurl = RiotRequester.baseurl.format(region=RiotRequester.europewest)+testurl
        r = self.requester.get(fullurl, payload)
        return r.json()

    def getUserHistory(self):
        pass
