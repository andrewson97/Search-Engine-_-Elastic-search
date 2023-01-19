from elasticsearch import Elasticsearch

from query import basic_search
import json
import requests
# from rules import process

INDEX = 'va_tam'

def s_search(query):
    # result = client. (index=INDEX,body=standard_analyzer(query))
    # keywords = result ['tokens']['token']
    # print(keywords)
    
    # query_body= process(query)
    query_body = basic_search(query)
    #print(query_body)

    # data  = json.loads(query_body)
    # key_words = data['query']
    # fields = ['திரைப்படம்',"பாடலாசிரியர்","இசையமைப்பாளர்","வருடம்","குறிச்சொல்"]

    # for word in key_words:
    #     if (word in fields):




    #initiating basic search
    print('Making Basic Search ')
    res = requests.post("http://localhost:9200/va_tam/_search",json=query_body,) 
    json_data = res.json() 
    return json_data