import pandas as pd

data = {
    'akcja': ['Atak', 'Przyjęcie', 'Błąd'],
    'skutecznosc': [55, 60, 4]
}

df = pd.DataFrame(data)
print("Twoja pierwsza tabela w Pythonie:")
print(df)