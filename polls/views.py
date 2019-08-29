from django.shortcuts import render


from django.http import HttpResponse, HttpResponseNotFound


import numpy as np
import time

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
    
    return HttpResponse("Hello World! You're at the polls index.")


def send_4xx(request):

    return HttpResponseNotFound("Could not find what you are looking for!")



def send_5xx(request):
    raise Exception('I am Exception!')

    return HttpResponse("I should not be here")

