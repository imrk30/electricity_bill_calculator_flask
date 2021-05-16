from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def calorie():
    if request.method == 'POST':
        unit = request.form['units']
        units = float(unit)
        if(units>0 and units<=100):
            payAmount=units*0
            fixedcharge=0.00
        elif(units>100 and units<=200):
            payAmount=(100*0)+(units-100)*1.50
            fixedcharge=20.00
        elif(units>200 and units<=500):
            payAmount=(100*0)+(200-100)*2+(units-200)*3
            fixedcharge=30.00
        elif(units>500):
            payAmount=(100*0)+(200-100)*3.5+(500-200)*4.6+(units-500)*6.6
            fixedcharge=50.00
        else:
            payAmount=0;
            
        Total= payAmount+fixedcharge
        show = 'Consumed '+str(units)+' Units '+'\tBill Amount '+str(Total)
        return show
        # return render_template('result.html',Total=Total)
    else:
        return 'Sorry !!'

if __name__ == '__main__':
   app.run(debug=True)