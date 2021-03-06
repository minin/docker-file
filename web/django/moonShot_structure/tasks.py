'''
Created on Oct 30, 2016

@author: alexei.minin
'''
import datetime
import celery
import requests
import logging
import xmltodict
from moonShot_structure import models
from __builtin__ import str


@celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=1))
def get_lottery_data():
    def save_data(_game, draw_title):
        lottery_title = _game[0]
        lottery_id = _game[1]
        next_draw = _game[3].values()[0].values()[3]                
        draw_date = _game[5].values()[0].values()[3]
        lott_obj, status = models.Lottery.objects.get_or_create(title = lottery_title)
        draw_obj, status = models.Draw.objects.update_or_create(lottery_id = lott_obj.id,
                                                                title = draw_title,
                                                                jackpot = next_draw,
                                                                date = draw_date
                                                                   )
    response = requests.get('{url}'.format(url = 'http://www.lotteryfeed.com/xml_b/all_jackpots.xml'), stream=True)
    xml_obj = xmltodict.parse(response.content)
    try:
        for root_tag, games_dict in xml_obj.items():
            for jackpots, list_of_games in games_dict.items():
                for games in list_of_games:
                    _state = games.values()
                    draw_title = _state[0]
                    if len(games.get("game_jackpot")) != 6:                    
                        for game in games.get("game_jackpot"):
                            _game = game.values()
                            save_data(_game, draw_title)
                    else:
                        _game = games.get("game_jackpot").values()
                        save_data(_game, draw_title)
        logging.getLogger('moonShot').info('updating db tabels.')                                    
    except Exception as e:
        logging.getLogger('moonShot').error('failed while running celery task. ' + str(e))
