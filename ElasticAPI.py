#-*- coding:utf8-*-
from elasticsearch5 import Elasticsearch as  es
#from elasticsearch5 import helps
import pdb
ES_SERVERS=[
    {'host': "192.168.200.194",
     'port': 9200
     }]
query_json={
        "query":{"match_all":{}}
    }
es_client = es(hosts=ES_SERVERS)

def Scan():
    pdb.set_trace()
    bodystru = {
        "query": {"match_all": {}}
    }
    iret = es_client.get(index="mailtrendstat",doc_type='sender',id=752)
    page = es_client.search(index="mailtrendstat", doc_type='sender', scroll='2m',
                            size=3,
                            body=bodystru,
                            search_type='scan'
                           )
    print iret
    print page
    return iret
def FindESdata():
    iret = es_client.indices.create(index='news', ignore=400)
    index = "mailtrendstat"
    bodystru={
        "query":{"match":{
            ""
        }}
    }
    #pdb.set_trace()
    page = es_client.search(index="mailtrendstat",doc_type='sender',scroll='2m',
                            size=3,
                            body=bodystru,
                            from_='5')
    sid=page['_scroll_id']
    subdata = page['hits']['hits'] #查询出来的数据
    count =len(subdata) #查询出来的条数
    total = page['hits']['total']#记录总数
    print "sid:",sid
    print subdata
    result=subdata
    while count>0:
        pdb.set_trace()
        #scroll_id = page['_scroll_id']
        scroll_id="DnF1ZXJ5VGhlbkZldGNoBQAAAAAAAKtaFnRGQmdTaXdfU1hXeXNPSTBscVJwcEEAAAAAAACrXBZ0RkJnU2l3X1NYV3lzT0kwbHFScHBBAAAAAAAAq1sWdEZCZ1Npd19TWFd5c09JMGxxUnBwQQAAAAAAAKtZFnRGQmdTaXdfU1hXeXNPSTBscVJwcEEAAAAAAACrXRZ0RkJnU2l3X1NYV3lzT0kwbHFScHBB"
        page = es_client.scroll(scroll_id=scroll_id,scroll='2m')
        pdb.set_trace()
        subdata=page['hits']['hits']
        result.extend(page)
        count+=len(subdata)
        print subdata
        print scroll_id
        if count>=total:
           break
        #break
    return result
def fun_():
    scroll_id = "DnF1ZXJ5VGhlbkZldGNoBQAAAAAAAKmeFnRGQmdTaXdfU1hXeXNPSTBscVJwcEEAAAAAAACpoBZ0RkJnU2l3X1NYV3lzT0kwbHFScHBBAAAAAAAAqZ0WdEZCZ1Npd19TWFd5c09JMGxxUnBwQQAAAAAAAKmfFnRGQmdTaXdfU1hXeXNPSTBscVJwcEEAAAAAAACpoRZ0RkJnU2l3X1NYV3lzT0kwbHFScHBB"
    page = es_client.scroll(scroll_id=scroll_id, scroll='2m')
    subdata = page['hits']['hits']
    #result.extend(page)
    #count += len(subdata)
    print subdata
def Scrollandscan():
    pdb.set_trace()
    es_result = es_client.scan(es_client,query=query_json,scroll=scroll,index="my_source",doc_type="logs")
    final_result = []
    for item in es_result:
        final_result.append(item['_source'])
match_query={
    "query":{
        "match":{
            "_id":"953"
        }
    }
}
def metchID():
    pdb.set_trace()
    ret = es_client.search(index="mailtrendstat",scroll="2m", doc_type="sender", body=match_query)
    scroll_id=ret["_scroll_id"]
    data = es_client.scroll(scroll_id=scroll_id,scroll='2m')
    print ret
import sys
def get_cur_info():
    print sys._getframe().f_code.co_name
    print sys._getframe().f_back.f_lineno

if __name__=="__main__":
    #st= FindESdata()
    #fun_()
    #metchID()
    #Scrollandscan()
    #Scan()
    get_cur_info()