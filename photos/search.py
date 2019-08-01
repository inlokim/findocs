from elasticsearch import Elasticsearch
import textract

class Util():

    def bin2txt(self, file_name):
        text = textract.process(file_name)
        return text.decode('utf-8')

    def search_index():
        
