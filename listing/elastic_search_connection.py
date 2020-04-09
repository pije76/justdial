from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Date

# creates a global connection to elastic search
connections.create_connection()


class ListingIndex(Document):
    title = Text()
    category = Text()
    location = Text()

    class Index:
        name = 'listing-index'
