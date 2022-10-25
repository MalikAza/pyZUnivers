import requests
import urllib.parse
from datetime import datetime, timedelta

base_url = "https://zunivers-api.zerator.com/public/"
joueur_url = "https://zunivers.zerator.com/joueur/"
full_date_format = "%Y-%m-%dT%H:%M:%S"
vortex_date_format = "%Y-%m-%d"

### Methods ###

def _get_datas(url):
    with requests.get(url) as r:
        datas = r.json()

    return datas

def user_journa(username):
    """arg: discord username (ex: ZeratoR#1337)
    return: bool"""
    full_user = urllib.parse.quote(str(username))
    activity_datas = _get_datas(f"{base_url}user/{full_user}/activity") # api req
    last_loot_count = activity_datas["lootInfos"][364]["count"]

    if last_loot_count == 0:
        return False
    else:
        return True

def user_pity(username):
    """arg: discord username (ex: ZeratoR#1337)
    return: str object"""
    full_user = urllib.parse.quote(str(username))
    user_overview_datas = _get_datas(f"{base_url}user/{full_user}/overview") # api req

    return int(str(user_overview_datas["invokeBeforePity"])[:-1])

def user_vortex_stats(username):
    """arg: discord username (ex: ZeratoR#1337)
    return: 2 int => vortex_stade, vortex_trys"""
    full_user = urllib.parse.quote(str(username))
    user_overview_datas = _get_datas(f"{base_url}user/{full_user}/overview") # api req
    vortex_stats = user_overview_datas["towerStat"]

    if vortex_stats:
        if vortex_stats["maxFloorIndex"] == 0: vortex_stade = 1
        else:
            if not vortex_stats["maxFloorIndex"]: vortex_stade = 0
            else: vortex_stade = vortex_stats["maxFloorIndex"] + 1
        vortex_trys = vortex_stats["towerLogCount"]
    else:
        vortex_stade = 0
        vortex_trys = 0

    return vortex_stade, vortex_trys

### Classes ###

class Insomniaque():
    """arg: discord username (ex: ZeratoR#1337)
    
    attributs: name, description, reward_score, done, progress_done, progress_todo"""

    def __init__(self, username):
        full_user = urllib.parse.quote(str(username))
        datas = _get_datas(f"{base_url}achievement/{full_user}/8e260bf0-f945-44b2-a9d9-92bf839ee917")
        insomniaque = datas[2]
        done = insomniaque["id"]

        self.name = insomniaque["achievement"]["name"]
        self.description = insomniaque["achievement"]["description"]
        self.reward_score = insomniaque["achievement"]["score"]
        if done:
            self.done = True
        else:
            self.done = False
            self.progress_done = []
            self.progress_todo = []

            for key, value in insomniaque["progress"]["items"].items():
                if value:
                    self.progress_done.append(key)
                else:
                    self.progress_todo.append(key)

class _ReputationClan():
    """attributs: name, level_name, progress"""

    def __init__(self, datas):
        score = datas["value"]
        level_max = datas["reputationLevel"]["toValue"] + 1

        self.name = datas["reputation"]["name"]
        self.level_name = datas["reputationLevel"]["name"]
        self.progress = f"{score}/{level_max}"

class _UserReputation():
    """attributs: first, second, third, fourth, fifth"""

    def __init__(self, datas):
        reputation_json = datas["reputations"]

        self.first = _ReputationClan(reputation_json[0])
        self.second = _ReputationClan(reputation_json[1])
        self.third = _ReputationClan(reputation_json[2])
        self.fourth = _ReputationClan(reputation_json[3])
        self.fifth = _ReputationClan(reputation_json[4])

class _ChallengeAtrb():
    """attributs: name, score_gain, powder_gain"""

    def __init__(self, datas):
        achieved = datas["challengeLog"]

        self.name = datas["challenge"]["description"]
        self.score_gain = datas["challenge"]["score"]
        self.powder_gain = datas["challenge"]["rewardLoreDust"]

