import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

# Загружаем данные
train_data = pd.read_csv("data/train.csv")
test_data = pd.read_csv("data/test.csv")

# Проверяем и удаляем NaN
train_data.dropna(inplace=True)
test_data.dropna(inplace=True)

# Преобразуем в строковый формат
X_train = train_data["word_name"].astype(str)
y_train = train_data["class_name"]
X_test = test_data["word_name"].astype(str)

# Векторизация: n-граммы (2-3 буквы подряд)
vectorizer = CountVectorizer(analyzer="char", ngram_range=(2, 3))
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# Используем RandomForest для классификации
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train_vect, y_train)

# Делаем предсказания
predictions = model.predict(X_test_vect)

# Записываем результаты в CSV
output = pd.DataFrame({"word_name": X_test, "class_name": predictions})
output.to_csv("data/output.csv", index=False, line_terminator="\n")

print("Файл 'output.csv' успешно сохранен!")
