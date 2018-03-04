#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 14:31:54 2018

@author: chirag
"""
from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
import matplotlib.pyplot as plt 
import numpy as np
import glob
import os, sys
fpath ="/Users/chirag/Downloads/SampleDataSet/traces.npy"
npyfilespath="/Users/chirag/Downloads/SampleDataSet"   
os.chdir(npyfilespath)
npfiles= glob.glob("*.npy")
npfiles.sort()
all_arrays = []
app = Flask(__name__)
CORS(app, support_credentials=True)


 
def getValues(X,Y,results):

    with open(fpath,'ab') as f_handle:
        for npfile in npfiles:
            #Find the path of the file and Load file\
           
            all_arrays.append(np.load(os.path.join(npyfilespath, npfile)))        
        
            dt= plt.axis((49599,50000,-6700000,-5000000)) 
       
        
        data = np.load(fpath)
        data=data.T
        #print (data(range(1000,20000)))
        #fin=data[0:90,6700000:5000000]
    
        print(data.shape)
        # temp
        chanindices = results # np.arange(lower,upper), or []
        timeindices = np.arange(X,Y) # timearray[0,10000]
        y_temp = data[np.ix_(chanindices, timeindices)]
        x_temp = timeindices
        
        return x_temp.tolist(), y_temp.tolist()
       # print (fin)
       # print (data[chanindices, index:index+stop])
        
        print(data)
    

    
@app.route('/api/tasks/<int:X>/<int:Y>/',methods=['GET'])
@cross_origin(supports_credentials=True)
def get_task(X,Y):
    #print(C, file=sys.stderr)
    results = request.args.get('channels')
    res = [int(x) for x in results.split(',')]
    x_val , y_val = getValues(X,Y,res)
    print(y_val)
    return jsonify({'X':x_val,'Y':y_val})
    
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
    
    

    
 #   plt.plot(data )
    #plt.plot(x2)
#plt.show()