class _UserChallengeAtrb():
    """attributs: name, score_gain, powder_gain, progress, achieved_date"""
    
    def __init__(self, datas):
        achieved = datas["challengeLog"]

        self.name = datas["challenge"]["description"]
        self.score_gain = datas["challenge"]["score"]
        self.powder_gain = datas["challenge"]["rewardLoreDust"]
        self.progress = f'{datas["progress"]["current"]}/{datas["progress"]["max"]}'
        if not achieved:
            self.achieved_date = None
        else:
            self.achieved_date = datetime.strptime(achieved["date"], full_date_format)

class Challenges():
    """arg: discord username (ex: ZeratoR#1337)
    attributs: first, second, third, begin_date, end_date"""

    def __init__(self, username):
        full_user = urllib.parse.quote(str(username))
        datas = _get_datas(base_url + "challenge" + (f"/{full_user}" if username else ""))
        
        self.first = _ChallengeAtrb(datas[0])
        self.second = _ChallengeAtrb(datas[1])
        self.third = _ChallengeAtrb(datas[2])
        if username:
            self.first = _UserChallengeAtrb(datas[0])
            self.second = _UserChallengeAtrb(datas[1])
            self.third = _UserChallengeAtrb(datas[2])
        # dates
        self.begin_date = datetime.strptime(datas[0]["beginDate"], full_date_format)
        self.end_date = datetime.strptime(datas[0]["endDate"], full_date_format)

class Event:
    """attributs: got_events, names, pack_names, monney_costs, dust_costs, is_onetimes, begin_dates, end_dates, actives"""

    def __init__(self):
        datas = _get_datas(base_url + "event")

        if datas != []:
            self.got_events = True
            self.names = []
            self.pack_names = []
            self.monney_costs = []
            self.dust_costs = []
            self.is_onetimes = []
            self.begin_dates = []
            self.end_dates = []
            self.actives = []
            for i in range(len(datas)):
                self.names.append(datas[i]["name"])
                self.pack_names.append(datas[i]["pack"]["name"])
                self.monney_costs.append(datas[i]["balanceCost"])
                self.dust_costs.append(datas[i]["loreDustCost"])
                self.is_onetimes.append(datas[i]["isOneTime"])
                self.begin_dates.append(datetime.strptime(datas[i]["beginDate"], full_date_format))
                self.end_dates.append(datetime.strptime(datas[i]["endDate"], full_date_format))
                self.actives.append(datas[i]["isActive"])
        else:
            self.got_events = False

class Vortex:
    """attributs: name, pack, reputation, begin_date, end_date"""

    def __init__(self):
        datas_season = _get_datas(f"{base_url}tower/season")
        datas_stats = _get_datas(f"{base_url}tower/stats")

        self.name = datas_season["tower"]["name"]
        self.pack = datas_season["tower"]["pack"]["name"]
        self.reputation = datas_season["tower"]["reputation"]["name"]
        self.begin_date = datetime.strptime(datas_season["beginDate"], vortex_date_format)
        self.end_date = datetime.strptime(datas_season["endDate"], vortex_date_format)

class _Leaderboard:
    """attributs: position, score"""

    def __init__(self, datas):
        self.position = datas["position"]
        self.score = datas["score"]

class _UserLeaderboards:
    """attributs: achievement, challenge, globals, inventory, inventory_unique, inventory_unique_golden,
                inventory_unique_normal, reputation, tradeless"""

    def __init__(self, datas):
        self.achievement = _Leaderboard(datas[0])
        self.challenge = _Leaderboard(datas[1])
        self.globals = _Leaderboard(datas[2])
        self.inventory = _Leaderboard(datas[3])
        self.inventory_unique = _Leaderboard(datas[4])
        self.inventory_unique_golden = _Leaderboard(datas[5])
        self.inventory_unique_normal = _Leaderboard(datas[6])
        self.reputation = _Leaderboard(datas[7])
        try:
            self.tradeless = _Leaderboard(datas[8])
        except IndexError:
            self.tradeless = False
        try:
            self.constellations = _Leaderboard(datas[9])
        except IndexError:
            self.constellations = False

