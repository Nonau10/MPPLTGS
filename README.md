# MPPLTGS
Un extracteur qui vous permet de transférer les scores de votre ligue MPP vers un google sheets


Il vous faudra un dossier vide quand meme (ça cré bcp 2 fichier)

# Bot google
Faut un bot google pour aller modifier votre sheets, etdonc faute mttre le credentials.json a coté du extracteur.py. 
Je laisse Gemini vous expliqué : 

Étape 1 : Créer le projet et le Bot sur Google Cloud
C'est ici que tu vas déclarer ton script à Google.

Rends-toi sur la Console Google Cloud et connecte-toi avec ton compte Google.

Clique en haut à gauche pour Créer un nouveau projet (appelle-le "Script MPP" par exemple).

Dans le menu de gauche, va dans API et services > Bibliothèque.

Cherche et Active ces deux API pour ton projet :

Google Sheets API

Google Drive API

Étape 2 : Générer le fichier credentials.json
Maintenant que les API sont actives, on va créer le fameux bot.

Toujours dans API et services, clique sur l'onglet Identifiants (Credentials) à gauche.

En haut, clique sur Créer des identifiants > Compte de service.

Donne un nom à ton bot (ex: "bot-mpp") et clique sur Créer et continuer, puis sur OK (tu n'as pas besoin de lui donner de rôle spécifique).

Ton bot apparaît maintenant dans la liste en bas de la page. Clique sur l'adresse e-mail générée pour ce bot (elle ressemble à bot-mpp@script-mpp-1234.iam.gserviceaccount.com).

Va dans l'onglet Clés (Keys), clique sur Ajouter une clé > Créer une clé, et choisis le format JSON.

🎉 Un fichier va se télécharger sur ton ordinateur. Renomme-le credentials.json et place-le dans le même dossier que ton script Python.

Étape 3 : L'astuce magique (Partager ton tableau)
C'est l'erreur que tout le monde fait la première fois ! Ton script a maintenant une identité, mais par défaut, ce bot n'a accès à aucun fichier de ton Google Drive personnel.

Ouvre le fichier credentials.json que tu viens de télécharger avec le Bloc-notes ou VS Code.

Cherche la ligne "client_email" et copie l'adresse e-mail complète qui s'y trouve (celle qui finit par .gserviceaccount.com).

Ouvre ton tableau Google Sheets "Ma Ligue MPP" dans ton navigateur classique.

Clique sur le gros bouton Partager en haut à droite.

Colle l'adresse e-mail du bot et donne-lui les droits d'Éditeur.



# MPP informations
Faut aussi obtenir le code de votre ligue (c'est dans les reglage de ligue)

Et il vous faut aussi un token d'api, donc pour ça je laisse gemini s'exprimer : 

Connecte-toi sur la version web de Mon Petit Prono depuis ton ordinateur.

Ouvre les Outils de développement de ton navigateur (Touche F12 ou Ctrl+Maj+I) et va dans l'onglet Réseau (Network).

Recharge la page

Filtre les requêtes par Fetch/XHR. Tu devrais y voir passer une requête contenant des données.

Clique sur cette requête et récupère :

Les en-têtes (Headers) : cherche particulièrement un champ Authorization (qui contient ton token de session). Tu copies cette chaine de caractère bien longue et tu la gardes pour plus tard dans ton sac à dos.
