from app.api import cms
from flask_graphql import GraphQLView

from app.api.schema import schema

cms.add_url_rule('data', view_func=GraphQLView.as_view('graphql', schema=schema))