class User():
    """arg: discord username (ex: ZeratoR#1337)
            challenge: bool, default=False
            reputation: bool, default=False
            journa: bool, default=False
            pity_andor_vortex: bool, default=False

    attributs: url, name, monnaie, powder, crystal, rank, active, card_numbers, unique_cards, unique_gold_cards,
            ticket_numbers, achievement_numbers, tradeless, is_subscribed, subscription_begin, subscription_begin_since,
            subscription_end, subscription_end_to, is_subscribed, pity_in, vortex_stade, vortex_trys, journa,
            challenge, reputation, leaderboards"""

    def __init__(self, username : discord.User,
                    challenge : bool = False,
                    reputation : bool = False,
                    journa : bool = False,
                    pity_andor_vortex : bool = False):

        full_user = urllib.parse.quote(str(username))
        user_datas = _get_datas(f"{base_url}user/{full_user}") # api req : basic informations

    ### miscellaneous indexes ###
        user = user_datas["user"]
        total_card_numbers = str(user_datas["itemCount"])
        total_achievement_numbers = str(user_datas["achievementCount"])
        trades = user_datas["tradeCount"]
        subscription = user_datas["subscription"]

    ### attributes ###
        self.url = f"{joueur_url}{full_user}"
        self.name = user["discordUserName"]
        self.monnaie = user["balance"]
        self.powder = user["loreDust"]
        self.crystal = user["loreFragment"]
        self.rank = user["rank"]["name"]
        self.active = user["isActive"]
        self.card_numbers = user_datas["inventoryCount"]
        self.unique_cards = f'{str(user_datas["inventoryUniqueCount"])}/{total_card_numbers}'
        self.unique_gold_cards = f'{str(user_datas["inventoryUniqueGoldenCount"])}/{total_card_numbers}'
        self.ticket_numbers = user_datas["luckyCount"]
        self.achievement_numbers = f'{str(user_datas["achievementLogCount"])}/{total_achievement_numbers}'
        # (no)tradeless
        if trades == 0:
            self.tradeless = True
        else:
            self.tradeless = False
        # sub
        if subscription:
            self.is_subscribed = True
            self.subscription_begin = datetime.strptime(subscription["beginDate"], full_date_format)
            self.subscription_end = datetime.strptime(subscription["endDate"], full_date_format)
        else:
            self.is_subscribed = False

    ### args exceptions ###

        # pity and or vortex #
        if pity_andor_vortex:
            ### datas ###
            user_overview_datas = _get_datas(f"{base_url}user/{full_user}/overview") # api req : pity + vortex_stade & vortex_trys
            ### miscellaneous indexes ###
            vortex_stats = user_overview_datas["towerStat"]
            ### attributes ###
            self.pity_in = int(str(user_overview_datas["invokeBeforePity"])[:-1])
            # vortex_stade & vortex_trys
            if vortex_stats:
                if vortex_stats["maxFloorIndex"] == 0: self.vortex_stade = 1
                else:
                    if not vortex_stats["maxFloorIndex"]: self.vortex_stade = 0
                    else: self.vortex_stade = vortex_stats["maxFloorIndex"] + 1
                self.vortex_trys = vortex_stats["towerLogCount"]
            else:
                self.vortex_stade = 0
                self.vortex_trys = 0

        # journa
        if journa: self.journa = user_journa(username)

    ### sub-classes ###
        if challenge: self.challenge = Challenges(username) # api req inside
        if reputation: self.reputation = UserReputation(username) # api req inside
        self.leaderboards = _UserLeaderboards(user_datas["leaderboards"])