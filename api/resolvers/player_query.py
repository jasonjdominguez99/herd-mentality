from ..models.models import Player

def resolve_players(obj, info):
    return [player.to_dict() for player in Player.query.all()]