@app.route('/generate-tournament', methods=['POST'])
def generate_tournament():
    import pandas as pd
    from io import BytesIO

    data = request.json
    team_type = data['teamType']
    player_count = data['playerCount']
    match_count = data['matchCount']

    # Créer le DataFrame
    df = pd.DataFrame({
        'Match': list(range(1, match_count + 1)),
        'Joueurs': [f'Joueur {i + 1}' for i in range(player_count)]
    })

    # Charger les données dans un buffer mémoire
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Concours')
    output.seek(0)

    # Lecture pour validation ou traitement supplémentaire
    processed_data = pd.read_excel(output, sheet_name='Concours')
    print("Vérification des données : ", processed_data.head())  # Exemple de traitement

    # Recharger le buffer mémoire pour l'envoi
    output.seek(0)
    return send_file(output, as_attachment=True, download_name='concours_petanque.xlsx')
