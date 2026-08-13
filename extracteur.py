#Ce script suppose moins de 20 joueurs dans le challenge.


import json
import glob
import time
import gspread
import requests

code = input("Entrez le code d'invitation de votre ligue MPP : ")
token = input("Entrez votre token d'authentification MPP : ")
name = input("Entrez le nom exact de votre Google Sheet : ")


# Extraire la liste des utilisateurs depuis l'API MPP
headers = {
    "Authorization": "Bearer "+token,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."
}

url_api = "https://api.mpp.football/challenge-standings/users-standings?challengeId=mpp_challenge_"+code+"&offset=0&limit=20"

reponse = requests.get(url_api, headers=headers)

if reponse.status_code == 200:
        donnees = reponse.json()

        liste_utilisateurs = [(str(player["user"]["id"]),player["user"]["username"]) for player in donnees["standings"]]

# obtenir les fichiers JSON dans le répertoire courant

date = ["2026-06-14", "2026-06-19", "2026-06-24", "2026-06-29", "2026-07-04", "2026-07-09", "2026-07-14", "2026-07-19"]
date.reverse
club_id = [('mpp_championship_club_1025', 'Salernitana'), ('mpp_championship_club_1028', 'SM Caen'), ('mpp_championship_club_1041', 'Corée du Sud'), ('mpp_championship_club_1042', 'Iran'), ('mpp_championship_club_1057', 'Maroc'), ('mpp_championship_club_1078', 'Martigues'), ('mpp_championship_club_114', 'Angleterre'), ('mpp_championship_club_11426', 'FC Annecy'), ('mpp_championship_club_115', 'Écosse'), ('mpp_championship_club_1161', 'Angola'), ('mpp_championship_club_1163', 'AC Ajaccio'), ('mpp_championship_club_118', 'Espagne'), ('mpp_championship_club_119', 'Italie'), ('mpp_championship_club_120', 'Milan'), ('mpp_championship_club_121', 'Roma'), ('mpp_championship_club_1215', 'Algérie'), ('mpp_championship_club_1216', 'Nigeria'), ('mpp_championship_club_1218', 'Mali'), ('mpp_championship_club_1219', 'Ghana'), ('mpp_championship_club_1220', 'Burkina Faso'), ('mpp_championship_club_1221', 'Côte d’Ivoire'), ('mpp_championship_club_1222', 'RD Congo'), ('mpp_championship_club_1224', 'Tunisie'), ('mpp_championship_club_1225', 'Égypte'), ('mpp_championship_club_1226', 'Sénégal'), ('mpp_championship_club_1227', 'Zambie'), ('mpp_championship_club_123', 'Bologna'), ('mpp_championship_club_124', 'Cagliari'), ('mpp_championship_club_1245', 'Niort'), ('mpp_championship_club_125', 'Fiorentina'), ('mpp_championship_club_126', 'Verona'), ('mpp_championship_club_1264', 'Arabie saoudite'), ('mpp_championship_club_1266', 'Japon'), ('mpp_championship_club_127', 'Inter'), ('mpp_championship_club_1272', 'Grenoble'), ('mpp_championship_club_128', 'Juventus'), ('mpp_championship_club_129', 'Lazio'), ('mpp_championship_club_130', 'Lecce'), ('mpp_championship_club_1327', 'Haïti'), ('mpp_championship_club_1359', 'Ouzbékistan'), ('mpp_championship_club_136', 'Udinese'), ('mpp_championship_club_138', 'AJ Auxerre'), ('mpp_championship_club_139', 'SC Bastia'), ('mpp_championship_club_1395', 'OGC Nice'), ('mpp_championship_club_140', 'Bordeaux'), ('mpp_championship_club_141', 'Havre AC'), ('mpp_championship_club_142', 'RC Lens'), ('mpp_championship_club_1423', 'Reims'), ('mpp_championship_club_143', 'OL'), ('mpp_championship_club_1430', 'Amiens SC'), ('mpp_championship_club_144', 'OM'), ('mpp_championship_club_145', 'FC Metz'), ('mpp_championship_club_146', 'AS Monaco'), ('mpp_championship_club_147', 'Montpellier'), ('mpp_championship_club_148', 'AS Nancy Lorraine'), ('mpp_championship_club_149', 'Paris SG'), ('mpp_championship_club_150', 'Rennes'), ('mpp_championship_club_152', 'AS Saint-Étienne'), ('mpp_championship_club_1529', 'Cap-Vert'), ('mpp_championship_club_153', 'Strasbourg'), ('mpp_championship_club_154', 'Troyes'), ('mpp_championship_club_1717', 'Bénin'), ('mpp_championship_club_1727', 'Zimbabwe'), ('mpp_championship_club_1800', 'Irak'), ('mpp_championship_club_1804', 'Nouvelle-Zélande'), ('mpp_championship_club_1819', 'Botswana'), ('mpp_championship_club_1833', 'Guinée équatoriale'), ('mpp_championship_club_1837', 'Gabon'), ('mpp_championship_club_184', 'Rayo Vallecano'), ('mpp_championship_club_1843', 'Jordanie'), ('mpp_championship_club_1859', 'Mozambique'), ('mpp_championship_club_1869', 'Panama'), ('mpp_championship_club_1873', 'Qatar'), ('mpp_championship_club_1883', 'Soudan'), ('mpp_championship_club_1888', 'Tanzanie'), ('mpp_championship_club_1892', 'Ouganda'), ('mpp_championship_club_1983', 'Clermont'), ('mpp_championship_club_1996', 'VAFC'), ('mpp_championship_club_2128', 'Angers SCO'), ('mpp_championship_club_2129', 'Boulogne'), ('mpp_championship_club_2130', 'Dijon FCO'), ('mpp_championship_club_2182', 'Sassuolo'), ('mpp_championship_club_2298', 'Laval MFC'), ('mpp_championship_club_2336', 'Nimes O.'), ('mpp_championship_club_2338', 'Paris FC'), ('mpp_championship_club_2494', 'Comores'), ('mpp_championship_club_251', 'Benfica'), ('mpp_championship_club_2541', 'QRM'), ('mpp_championship_club_2544', 'GFC Ajaccio'), ('mpp_championship_club_3272', 'Concarneau'), ('mpp_championship_club_3288', 'Dunkerque'), ('mpp_championship_club_3308', 'Rodez AF'), ('mpp_championship_club_357', 'Allemagne'), ('mpp_championship_club_358', 'Roumanie'), ('mpp_championship_club_359', 'Portugal'), ('mpp_championship_club_360', 'Belgique'), ('mpp_championship_club_361', 'Suède'), ('mpp_championship_club_362', 'Turquie'), ('mpp_championship_club_363', 'Norvège'), ('mpp_championship_club_364', 'Serbie'), ('mpp_championship_club_365', 'Slovénie'), ('mpp_championship_club_366', 'Pays-Bas'), ('mpp_championship_club_367', 'Tchéquie'), ('mpp_championship_club_368', 'France'), ('mpp_championship_club_369', 'Danemark'), ('mpp_championship_club_427', 'Toulouse FC'), ('mpp_championship_club_428', 'EA Guingamp'), ('mpp_championship_club_429', 'LOSC'), ('mpp_championship_club_430', 'FC Nantes'), ('mpp_championship_club_456', 'Atalanta'), ('mpp_championship_club_459', 'Napoli'), ('mpp_championship_club_494', 'Cameroun'), ('mpp_championship_club_497', 'Suisse'), ('mpp_championship_club_507', 'Slovaquie'), ('mpp_championship_club_510', 'Ukraine'), ('mpp_championship_club_511', 'Pologne'), ('mpp_championship_club_515', 'Autriche'), ('mpp_championship_club_520', 'Géorgie'), ('mpp_championship_club_522', 'Afrique du Sud'), ('mpp_championship_club_534', 'Albanie'), ('mpp_championship_club_535', 'Croatie'), ('mpp_championship_club_537', 'Bosnie'), ('mpp_championship_club_538', 'Hongrie'), ('mpp_championship_club_5420', 'Pau FC'), ('mpp_championship_club_5447', 'Evian Thonon Gaillard'), ('mpp_championship_club_575', 'Australie'), ('mpp_championship_club_596', 'États-Unis'), ('mpp_championship_club_597', 'Canada'), ('mpp_championship_club_614', 'Brésil'), ('mpp_championship_club_632', 'Argentine'), ('mpp_championship_club_6512', 'Curaçao'), ('mpp_championship_club_659', 'Mexique'), ('mpp_championship_club_6783', 'Chambly'), ('mpp_championship_club_6785', 'Orléans'), ('mpp_championship_club_693', 'FCSM'), ('mpp_championship_club_694', 'FC Lorient'), ('mpp_championship_club_742', 'Monza'), ('mpp_championship_club_830', 'Équateur'), ('mpp_championship_club_832', 'Colombie'), ('mpp_championship_club_835', 'Paraguay'), ('mpp_championship_club_837', 'Uruguay'), ('mpp_championship_club_862', 'Brest'), ('mpp_championship_club_915', 'Red Star'), ('mpp_championship_club_920', 'Le Mans'), ('mpp_championship_club_921', 'Châteauroux'), ('mpp_championship_club_9830', 'TBC'), ('mpp_championship_club_990', 'Genoa'), ('mpp_championship_club_9990001', 'Decathlon')]


