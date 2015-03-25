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
    keyfile = "KeyFile"


    def __init__(self, requester):
        self.requester = requester
        self.payload = {'key': open("KeyFile").read()}

    def test(self, zone):
        testurl = '/api/lol/{region}/v1.4/summoner/by-name/{summonerNames}'.format(region=RiotRequester.europewest, summonerNames='n3twave')
        fullurl = RiotRequester.baseurl.format(zone=RiotRequester.europewest)+testurl
        r = self.requester.get(fullurl, self.payload)
        return r.json()

    def getUserHistory(self, username, champid, zone ):
        urldir = "/api/lol/{region}/v2.2/matchhistory/{summonerId}".format(summonerId=username, region=RiotRequester.__getattribute__(zone))
        fullurl = RiotRequester.baseurl.format(zone=RiotRequester.__getattribute__(zone))+urldir
        payload = self.payload
        payload['championids'] = champid
        payload['rankedQues'] = 'RANKED_SOLO_5x5'
        r = self.requester.get(fullurl, self.payload)
        return r.json()
