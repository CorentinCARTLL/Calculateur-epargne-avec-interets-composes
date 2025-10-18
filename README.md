## Calculateur d’Épargne avec Intérêts Composés

Ce projet simule et visualise l’évolution d’un capital placé sur plusieurs années en tenant compte des **intérêts composés**.  
Il est composé de deux parties complémentaires :
- Une **version web interactive** (HTML, CSS, JavaScript, Chart.js)
- Une **version console Python** (matplotlib)

L’objectif est de comparer deux approches d’accumulation de capital :
-  **Sans intérêts composés** : simple cumul des versements (croissance linéaire)
-  **Avec intérêts composés** : réinvestissement des gains chaque année (croissance exponentielle)

L’utilisateur peut saisir :
-  un capital initial  
-  un taux de rendement annuel (%)  
-  une durée d’investissement (années)  
-  un versement mensuel régulier  

Le programme calcule le capital final selon la formule :

\[
C_f = V_a \times \frac{(1 + r)^n - 1}{r} \times (1 + r) + C_i \times (1 + r)^n
\]

où :
- \(C_f\) : capital final  
- \(V_a\) : versements annuels  
- \(r\) : taux d’intérêt annuel  
- \(n\) : durée en années  
- \(C_i\) : capital initial  

Les résultats sont affichés sous forme numérique et graphique, illustrant clairement la différence entre une épargne simple et une épargne à intérêts composés.

### Compétences mobilisées
- Développement **front-end** : HTML, CSS, JavaScript, Chart.js  
- Programmation **Python** pour la simulation et la visualisation (matplotlib)  
- Application des **formules financières** d’intérêts composés  
- Création d’interfaces et de graphiques interactifs  
- Structuration d’un **mini-projet éducatif et financier complet**

### Aperçu
- **Interface Web** : saisie des données + graphique dynamique (avec/sans intérêts composés)  
- **Console Python** : simulation textuelle + tracé des deux courbes avec matplotlib
