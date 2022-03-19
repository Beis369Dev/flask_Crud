from flask import Flask,render_template, request,redirect,url_for,flash
import pymysql


app=Flask(__name__)


## Objeto de Coneccion a MySql y Obj. Cursor 
DB= pymysql.connect(host='localhost',user='root',passwd='',database='pag2')

cursor=DB.cursor()

app.secret_key='mysecretkey'

#-------------------------------------Rutas-------------------------------------------------------------
#-----Index---------------
@app.route('/')
def Index():
    cursor.execute('SELECT * FROM `user_db`')
    data=cursor.fetchall()
    return render_template('index.html',datainfo=data)



#-------------AddContact------------------------------------
@app.route('/add_contact', methods=['POST'])
def AddContact():
    if request.method=='POST':
        Name = request.form['Name']
        LastName = request.form['LastName']
        Cedula = request.form['C.I']
        
        cursor.execute('INSERT INTO user_db(Name,LastName,CI) VALUES(%s,%s,%s)'
        ,(Name,LastName,Cedula))
        DB.commit()
        flash('Infromacion Agregada')
        
        

        return redirect(url_for('Index'))



        



##----------------------Edit-------------------------
@app.route('/edit/<id>')
def get_data(id):
    cursor.execute("SELECT * FROM `user_db` WHERE id= %s",(id))
    Dquery=cursor.fetchall()
    return render_template('edit_data.html', get_Query=Dquery[0])

@app.route('/save_data/<id>',methods=['POST'])
def save_data(id):
    if request.method=='POST':
        Name=  request.form['Name']
        LastName = request.form['LastName']
        Cedula = request.form['C.I']
        cursor.execute(""" UPDATE user_db SET
        Name=%s , LastName= %s , CI= %s WHERE id = %s """,
        (Name,LastName,Cedula,id))
        DB.commit()
        flash("Los Datos Fueron Actualizados")
    return redirect(url_for('Index'))





#------------------Delet----------------------------------
@app.route('/delet/<string:id>')
def Delet(id):
    cursor.execute('DELETE FROM `user_db` WHERE id =  %s',(id))
    DB.commit()
    flash('Registro Borrado')
    return redirect(url_for('Index'))





#--------------------App_Run()--------------------------
if __name__=='__main__':
    app.run(port=80,debug=True)








#-----------------------------------------Finish_Program----------------------------------------------