def get_data (date_curent, id_current):
    url_api = "https://api.mpp.football/user-match-forecasts/championship/8/history?userId="+id_current[0]+"&limitDays=5&beforeDate="+date_current
    # Lancement de la requête HTTP
    reponse = requests.get(url_api, headers=headers)

    if reponse.status_code == 200:
        donnees = reponse.json()

        # Enregistrement dans un fichier JSON
        with open(id_current[1]+"_"+date_curent+"_"+id_current[0]+".json", "w", encoding="utf-8") as fichier:
            json.dump(donnees, fichier, ensure_ascii=False, indent=4)

        print("Données sauvegardées avec succès dans " + id_current[1]+"_"+date_curent+"_"+id_current[0]+".json")
    else:
        print(f"Erreur {reponse.status_code}")

for id_current in liste_utilisateurs:
    for date_current in date:
        get_data(date_current, id_current)

# Le dictionnaire de traduction des clubs 
dictionnaire_clubs = dict(club_id)

def traduire_club(club_id):
    return dictionnaire_clubs.get(club_id, club_id)

# Connexion initiale à Google Sheets
try:
    gc = gspread.service_account(filename="credentials.json")
    sh = gc.open(name) # Nom exact de ton Google Sheet
except Exception as e:
    print(f"Erreur de connexion à Google Sheets : {e}")
    print("Assurez-vous que le fichier 'credentials.json' est présent et que le nom du Google Sheet est correct.")
    print("Assurez-vous que la feuille de calcul Google existe et est partagée avec l'adresse e-mail du compte de service en tant que propriétaire ou éditeur.")
    exit()

