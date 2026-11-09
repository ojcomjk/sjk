# ML_Project - 의료비 예측 웹 앱

`insurance.csv` 데이터로 선형 회귀 모델을 학습하고, 사용자가 입력한 `age`, `bmi`, `smoker` 값으로 `charges`를 예측하는 Streamlit 앱입니다.

## 1. 저장소 파일 구성

```text
ML_Project/
│
├── model.py
├── app.py
├── requirements.txt
├── insurance.csv
└── README.md
```

> 기존 예시의 `water_potability.csv`가 아니라, 이 프로젝트에서 실제 사용하는 `insurance.csv`를 저장소에 넣어야 합니다.

## 2. GitHub에 올리기

1. GitHub에서 새 Repository를 만듭니다. 이름은 `ML_Project`로 지정할 수 있습니다.
2. 위 파일 5개를 Repository의 최상위 폴더에 업로드합니다.
3. 특히 `insurance.csv`도 반드시 함께 업로드합니다. 앱 방문자는 CSV를 직접 업로드하지 않습니다.

## 3. Streamlit Community Cloud로 공개하기

1. https://share.streamlit.io/ 에 접속합니다.
2. GitHub 계정으로 로그인하고 Streamlit 접근을 승인합니다.
3. **Create app**을 선택합니다.
4. Repository: `ML_Project`
5. Branch: `main` (실제 사용하는 브랜치 선택)
6. Main file path: `app.py`
7. **Deploy**를 누릅니다.

배포가 완료되면 Streamlit이 제공하는 웹 주소를 다른 사람에게 공유할 수 있습니다.

## 4. 내 컴퓨터에서 실행하기

프로젝트 폴더에서 다음 명령어를 실행합니다.

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 5. 모델 작동 순서

1. `model.py`가 같은 폴더의 `insurance.csv`를 읽습니다.
2. `smoker` 값을 비흡연 `0`, 흡연 `1`로 변환합니다.
3. `age`, `bmi`, `smoker`를 독립변수 X로, `charges`를 종속변수 y로 사용합니다.
4. 훈련 데이터와 테스트 데이터를 7:3으로 나눕니다.
5. Min-Max 정규화와 선형 회귀 모델을 학습합니다.
6. 앱 화면에서 입력한 세 값으로 `charges`를 예측합니다.

정규화는 학습 데이터에만 맞추고 테스트/새 입력 데이터에는 같은 변환을 적용하도록 Pipeline을 사용했습니다.

## 참고

- 이 앱은 교육 및 실습용 예측 모델입니다.
- 예측값은 데이터에 기반한 추정치이며 실제 의료비나 보험료를 보장하지 않습니다.
- `insurance.csv`는 공개 저장소에 포함되므로 누구나 내려받을 수 있습니다. 데이터의 출처와 사용 조건을 확인한 뒤 공개하세요.
