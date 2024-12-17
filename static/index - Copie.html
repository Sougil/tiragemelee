<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Générateur de Concours de Pétanque</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f0f4f8;
        }
    </style>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center">
    <div class="bg-white shadow-2xl rounded-xl p-8 w-full max-w-md">
        <h1 class="text-3xl font-bold text-center text-gray-800 mb-6">
            <i class="fas fa-dice mr-2 text-blue-600"></i>Générateur de Concours
        </h1>
        
        <form id="tournamentForm" class="space-y-4">
            <div>
                <label class="block text-gray-700 font-bold mb-2" for="teamType">
                    Type de Concours
                </label>
                <select id="teamType" class="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                    <option value="2">Doublette (2 joueurs par équipe)</option>
                    <option value="3">Triplette (3 joueurs par équipe)</option>
                </select>
            </div>
            
            <div>
                <label class="block text-gray-700 font-bold mb-2" for="playerCount">
                    Nombre de Joueurs
                </label>
                <input 
                    type="number" 
                    id="playerCount" 
                    min="4" 
                    max="100" 
                    class="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Minimum 4 joueurs"
                    required
                >
            </div>
            
            <div>
                <label class="block text-gray-700 font-bold mb-2" for="matchCount">
                    Nombre de Parties
                </label>
                <input 
                    type="number" 
                    id="matchCount" 
                    min="1" 
                    max="20" 
                    class="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Entre 1 et 20 parties"
                    required
                >
            </div>
            
            <button 
                type="submit" 
                class="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition duration-300 flex items-center justify-center"
            >
                <i class="fas fa-file-excel mr-2"></i>Générer le Fichier Excel
            </button>
        </form>
    </div>

    <script>
        document.getElementById('tournamentForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            // Récupérer les valeurs du formulaire
            const teamType = document.getElementById('teamType').value;
            const playerCount = document.getElementById('playerCount').value;
            const matchCount = document.getElementById('matchCount').value;
            
            // Vérifications de base
            if (playerCount < 4) {
                alert('Le nombre de joueurs doit être au minimum de 4.');
                return;
            }
            
            // Vérifier la compatibilité du nombre de joueurs avec le type d'équipe
            const minPlayers = teamType * 2;
            if (playerCount < minPlayers) {
                alert(`Pour une ${teamType === '2' ? 'doublette' : 'triplette'}, il faut au moins ${minPlayers} joueurs.`);
                return;
            }
            
            try {
                // Appeler le backend pour générer le fichier
                const response = await fetch('/generate-tournament', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        teamType: parseInt(teamType),
                        playerCount: parseInt(playerCount),
                        matchCount: parseInt(matchCount)
                    })
                });
                
                if (!response.ok) {
                    throw new Error('Erreur lors de la génération du fichier');
                }
                
                // Récupérer le fichier
                const blob = await response.blob();
                const filename = `concours_petanque_${teamType === '2' ? 'doublette' : 'triplette'}.xlsx`;
                
                // Créer un lien de téléchargement
                const link = document.createElement('a');
                link.href = window.URL.createObjectURL(blob);
                link.download = filename;
                link.click();
                
            } catch (error) {
                console.error('Erreur:', error);
                alert('Une erreur est survenue lors de la génération du fichier.');
            }
        });
    </script>
</body>
</html>