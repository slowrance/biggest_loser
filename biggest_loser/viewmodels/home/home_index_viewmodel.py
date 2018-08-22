from pyramid.request import Request

from biggest_loser.services import season_user_service
from biggest_loser.viewmodels.shared.viewmodel_base import ViewModelBase


class HomeIndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.users = season_user_service.get_users()
        self.user_count = season_user_service.user_count()
        self.cash_players = season_user_service.cash_count()
        self.prize_pool = season_user_service.prize_pool()

        self.calculate_user_stats(self.users)

    def calculate_user_stats(self, users):
        for u in users:
            u.lost_weight = False
            start_weight = u.weights[0].weight
            current_weight = u.weights[-1].weight
            u.percent = ((start_weight - current_weight) / start_weight)
            if u.percent >= 0:
                u.lost_weight = True
            u.percent = f'{u.percent:.2%}'
