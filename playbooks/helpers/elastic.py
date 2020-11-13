
from elasticsearch import Elasticsearch

def InitESconnctor(hostname, username, password, port=9200, scheme="https"):
    """
    Input: Take in info to connect to Elasticsearch
    Output: Return Elasticsearch conenctor
    """
    # Init ES connector
    es = Elasticsearch(
        [hostname],
        http_auth=(username, password),
        scheme=scheme,
        port=port,
    )
    return es

def QueryElasticsearch(es, index, query_body):
    """
    Input: Take in ES conenctor, query, and index to search
    Output: Return results from index based on query
    """
    results = es.search(
        index=index, 
        body=query_body
    )
    return results