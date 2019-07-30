from django.test import TestCase
from elasticsearch import Elasticsearch
import json

class ElasticSearchTest(TestCase):

    def test_index(self):

        es=Elasticsearch([{'host':'localhost','port':9200}])

        res= es.search(index='megacorp',body={
                'query':{
                    'match':{
                        "about":"play cricket"
                    }
                }
            })

        print(json.dumps(res,indent=2))
