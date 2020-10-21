from user_bet.models import *
from rest_framework.request import Request
from typing import List, \
    Dict, Union
from user_bet.go_bet_api_wrapper import GoBetWrapper
import logging
from sport_events.models import MatchEvent

LOG = logging.getLogger(__name__)


def process_bet_status(request: Request) -> bool:
    bets = request.data.get('Heads')
    if not bets:
        LOG.error('qqq')
        return False
    for bet in bets:
        user_bet = UserBet.objects.filter(bet_code=bet['KeyHead']['BarCode'], is_went=None).first()
        if not user_bet:
            LOG.error('www')
            return False
        status = bet.get('Status')
        exit_code = bet.get('ExtStatus')
        print(status, exit_code)
        if status == 2 and exit_code == 0:
            user_bet.user.customeraccount.current_balance += user_bet.user_win
            user_bet.is_went = True
            user_bet.save()
            user_bet.user.customeraccount.save()
            return True
        elif status == 4 and exit_code == 0:
            user_bet.user.customeraccount.current_balance -= user_bet.user_win
            user_bet.is_went = False
            user_bet.save()
            user_bet.user.customeraccount.save()
            return True
        elif status == 2 and exit_code == 1:
            user_bet.user.customeraccount.current_balance += user_bet.user_bet
            user_bet.is_went = False
            user_bet.returned = True
            user_bet.save()
            user_bet.user.customeraccount.save()
            return True
        else:
            LOG.error('rrr')
            return False








