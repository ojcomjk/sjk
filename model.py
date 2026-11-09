from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

DATA_PATH = Path(__file__).resolve().parent / "insurance.csv"
FEATURES = ["age", "bmi", "smoker"]


def load_data():
    """GitHub 저장소에 포함된 insurance.csv를 읽어 옵니다."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            "insurance.csv 파일이 없습니다. model.py와 같은 폴더에 "
            "insurance.csv를 저장했는지 확인하세요."
        )

    df = pd.read_csv(DATA_PATH)

    required_columns = FEATURES + ["charges"]
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"CSV에 필요한 열이 없습니다: {missing}")

    # smoker: no=0, yes=1
    df = df.copy()
    df["smoker"] = df["smoker"].map({"no": 0, "yes": 1})
    df = df.dropna(subset=required_columns)

    X = df[FEATURES]
    y = df["charges"]
    return X, y


def train_model():
    """학습용/테스트용 데이터를 나누고 선형 회귀 모델을 학습합니다."""
    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=10
    )

    # 정규화와 회귀 모델을 하나의 파이프라인으로 구성합니다.
    # scaler는 훈련 데이터에만 fit되므로 테스트 데이터 정보가 미리 반영되지 않습니다.
    model = Pipeline(
        steps=[
            ("scaler", MinMaxScaler()),
            ("regression", LinearRegression()),
        ]
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    score = r2_score(y_test, predictions)

    return model, score


def predict_charges(model, age, bmi, smoker):
    """입력한 나이, BMI, 흡연 여부로 의료비를 예측합니다."""
    smoker_value = 1 if smoker else 0
    input_data = pd.DataFrame(
        [[age, bmi, smoker_value]],
        columns=FEATURES,
    )
    return float(model.predict(input_data)[0])
