import matplotlib.pyplot as plt

capital_initial = float(input("Quel est le capital initial ? (€)"))
taux = float(input("Quel est le taux de rendement annuel ? (%)")) / 100
duree = int(input("Quelle est la durée en années ?"))
versements_mensuels = float(input("Quels sont les versements réguliers mensuels ? (€)"))
versements_annuels = versements_mensuels * 12

capital_final = versements_annuels * (((1 + taux) ** duree - 1) / taux) * (1 + taux) + capital_initial * (1 + taux) ** duree
total_versements = versements_annuels * duree
gains = capital_final - total_versements - capital_initial # grâce à l'intérêt composé

print(f"Le capital final est de {capital_final:,.2f} €")
print(f"Le montant total des versements est de {total_versements:,.2f} €")
print(f"Les gains grâce aux intérêts composés sont de {gains:,.2f} €")


annees = list(range(duree + 1))
capital_sans_interets = [capital_initial + versements_annuels * annee for annee in annees]
capital_avec_interets = []

for annee in annees:
    capital = versements_annuels * (((1 + taux) ** annee - 1) / taux) * (1 + taux) + capital_initial * (1 + taux) ** annee
    capital_avec_interets.append(capital)

plt.plot(annees, capital_sans_interets, label='Sans intérêts composés')
plt.plot(annees, capital_avec_interets, label='Avec intérêts composés')
plt.xlabel('Années')
plt.ylabel('Capital (€)')
plt.title('Évolution du capital avec et sans intérêts composés')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
