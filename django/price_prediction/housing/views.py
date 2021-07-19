from django.http import HttpResponse
from django.shortcuts import render
from joblib import dump, load
import numpy as np


def index(request):
    if(request.method == "GET"):      
        return render(request, "housing/index.html")
    else :
        method = request
        model = load("housing/templates/housing/Dragon.joblib")
        CRIM = assign("CRIM")
        ZN = assign("ZN")
        INDUS = assign("INDUS")
        CHAS = assign("CHAS")
        NOX = assign("NOX")
        RM = assign("RM")
        AGE = assign("AGE")
        DIS = assign("DIS")
        RAD = assign("RAD")
        TAX = assign("TAX")
        PTRATIO = assign("PTRATIO")
        B = assign("B")
        LSTAT = assign("LSTAT")
        result = model.predict(np.array([[CRIM,  ZN, INDUS, CHAS, NOX,
       RM, AGE,  DIS, RAD , TAX,
       PTRATIO,  B, LSTAT]]))[0]
        result = result * 1000
        return render(request, "housing/index.html", {'answer': result})


def assign(val) :
    ans = 0
    try :
        ans = float(request.POST[val])
    
    except(e) :
        ans = 0
    
    finally :
        return ans
    
    return ans