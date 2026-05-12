import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# data = {
#     'akcja': ['Atak', 'Przyjęcie', 'Błąd'],
#     'skutecznosc': [55, 60, 4]
# }

# df = pd.DataFrame(data)
# print("Twoja pierwsza tabela w Pythonie:")
# print(df)

df = pd.read_csv('mecze.csv')

srednie_bledy = df['bledy'].mean()
print(f"Średnia liczba błędów w bazie: {srednie_bledy}")

# Cechy (wszystko poza wynikiem i nazwą drużyny)
X = df[['atak_skutecznosc', 'przyjecie_skutecznosc', 'bledy']]

# Cel (tylko kolumna wynik)
y = df['wynik']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Liczba meczów do nauki: {len(X_train)}")
print(f"Liczba meczów do testu: {len(X_test)}")

model = LogisticRegression()

model.fit(X_train, y_train)

print("Model został wytrenowany")

predictions = model.predict(X_test)

print(f"Przewidziane wyniki: {predictions}")
print(f"Rzeczywiste wyniki:  {y_test.values}")