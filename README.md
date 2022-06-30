# Chatbot-to-answer-customer-questions
Une application web avec un chatbot intégré pour répondre aux question des utilisateurs.
L'idée derrière ce projet est de créer une application pour répondre aux questions des clients d'une banque. 
Selon le type de question que l'utilisateur pose, différentes stratégies est adoptée pour lui rendre la réponse.

Dans notre cas nous avons limité le domaine d'utilisatation à la fiannce.

Parmi les types de questions nous avons : 
#1 Des questions liées aux comptes du clients : les réponses seront cherchées dans la base de donnée.

#2 Des questions liées à la banque : les réponses seront cherchées dans la base d'entrainement.

#3 Des quetions à la finance : les réponses seront scrapées sur internet.

Pour la construction du modèle, nous avons fait recours au NLP ainsi que Réseau de Neurone de propagation en avant.
Pour l'application web nous avons fait récours au flask, bien vrai qu'il existe quantité d'autres technologies qui pouvaient etre utilisées. Cechoix est justifiée du fait 
que le modèle est implementé en utilisant le python, donc histoire de rester dans le même bain.

Le dossier screenshoot contient des images rélatives aux étapes du développement.
