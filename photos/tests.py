from django.test import TestCase
from elasticsearch import Elasticsearch
import json
import textract

class ElasticSearchTest(TestCase):

    def test_index(self):
        print("text")
        text = textract.process("/Users/Kiminlo/Downloads/111.doc")
        text2 = text.decode('utf-8')
        print(text2)
        # es=Elasticsearch([{'host':'localhost','port':9200}])
        #
        # res= es.search(index='megacorp',body={
        #         'query':{
        #             'match':{
        #                 "about":"play cricket"
        #             }
        #         }
        #     })
        # print(json.dumps(res,indent=2))
        # pass

    # def texttract1(self):
    #     print("text")
    #     text = textract.process("/Users/Kiminlo/Downloads/111.doc ")
    #     print(text)
