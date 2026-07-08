import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')

# Заполнить пропуски средним значением
df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].mean())
# 1. Смотрим, какие колонки остались с пропусками (если есть)


# # 2. Заполняем оставшиеся пропуски медианой (для числовых) и модой (для текстовых)
# # Числовые колонки
# numeric_cols = df.select_dtypes(include=['number']).columns
# for col in numeric_cols:
#     if df[col].isna().sum() > 0:
#         df[col] = df[col].fillna(df[col].median())

# # Текстовые колонки
# object_cols = df.select_dtypes(include=['object']).columns
# for col in object_cols:
#     if df[col].isna().sum() > 0:
#         df[col] = df[col].fillna(df[col].mode()[0])



# # 3. Превращаем текстовые признаки в числа (One-Hot Encoding)
# df = pd.get_dummies(df, columns=object_cols, drop_first=True)



# # 4. Разделяем на X (признаки) и y (целевая переменная - цена)
# X = df.drop('SalePrice', axis=1)  # всё, кроме цены
# y = df['SalePrice']              # только цена



# # 5. Разделяем на train и test (80% для обучения, 20% для проверки)
# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# print(f"\nTrain set: {X_train.shape[0]} домов")
# print(f"Test set: {X_test.shape[0]} домов")
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# import numpy as np

# # 1. Создаём модель
# model = RandomForestRegressor(n_estimators=100, random_state=42)

# # 2. Обучаем модель на тренировочных данных
# model.fit(X_train, y_train)

# print("✅ Модель обучена!")
import joblib

# 1. Сохраняем саму модель
joblib.dump(model, 'house_price_model.pkl')

# 2. Сохраняем список признаков (ОЧЕНЬ ВАЖНО!)
# Так как мы делали One-Hot Encoding, у нас 245 колонок. 
# Модель должна знать их порядок.
joblib.dump(X.columns, 'model_features.pkl')

print("✅ Модель и признаки сохранены!")
# Загружаем модель обратно из файла
loaded_model = joblib.load('house_price_model.pkl')
loaded_features = joblib.load('model_features.pkl')

# Создаём новый дом (ДАННЫЕ ДОЛЖНЫ СОВПАДАТЬ С ТЕМИ, НА КОТОРЫХ ОБУЧАЛИ!)
# Для примера возьмём первую строку из тестовой выборки
new_house = X_test.iloc[[0]] 

# Делаем предсказание
predicted_price = loaded_model.predict(new_house)

print(f"🏠 Реальная цена этого дома: ${y_test.iloc[0]:,.0f}")
print(f"🤖 Модель предсказала цену: ${predicted_price[0]:,.0f}")






# # 3. Делаем предсказания на тестовой выборке
# y_pred = model.predict(X_test)

# print(f"\nПредсказания сделаны для {len(y_pred)} домов")
# # Считаем метрики
# mae = mean_absolute_error(y_test, y_pred)
# rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# r2 = r2_score(y_test, y_pred)

# print("=" * 50)
# print("📊 РЕЗУЛЬТАТЫ МОДЕЛИ")
# print("=" * 50)
# print(f"MAE (средняя ошибка): ${mae:,.0f}")
# print(f"RMSE (среднеквадратичная ошибка): ${rmse:,.0f}")
# print(f"R² (коэффициент детерминации): {r2:.3f}")
# print("=" * 50)

# # Интерпретация
# print("\n💡 ЧТО ЭТО ЗНАЧИТ:")
# print(f"- Модель ошибается в среднем на ${mae:,.0f} за дом")
# print(f"- R² = {r2:.3f} означает, что модель объясняет {r2*100:.1f}% вариации цен")
# # График: Реальные цены vs Предсказанные
# plt.figure(figsize=(10, 6))
# plt.scatter(y_test, y_pred, alpha=0.5, color='blue')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', linewidth=2, label='Идеальное предсказание')
# plt.title('Реальные цены vs Предсказанные', fontsize=16, fontweight='bold')
# plt.xlabel('Реальная цена ($)', fontsize=12)
# plt.ylabel('Предсказанная цена ($)', fontsize=12)
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.show()

