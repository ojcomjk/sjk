import streamlit as st

from model import predict_charges, train_model

st.set_page_config(
    page_title="의료비 예측 앱",
    page_icon="🩺",
    layout="centered",
)


@st.cache_resource
def get_model():
    return train_model()


st.title("🩺 의료비(charges) 예측 앱")
st.write(
    "나이, BMI, 흡연 여부를 입력하면 선형 회귀 모델이 "
    "예상 의료비를 계산합니다."
)

try:
    model, r2 = get_model()
except Exception as error:
    st.error(f"모델을 준비하는 중 문제가 발생했습니다: {error}")
    st.stop()

st.subheader("입력값")

age = st.number_input(
    "나이 (age)",
    min_value=18,
    max_value=100,
    value=30,
    step=1,
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0,
    step=0.1,
)

smoker_label = st.selectbox(
    "흡연 여부 (smoker)",
    options=["비흡연(no)", "흡연(yes)"],
)
smoker = smoker_label == "흡연(yes)"

if st.button("의료비 예측하기", type="primary", use_container_width=True):
    predicted_charges = predict_charges(model, age, bmi, smoker)

    st.success("예측이 완료되었습니다.")
    st.metric(
        label="예상 의료비 (charges)",
        value=f"${predicted_charges:,.2f}",
    )
    st.caption(
        "이 값은 제공된 데이터와 선형 회귀 모델을 바탕으로 한 추정치이며, "
        "실제 의료비 또는 보험료를 보장하지 않습니다."
    )

with st.expander("모델 성능 확인하기"):
    st.write(f"테스트 데이터 결정계수(R²): **{r2:.4f}**")
    st.caption(
        "R²는 테스트 데이터의 실제 charges와 예측 charges가 얼마나 "
        "잘 맞는지를 나타내는 지표입니다. 1에 가까울수록 설명력이 높습니다."
    )

st.divider()
st.caption("학습 데이터: GitHub 저장소에 포함된 insurance.csv")
