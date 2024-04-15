# Guide de Contribution au projet REPO-PYTHON
Merci de contribuer au projet REPO-PYTHON! suivez les étapes ci-dessous pour proposer bos modifications via Git Flow et une merge request.

## Etapes à suivre:

1. Cloner le projet:
Clonez le projet sur votre machine locale en utilisant la commande suivante:
`git clone <URL_du_projet>`

2. Créer une branche:
Créez une nouvelle branche à partir de la branche 'main' avec le préfixe 'feature/' ou 'bugfix/' suivi d'un nom signifiant pour votre fonctionnalité ou bugfix:
`git checkout -b feature/nom_de_ma_fonctionnalite`

3. Faire des modifications
Faites vos modifications dans la branche 'feature/nom_de_ma_fonctionnalite'.
Assurez-vous de bien suivre les conventions de codage et de documentation du projet.

4. Ajouter et valider les modifications:
Ajouter vos modifications à l'index et valider les localement en utilisant les commandes suivantes
`git add .`
`git commit -m feat(composant): description concise des modifications`

5. Poussez les Modifications:
Poussez la branche avec vos modifications sur le dépôt distant
`git push origin feature/nom_de_ma_fonctionalite`

6. Créer une merge request:
Rendez-vous sur la page du dépôt et créer une nouvelle merge request (MR) en selectionnant votre branche 'feature/nom_de_ma_fonctionalite' comme branche source et la branche 'main' comme branche cible.

7. Atteindre la révision:
Attendez que les relecteurs examinent vos modifications et apportent des commentairesou des demandes de modifications si nécessaire.

8. Fusionner la MR:
Une fois que la MR est approuvée. un mainteneur fusionnera vos modifications dans la branche 'main'. Assurez-vous de supprimer la branche de fonctionnalité locale et distante une fois fusionnée.

Félicitations! Vous avez contribué avec succès au projet REPO-PYTHON en utilisant Git Flow.

