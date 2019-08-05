from elasticsearch import Elasticsearch
import textract
import json

class Util():

    def connection(self):
        es=Elasticsearch([{'host':'localhost','port':9200}])
        return es

    def bin2txt(self, file_name):
        text = textract.process(file_name)
        return text.decode('utf-8')

    def doc_index(self, title, content):
        e1={
            "title":title,
            "content":content
        }
        es=self.connection()
        res = es.index(index='test1',doc_type='doc',body=e1)

        print(res)

    def search(self, keyword):
        es=self.connection()
        res= es.search(index='test1',body={
                'query':{
                    'match':{
                        "content":keyword
                    }
                }
            })


        for hit in res['hits']['hits']:
            print(hit['_source']['content'])
            print(hit['_score'])
            print('**********************')
