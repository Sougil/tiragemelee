import os
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import pandas as pd
from io import BytesIO

app = Flask(__name__, static_folder='static')
CORS(app)  # Ajout de CORS pour éviter les problèmes de requêtes cross-origin

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/generate-tournament', methods=['POST'])
def generate_tournament():
    try:
        # Récupérer les données JSON envoyées par le client
        data = request.json
        if not data:
            return jsonify({"error": "Requête JSON manquante ou mal formée"}), 400

        team_type = data.get('teamType')
        player_count = data.get('playerCount')
        match_count = data.get('matchCount')

        # Validation des données
        if not all([team_type, player_count, match_count]):
            return jsonify({"error": "Tous les champs requis (teamType, playerCount, matchCount) doivent être fournis"}), 400

        if player_count < 4:
            return jsonify({"error": "Le nombre de joueurs doit être au minimum de 4"}), 400

        if match_count < 1:
            return jsonify({"error": "Le nombre de matchs doit être au minimum de 1"}), 400

        # Vérifier la compatibilité entre le type d'équipe et le nombre de joueurs
        min_players = team_type * 2
        if player_count < min_players:
            return jsonify({
                "error": f"Pour une {'doublette' if team_type == 2 else 'triplette'}, il faut au moins {min_players} joueurs."
            }), 400

        # Génération du tableau des matchs
        df = pd.DataFrame({
            'Match': [f'Match {i + 1}' for i in range(match_count)],
            'Joueurs': [f'Joueur {i % player_count + 1}' for i in range(match_count)]
        })

        # Création du fichier Excel
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Concours')

        output.seek(0)

        # Retourner le fichier généré
        return send_file(output, as_attachment=True, download_name='concours_petanque.xlsx')

    except Exception as e:
        return jsonify({"error": f"Erreur interne : {str(e)}"}), 500


if __name__ == '__main__':
    # Port configuré pour Render, avec un fallback à 5000 en local
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
