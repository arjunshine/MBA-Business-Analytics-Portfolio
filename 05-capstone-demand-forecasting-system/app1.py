import pandas as pd
import os
cwd = os.getcwd()
os.chdir("C:\\Users\\Arjun\\Documents\\Trimester 5\\DEMAND_ANALYSIS [ PY ]")

from flask import Flask, request, jsonify, render_template
import layout_re as l
import model as mdl
import combi_forecast as cf
import orderquantity as oq
import mba_association as mba

pfp=pd.read_excel(r"file:///C:/Users/Arjun/Documents/Trimester 5/TRIAL/"
                  "DEMAND_ANALYSIS-DATA/New folder/working.xlsx",sep='\t',header=0)

app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/')
def home():
    return render_template('trial.html')

@app.route('/option', methods=["GET","POST"])
def option():
    errors = ""
    if request.method == "POST":
        number1 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])
        if number1 is not None:
            result = number1 
            return '''
                <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter the number of tables to analyze:</p>
                <form method="post" action=".">
                    <p><input name="number1" /></p>
                    <p><input type="submit" value="Analyze" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

if __name__ == "__main__":
    app.run(debug=True)

