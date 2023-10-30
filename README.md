# 감정 분석기

이 프로젝트는 감정 분석 알고리즘을 통해 대화를 통해 감정을 파악하고, 특히 취약한 계층인 독거 노인의 위험도를 측정하는 목표를 가지고 있습니다. 이 프로젝트는 1학년 챗봇과 감정 분석 알고리즘을 융합한 것입니다.

## 모델 설명

### 모델 1

**모델 유형:** Sequential

**모델 구조:**
- Conv2D Layer (32 필터)
- Conv2D Layer (64 필터)
- MaxPooling2D Layer
- Dropout Layer
- Conv2D Layer (128 필터)
- MaxPooling2D Layer
- Dropout Layer
- Conv2D Layer (256 필터)
- MaxPooling2D Layer
- Dropout Layer
- Flatten Layer
- Dense Layer (512 뉴런)
- Dropout Layer
- Dense Layer (6 뉴런)

**학습 데이터:** [Kaggle Emotion Detection Dataset](https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer)

**하이퍼파라미터:**
- Epoch: 15
- Batch Size: 32

**성능:**
- 정확도 (Accuracy): 0.80
- 검증 정확도 (Validation Accuracy): 0.65

### 모델 2

**학습 데이터:** [Kaggle Emotion Detection Dataset](https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer) (Google Teachable Machine을 사용하여 학습)

## 기간

프로젝트 진행 기간: ~2023/12/22
