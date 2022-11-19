import pickle
loaded_class = pickle. load(open('randomclass_chronic', 'rb'))
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')

@app.route("/index.html",methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/val",methods=['POST'])
def val():
    test=[]
    if request.method == 'POST':
        test.append(request.form.get("age"))
        test.append(request.form.get("bp"))
        test.append(request.form.get("sg"))
        test.append(request.form.get("al"))
        test.append(request.form.get("su"))
        
        rbc=request.form.get("rbc")
        if rbc=='yes':
            test.append(0)
        else:
            test.append(1)
            
        pc=request.form.get("pc")
        if pc=='yes':
            test.append(0)
        else:
            test.append(1)
            
        pcc=request.form.get("pcc")
        if pcc=='yes':
            test.append(1)
        else:
            test.append(0)
        
        ba=request.form.get("ba")
        if ba=='yes':
            test.append(1)
        else:
            test.append(0)
            
        test.append(request.form.get("bgr"))
        test.append(request.form.get("bu"))
        test.append(request.form.get("sc"))
        test.append(request.form.get("sod"))
        test.append(request.form.get("pot"))
        test.append(request.form.get("hemo"))
        test.append(request.form.get("pcv"))
        test.append(request.form.get("wc"))
        test.append(request.form.get("rc"))
        htn=request.form.get("htn")
        if htn=='yes':
            test.append(1)
        else:
            test.append(0)
            
        d=request.form.get("dm")
        if d==4:
            test.append(1)
        else:
            test.append(0)
            
        cad=request.form.get("cad")
        if cad=='yes':
            test.append(1)
        else:
            test.append(0)
            
        appet=request.form.get("appet")
        if appet=='yes':
            test.append(0)
        else:
            test.append(1)
        
        pe=request.form.get("pe")
        if pe=='yes':
            test.append(1)
        else:
            test.append(0)
            
        ane=request.form.get("ane")
        if ane=='yes':
            test.append(1)
        else:
            test.append(0)
        
    test_df=pd.DataFrame(test)
    test_df=np.array(test_df).reshape(1, -1)
    
    ans=loaded_class.predict(test_df)
    
    if int(ans)==1:
        return render_template('result_negative.html')
    else:
        return render_template('result_positive.html')
    
if __name__ == "__main__":
    app.debug=True
    app.run(debug=False)