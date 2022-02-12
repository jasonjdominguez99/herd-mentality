from __init__ import created_app
from ariadne import (
    load_schema_from_path, make_executable_schema,
    graphql_sync, snake_case_fallback_resolvers,
    QueryType, MutationType, gql
)
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from resolvers import (
    card_mutation, card_query, player_mutation,
    player_query
)

query = QueryType()
query.set_field("players", player_query.get_players)
query.set_field("card", card_query.get_card)

mutation = MutationType()
mutation.set_field("createPlayer", player_mutation.create_player)
mutation.set_field("updatePlayer", player_mutation.update_player)
mutation.set_field("createCard", card_mutation.create_card)
mutation.set_field("updateCard", card_mutation.update_card)

type_defs = gql(load_schema_from_path("api/schema/"))
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

app = created_app()

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run()