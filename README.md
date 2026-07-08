#RU
# House Prices Prediction

Привет! Это мой второй проект по машинному обучению. 
Задача классическая: предсказать стоимость дома на основе его характеристик (площадь, район, год постройки и т.д.).

## Честно об использовании AI

Сразу скажу прямо: я использовал нейросеть, чтобы написать базовый код для этого проекта. 
Я только начинаю свой путь в Data Science (сейчас 10 класс), и мне было важнее понять саму логику и пайплайн, чем тратить часы на поиск синтаксических ошибок.

**НО!** Я не просто копировал код. После того как нейросеть его выдавала, я садился и разбирал каждую строчку. Гуглил, почему мы заполняем пропуски именно медианой, а не средним, как работает `pd.get_dummies` и почему Random Forest тут подходит лучше линейной регрессии. 
Я до сих пор изучаю этот код, чтобы полностью понять внутреннюю кухню. Если вы найдете в коде что-то, что можно сделать лучше или оптимальнее — буду рад фидбеку в Issues!

## 🛠 Что я сделал в этом проекте

1. **Почистил данные:** Нашел и удалил выбросы (заметил два огромных дома с подозрительно низкой ценой, которые ломали модель).
2. **Обработал пропуски:** Заполнил `NaN` медианой для числовых признаков (она устойчивее к выбросам) и модой для текстовых.
3. **One-Hot Encoding:** Превратил текстовые категории (районы, типы домов) в числа. Из ~80 колонок получилось 246 признаков.
4. **Обучил модель:** Использовал `RandomForestRegressor`. 
5. **Сделал интерфейс:** Написал простое веб-приложение на **Streamlit**, чтобы можно было ввести параметры дома и получить предсказанную цену без запуска кода.

##  Стек технологий
- Python
- Pandas, NumPy
- Scikit-Learn (RandomForest, метрики)
- Matplotlib, Seaborn (для графиков)
- Streamlit (для веб-интерфейса)

## 🚀 Как запустить

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/AhmedovE1704/house-prices-prediction.git
   cd house-prices-prediction
2. Установите зависимости:
   pip install -r requirements.txt
3. Запустите веб-приложение:
   streamlit run app.py

#ENG
# House Prices Prediction

Hi! This is my second machine learning project. 
The classic task is to predict the value of a house based on its characteristics (area, area, year of construction, etc.).

## Be honest about using AI

I'll tell you straight away: I used a neural network to write the basic code for this project. 
I'm just starting my way into Data Science (now 10th grade), and it was more important for me to understand the logic and pipeline itself than to spend hours searching for syntax errors.

** BUT!** I didn't just copy the code. After the neural network gave it out, I sat down and parsed each line. I Googled why we fill in the gaps with the median rather than the average, how `pd.get_dummies` works, and why Random Forest is better suited to linear regression here. 
I'm still studying this code to fully understand the inner kitchen. If you find something in the code that can be done better or more optimally, I will be glad to receive feedback in Issues!

## 🛠 What I did in this project

1. **Cleaned up the data:** Found and removed the outliers (noticed two huge houses with suspiciously low prices that were breaking the model).
2. **Processed the omissions:** Filled in `NaN` with the median for numeric features (it is more resistant to outliers) and the mode for textual ones.
3. **One-Hot Encoding:** Turned text categories (neighborhoods, house types) into numbers. Out of ~80 columns, 246 features were obtained.
4. **Trained the model:** Used `RandomForestRegressor'. 
5. **Made the interface:** I wrote a simple web application on Streamlit so that I could enter the parameters of the house and get the predicted price without running the code.

## Technology stack
- Python
- Pandas, NumPy
- Scikit-Learn (randomForest, metrics)
- Matplotlib, Seaborn (for graphs)
- Streamlit (for the web interface)

## 🚀 How to launch

1. Clone the repository:
   ```bash
   git clone https://github.com/AhmedovE1704/house-prices-prediction.git
   cd house-prices-prediction
2. Install the dependencies:
   pip install -r requirements.txt
3. Launch the web application:
   streamlit run app.py

