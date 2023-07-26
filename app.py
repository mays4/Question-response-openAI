from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI
from flask import Flask, render_template,request,session,url_for,redirect
app = Flask(__name__,template_folder="templetes",static_folder="staticFiles")
import os

load_dotenv(find_dotenv())
secret_key = os.environ.get('SECRET_KEY')
app.secret_key = secret_key
@app.route("/")
def index():

    session.pop('response', None)
    return render_template("index.html")

@app.route("/get_response",methods=['POST'])
def get_response():
 
  
    llm = OpenAI(model_name="text-davinci-003")  
    prompt = request.form['question']  
    response=llm(prompt)
    session['response']=response
    session['question']=prompt
    return redirect(url_for('show_response'))

@app.route('/show_response')
def show_response():
    
    response = session.pop('response', None)
    question=session.pop('question',None)
    return render_template('index.html' ,question=question, response=response)

     
    

if __name__ == "__main__":
    app.run(debug=True)