# La grande boucle par joueur
for user_id, pseudo in liste_utilisateurs:
    print(f"\n--- Traitement en cours pour {pseudo} ---")
    
    # On initialise le tableau vierge pour CE joueur
    lignes_tableau = [[
        "Date du Match", "Équipe Domicile", "Score Réel", "Équipe Extérieure", 
        "Cote Domicile", "Cote Nul", "Cote Extérieur", 
        "Prono Domicile", "Prono Extérieur", "Points Remportés"
    ]]

    # On cherche uniquement les fichiers contenant l'ID de ce joueur
    fichiers_joueur = glob.glob(f"*{user_id}*.json")
    
    if not fichiers_joueur:
        print(f"⚠️ Aucun fichier JSON trouvé pour {pseudo} ({user_id}). Ignoré.")
        continue

    # On parcourt les fichiers trouvés pour ce joueur
    for fichier in fichiers_joueur:
        with open(fichier, "r", encoding="utf-8") as f:
            donnees = json.load(f)
            
            if "matchesByDate" not in donnees:
                continue
                
            for date_jour, matchs in donnees["matchesByDate"].items():
                for match in matchs:
                    
                    date_propre = match["date"].replace("T", " ")[:16]
                    domicile_nom = traduire_club(match["home"]["clubId"])
                    score_domicile_reel = match["home"]["score"]
                    exterieur_nom = traduire_club(match["away"]["clubId"])
                    score_exterieur_reel = match["away"]["score"]
                    score_reel = f"{score_domicile_reel} - {score_exterieur_reel}"
                    cote_dom = match["quotations"]["home"]
                    cote_nul = match["quotations"]["draw"]
                    cote_ext = match["quotations"]["away"]
                    
                    # Le .get() qui a réglé notre problème précédent !
                    if match.get("userForecast") is not None:
                        prono_dom = match["userForecast"]["homeScore"]
                        prono_ext = match["userForecast"]["awayScore"]
                        points_gagnes = match["userForecast"]["points"]["total"]
                    else:
                        prono_dom = "-"
                        prono_ext = "-"
                        points_gagnes = 0
                        
                    ligne = [
                        date_propre, domicile_nom, score_reel, exterieur_nom, 
                        cote_dom, cote_nul, cote_ext, 
                        prono_dom, prono_ext, points_gagnes
                    ]
                    lignes_tableau.append(ligne)

    print(f"Extraction terminée : {len(lignes_tableau) - 1} matchs extraits.")

    # 5. Injection dans le bon onglet Google Sheets
    try:
        # On essaie d'ouvrir l'onglet au nom du joueur
        worksheet = sh.worksheet(pseudo)
    except gspread.exceptions.WorksheetNotFound:
        # S'il n'existe pas, on le crée (avec 1000 lignes et 10 colonnes par défaut)
        print(f"L'onglet '{pseudo}' n'existe pas, création en cours...")
        worksheet = sh.add_worksheet(title=pseudo, rows="1000", cols="10")
        
    # On nettoie et on met à jour
    worksheet.clear() 
    worksheet.update('A1', lignes_tableau)
    print(f"✅ Données envoyées avec succès dans l'onglet '{pseudo}' !")
    
    # Petite pause d'une seconde pour éviter que Google bloque le script pour "Spam" 
    # (Google limite le nombre de modifications qu'on peut faire par minute)
    time.sleep(1)

print("\n🎉 Tous les joueurs ont été traités !")
