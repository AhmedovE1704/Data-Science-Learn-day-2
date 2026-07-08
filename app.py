import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. Заголовок и описание
st.title("🏠 Предсказание цены дома")
st.write("Введите характеристики дома, и нейросеть оценит его стоимость!")

# 2. Загружаем модель и список признаков (те самые 245 колонок)
model = joblib.load('house_price_model.pkl')
features = joblib.load('model_features.pkl')

# 3. Создаём интерфейс (пользователь вводит данные)
st.subheader("Характеристики дома:")
overall_qual = st.slider("Общее качество дома (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Надземная площадь (кв. футы)", 500, 5000, 1500)
garage_cars = st.slider("Количество мест в гараже", 0, 4, 2)

# 4. Кнопка расчёта
if st.button("Рассчитать цену"):
    
    # Создаём пустую таблицу со всеми 245 признаками и заполняем нулями
    input_data = pd.DataFrame(np.zeros((1, len(features))), columns=features)
    
    # Вписываем данные от пользователя в нужные колонки
    # (Названия колонок должны в точности совпадать с теми, что были при обучении!)
    input_data['OverallQual'] = overall_qual
    input_data['GrLivArea'] = gr_liv_area
    input_data['GarageCars'] = garage_cars
    
    # Делаем предсказание
    prediction = model.predict(input_data)
    
    # Выводим красивый результат
    st.success(f"💰 Предсказанная цена дома: ${prediction[0]:,.0f}")
    
    # Добавим немного контекста
    st.info(f"Для дома площадью {gr_liv_area} кв. футов, качеством {overall_qual}/10 и {garage_cars} местами в гараже.")