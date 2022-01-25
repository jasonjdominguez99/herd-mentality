from ..models.models import Card
from ariadne import convert_kwargs_to_snake_case
import uuid

def create_card(*_, question):
    unique_id = uuid.uuid4()
    return Card(unique_id.int, question)

@convert_kwargs_to_snake_case
def update_card(_, info, has_been_picked=None):
    card = info.context.card
    card.update_has_been_picked(has_been_picked)

    return card