# # Гистограмма ошибок
# errors = y_test - y_pred
# plt.figure(figsize=(10, 6))
# plt.hist(errors, bins=30, color='coral', edgecolor='black')
# plt.title('Распределение ошибок предсказания', fontsize=16, fontweight='bold')
# plt.xlabel('Ошибка ($)', fontsize=12)
# plt.ylabel('Количество домов', fontsize=12)
# plt.axvline(0, color='red', linestyle='--', linewidth=2)
# plt.show()
# # Получаем важность признаков
# feature_importance = pd.DataFrame({
#     'Признак': X.columns,
#     'Важность': model.feature_importances_
# }).sort_values('Важность', ascending=False)

# print("🏆 ТОП-10 признаков, влияющих на цену:")
# print(feature_importance.head(10))

# # Визуализация
# plt.figure(figsize=(10, 8))
# top_10 = feature_importance.head(10)
# plt.barh(range(len(top_10)), top_10['Важность'], color='skyblue')
# plt.yticks(range(len(top_10)), top_10['Признак'])
# plt.title('Топ-10 признаков, влияющих на цену', fontsize=16, fontweight='bold')
# plt.xlabel('Важность', fontsize=12)
# plt.ylabel('Признак', fontsize=12)
# plt.tight_layout()
# plt.show()
# sns.set_style("whitegrid")
# plt.rcParams['figure.figsize'] = (12, 6)
# # гистограмма цены
# plt.figure(figsize=(10, 6))
# plt.hist(df['SalePrice'], bins=50, color='skyblue', edgecolor='black')
# plt.title('Распределение цен на дома', fontsize=16, fontweight='bold')
# plt.xlabel('Цена ($)', fontsize=12)
# plt.ylabel('Количество домов', fontsize=12)
# plt.axvline(df['SalePrice'].mean(), color='red', linestyle='--', label=f'Средняя: ${df["SalePrice"].mean():,.0f}')
# plt.legend()
# plt.show()

# # корреляция признаков с ценой
# plt.figure(figsize=(10, 6))
# numeric_df = df.select_dtypes(include=['number']) 
# correlation = numeric_df.corr()['SalePrice'].drop('SalePrice').sort_values(ascending=False)
# correlation.head(10).plot(kind='barh', color='coral')
# plt.title('Топ-10 признаков, влияющих на цену', fontsize=16, fontweight='bold')
# plt.xlabel('Корреляция с ценой', fontsize=12)
# plt.ylabel('Признак', fontsize=12)
# plt.tight_layout()
# plt.show()

# # площадь vs цена 
# plt.figure(figsize=(10, 6))
# plt.scatter(df['GrLivArea'], df['SalePrice'], alpha=0.5, color='green')
# plt.title('Площадь дома vs Цена', fontsize=16, fontweight='bold')
# plt.xlabel('Надземная площадь (кв. футы)', fontsize=12)
# plt.ylabel('Цена ($)', fontsize=12)
# plt.show()

# # цена по качеству дома
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=df, x='OverallQual', y='SalePrice', palette='viridis')
# plt.title('Цена в зависимости от качества дома', fontsize=16, fontweight='bold')
# plt.xlabel('Качество дома (1-10)', fontsize=12)
# plt.ylabel('Цена ($)', fontsize=12)
# plt.show()

# # cохраняем количество строк ДО удаления
# rows_before = len(df)

# # удаляем дома с площадью больше 4000 кв. футов и ценой ниже 300000
# df = df[~((df['GrLivArea'] > 4000) & (df['SalePrice'] < 300000))]

# # сохраняем количество строк ПОСЛЕ удаления
# rows_after = len(df)

# print(f"Удалено строк: {rows_before - rows_after}")
# print(f"Осталось строк: {rows_after}")

# # находим дома с площадью больше 4000 кв. футов
# outliers = df[df['GrLivArea'] > 4000][['GrLivArea', 'SalePrice', 'OverallQual', 'Neighborhood']]
# print("Выбросы (большие дома с подозрительной ценой):")
# print(outliers)



# # визуализируем их на графике
# plt.figure(figsize=(10, 6))
# plt.scatter(df['GrLivArea'], df['SalePrice'], alpha=0.5, color='green', label='Обычные дома')
# plt.scatter(outliers['GrLivArea'], outliers['SalePrice'], color='red', s=100, label='Выбросы')
# plt.title('Выбросы: большие дома с низкой ценой', fontsize=16, fontweight='bold')
# plt.xlabel('Площадь (кв. футы)', fontsize=12)
# plt.ylabel('Цена ($)', fontsize=12)
# plt.legend()
# plt.show()
