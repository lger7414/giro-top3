from flask import Flask, jsonify, send_from_directory
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/top3')
def top3():
    url = 'https://www.eurosport.de/radsport/giro-d-italia/tabelle-gesamtwertung-ranking.shtml'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Beispielhafte Struktur – muss ggf. an die tatsächliche HTML-Struktur angepasst werden
    table = soup.find('table')
    rows = table.find_all('tr')[1:4]  # Überspringt die Kopfzeile und nimmt die nächsten 3 Zeilen

    result = []
    for row in rows:
        cols = row.find_all('td')
        name = cols[1].get_text(strip=True)
        time_diff = cols[2].get_text(strip=True)
        result.append({'name': name, 'time_diff': time_diff})

    return jsonify(result)
