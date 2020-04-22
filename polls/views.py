from django.shortcuts import render
import requests

from django.http import HttpResponse, HttpResponseNotFound


import numpy as np
import time

from .models import Post
from django_sample_project.tracer import get_tracer
tracer = get_tracer()

mu, sigma = 0.8, 0.2 # mean and standard deviation
s = np.random.normal(mu, sigma, 100)

def send_2xx(request):
    #print("I am inside polls index")
    num = request.session.get('num')
    if not num:
        num = 0
    
    if num < 100:
        time.sleep(s[num])
        #print ("Sleeping for: ", s[num])
        num += 1
        request.session['num'] = num
    else:
        time.sleep(s[0])
        request.session['num'] = 1

    # import  MySQLdb
    # db = MySQLdb.connect(host="localhost",user="root",
    #               passwd="password",db="test_db")

    # db.query("SELECT SLEEP(2);")
    # r=db.use_result()
    # result = (r.fetch_row())
    # print (result)

    # c = db.cursor()
    # c.execute("SELECT SLEEP(2);")
    # result = c.fetchone()
    # c.close()
    # db.commit()
    # db.close()


    post_obj = Post.objects.create(title="I am title", text="I am text")
    result = post_obj.id

    resp = requests.get("http://localhost:8080/")
    # print(resp.text)

    if tracer:
        with tracer.start_span('TestSpan') as span:
            span.log_kv({'event': 'test message', 'life': 42})
    else:
        print ("\n\n**** Error: Tracer not found. Jaeger should be there ******\n\n")

    # db = create_engine('sqlite:///tutorial.db')

    # db.echo = False  # Try changing this to True and see what happens

    # metadata = MetaData(db)

    # users = Table('users', metadata,
    #     Column('user_id', Integer, primary_key=True),
    #     Column('name', String(40)),
    #     Column('age', Integer),
    #     Column('password', String),
    # )
    # #users.create()

    # db.connect().execute("SELECT 1+1;")

    # i = users.insert()
    # i.execute(name='Mary', age=30, password='secret')
    # i.execute({'name': 'John', 'age': 42},
    #         {'name': 'Susan', 'age': 57},
    #         {'name': 'Carl', 'age': 33})

    # sel = users.select()
    # rs = sel.execute()

    # row = rs.fetchone()
    # print ('Id:', row[0])
    # print ('Name:', row['name'])
    # print ('Age:', row.age)
    # print ('Password:', row[users.c.password])

    # for row in rs:
    #     print (row.name, 'is', row.age, 'years old')


    # import urllib3
    # http = urllib3.PoolManager()
    # r = http.request('GET', 'http://ajax.googleapis.com/ajax/services/search/web')
    # result = r.data

    # from urllib3 import HTTPConnectionPool
    # pool = HTTPConnectionPool('ajax.googleapis.com', maxsize=1)
    # r = pool.request('GET', '/ajax/services/search/web', fields={'q': 'urllib3', 'v': '1.0'})
    # result = r.data

    # import requests
    # x = requests.get('https://w3schools.com/python/demopage.htm')
    # result = x.text

    # import redis
    # r = redis.Redis(host='localhost', port=6379)
    # r.set('foo', 'bar')

    # import pymongo

    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # mydb = myclient["mydatabase"]
    # mycol = mydb["customers"]

    # myquery = { "address": "Valley 345" }
    # newvalues = { "$set": { "address": "Canyon 123" } }

    # mycol.update_one(myquery, newvalues)

    # #print "customers" after the update:
    # for x in mycol.find():
    #     print(x)

    return HttpResponse("Created Object: " + str(result))


def send_4xx(request):

    return HttpResponseNotFound("Could not find what you are looking for!")



def send_5xx(request):
    raise Exception('I am Exception!')

    return HttpResponse("I should not be here")

