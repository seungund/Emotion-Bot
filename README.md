# 감정 분석기

감정분석 알고리즘을 통해 대화만으로 감정파악 (1학년 챗봇과 감정분석 알고리즘을 융합) 독거노인 같은 취약계층의 위험도 측정

## 모델 설명

### 모델 1

Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 46, 46, 32)        320       
                                                                 
 conv2d_1 (Conv2D)           (None, 44, 44, 64)        18496     
                                                                 
 max_pooling2d (MaxPooling2  (None, 22, 22, 64)        0         
 D)                                                              
                                                                 
 dropout (Dropout)           (None, 22, 22, 64)        0         
                                                                 
 conv2d_2 (Conv2D)           (None, 20, 20, 128)       73856     
                                                                 
 max_pooling2d_1 (MaxPoolin  (None, 10, 10, 128)       0         
 g2D)                                                            
                                                                 
 dropout_1 (Dropout)         (None, 10, 10, 128)       0         
                                                                 
 conv2d_3 (Conv2D)           (None, 8, 8, 256)         295168    
                                                                 
 max_pooling2d_2 (MaxPoolin  (None, 4, 4, 256)         0         
 g2D)                                                            
                                                                 
 dropout_2 (Dropout)         (None, 4, 4, 256)         0         
                                                                 
 flatten (Flatten)           (None, 4096)              0         
                                                                 
 dense (Dense)               (None, 512)               2097664   
                                                                 
 dropout_3 (Dropout)         (None, 512)               0         
                                                                 
 dense_1 (Dense)             (None, 6)                 3078      
                                                                 
=================================================================
Total params: 2488582 (9.49 MB)
Trainable params: 2488582 (9.49 MB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________

학습 데이터 : https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer 이미지 사용

epoch = 15, batch_size = 32

accuracy : 0.80

val_accuracy : 0.65

### 모델 2

학습 데이터 : https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer 이미지 사용

Google Teachable Machine을 사용하여 학습


## 기간
~2023/12/22