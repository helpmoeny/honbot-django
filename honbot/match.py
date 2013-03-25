import os
import json
import views
import time


directory = str(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'match')) + '/'


def match(match_id):
    """
    initial hit for match view makes some decisions based on if the match is parsed already
    """
    if checkfile(match_id):
        return prepare_match(load_match(match_id), match_id)
    else:
        url = '/multi_match/all/matchids/' + str(match_id)
        data = views.get_json(url)
        h = [[str(match_id), '1/1/1']]
        if data is not None:
            multimatch(data, h)
            return match(match_id)
        else:
            return None


def prepare_match(data, match_id):
    """
    prepares match data for match view
    """
    match = {}
    players = [None]*10
    for p in data['players']:
        players[int(data['players'][p]['position'])] = data['players'][p]
    match['matchlength'] = data['realtime']
    match['players'] = players
    return match


def recent_matches(match_json, results):
    """
    returns specifed number of recent matches and win loss status as bool
    """
    if match_json[0]['history'] is not None:
        data = match_json[0]['history'].split(',')
        matches = []
        temp = []
        for i in data:
            temp = i.split('|')
            temp.pop(1)
            if len(matches) > 0:
                if matches[-1][0] != temp[0]:
                    matches.append(temp)
            else:
                matches.append(temp)
        matches.reverse()
        return matches[:results]
    else:
        matches = []
        return matches


def checkfile(match_id):
    """
    check if match has been parsed before returns bool
    """
    print directory
    if os.path.exists(directory + str(match_id) + '.json'):
        return True
    else:
        return False


def match_save(data, match_id):
    """
    save match to directory in json format
    """
    with open(directory + str(match_id) + '.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)


def load_match(match_id):
    """
    open match from directory and return json
    """
    if checkfile(match_id):
        with open(directory + str(match_id) + '.json', 'rb') as f:
            data = json.load(f)
        return data
    else:
        return None


def multimatch(data, history):
    """
    pass this multimatch api results and the number of matches. it will parse and save the useful bits
    """
    allmatches = {}
    for m in history:
        match = {}
        match['match_id'] = m[0]
        allmatches[str(m[0])] = match
        players = {}
        allmatches[m[0]]['players'] = players
    for m in data[2]:
        matchlength = round(float(m['secs']) / 60, 1)
        allmatches[m['match_id']]['matchlength'] = matchlength
        allmatches[m['match_id']]['realtime'] = time.strftime('%M:%S', time.gmtime(int(m['secs'])))
        player = {}
        player['id'] = m['account_id']
        player['kills'] = m['herokills']
        player['deaths'] = m['deaths']
        player['assists'] = m['heroassists']
        player['herodmg'] = m['herodmg']
        player['hero'] = m['hero_id']
        player['position'] = m['position']
        player['team'] = m['team']
        player['consumables'] = m['consumables']
        player['level'] = m['level']
        player['goldlost2death'] = m['goldlost2death']
        player['secsdead'] = m['secs_dead']
        player['wards'] = m['wards']
        player['denies'] = m['denies']
        player['herodmg'] = m['herodmg']
        if int(matchlength) > 0:
            player['gpm'] = round(int(m['gold']) / matchlength, 1)
            player['xpm'] = round(int(m['exp']) / matchlength, 1)
            player['apm'] = round(int(m['actions']) / matchlength, 1)
        player['cs'] = m['teamcreepkills']
        try:
            player['kdr'] = round(float(player['kills']) / float(player['deaths']), 1)
        except ZeroDivisionError:
            player['kdr'] = 'Inf.'
        player['win'] = bool(int(m['wins']))
        player['smackdown'] = m['smackdown']
        player['bdmg'] = m['bdmg']
        player['nickname'] = m['nickname']
        allmatches[m['match_id']]['players'][m['account_id']] = player
        allmatches[m['match_id']]['players'][m['account_id']]['items'] = None
    for m in data[1]:
        items = [None]*6
        items[0] = m['slot_1']
        items[1] = m['slot_2']
        items[2] = m['slot_3']
        items[3] = m['slot_4']
        items[4] = m['slot_5']
        items[5] = m['slot_6']
        allmatches[m['match_id']]['players'][m['account_id']]['nickname'] = m['nickname']
        allmatches[m['match_id']]['players'][m['account_id']]['items'] = items
    ### Save to file ###
    for m in history:
        allmatches[m[0]]['date'] = m[1]
        match_save(allmatches[m[0]], m[0])


def get_player_from_matches(history, account_id):
    """
    this takes a list of matches and returns that player's stats in that match
    """
    matches = []
    for m in history:
        temp = {}
        raw = load_match(m[0])
        if raw is not None and int(m[0]) > 60000000:
            temp = raw['players'][str(account_id)]
            temp['match_id'] = m[0]
            temp['date'] = m[1]
            matches.append(temp)
    return matches
