from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)
@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")
  
@app.route('/paris/')
def meteo():
    response = urlopen('https://api.openweathermap.org/data/2.5/forecast/daily?q=Paris,fr&cnt=16&appid=bd5e378503939ddaee76f12ad7a97608')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('temp', {}).get('day') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)



@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def monhistogramme():
    return render_template("histogramme.html")


@app.route('/commits/')
def show_commits():
    return render_template('commits.html')


@app.route('/api/commits/data')
def get_commits_data():
    response = requests.get('https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits')
    commits_data = response.json()


    data = [['Minute', 'Commits']]
    commit_counts = {}
    for commit in commits_data:
        commit_time = datetime.strptime(commit['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ')
        minute = commit_time.strftime('%Y-%m-%d %H:%M')
        commit_counts[minute] = commit_counts.get(minute, 0) + 1


    for minute, count in sorted(commit_counts.items()):
        data.append([minute, count])

    return jsonify(data)



                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #Comm2
  
if __name__ == "__main__":
  app.run(debug=True)
