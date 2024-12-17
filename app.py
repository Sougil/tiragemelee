import os
from flask import Flask, request, send_file

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/generate-tournament', methods=['POST'])
def generate_tournament():
    import pandas as pd
    from io import BytesIO

    data = request.json
    team_type = data['teamType']
    player_count = data['playerCount']
    match_count = data['matchCount']

    df = pd.DataFrame({
        'Match': list(range(1, match_count + 1)),
        'Joueurs': [f'Joueur {i+1}' for i in range(player_count)]
    })

    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Concours')

    output.seek(0)
    return send_file(output, as_attachment=True, download_name='concours_petanque.xlsx')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render gère dynamiquement le port
    app.run(host='0.0.0.0', port=port)
