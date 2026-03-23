# Sistema de Reconhecimento de Gestos & Laboratório de Visão Computacional

Este projeto contém um sistema para reconhecimento de gestos em tempo real e notebooks exploratórios para Visão Computacional. Faz parte da Aula 2 da NLW (Next Level Week) Operator da Rocketseat.

## 🚀 Sobre o Projeto
O projeto permite criar um sistema de reconhecimento de gestos customizado. O pipeline inclui coleta de dados de marcos da mão, treinamento de um classificador e inferência em tempo real via webcam.

**Tecnologias:**
- **Python**
- **OpenCV**: Captura e processamento de vídeo.
- **MediaPipe**: Extração de landmarks das mãos.
- **Scikit-Learn**: Treinamento do modelo (Random Forest).
- **uv**: Gerenciamento de ambiente e dependências.

---

## 📽️ Pipeline de Reconhecimento de Gestos

O fluxo é dividido em três scripts principais, localizados na pasta `src/`.

#### 1. Coleta de Dados (`src/collect_hand_data.py`)
Cria um dataset customizado capturando as coordenadas dos 21 marcos da mão(apagar arquivo csv para começar do 0).

**Uso:**
```bash
python src/collect_hand_data.py --label seu_gesto
```
- **`s`**: Salva um frame.
- **`r`**: Inicia/Para gravação contínua.
- **`q`**: Sai.

#### 2. Treinamento do Modelo (`src/train_gesture_model.py`)
Processa o arquivo `hand_landmarks_data.csv` e treina um classificador `RandomForest`. O script gera os arquivos `gesture_model.joblib` e `label_encoder.joblib`.

**Uso:**
```bash
python src/train_gesture_model.py
```

#### 3. Reconhecimento em Tempo Real (`src/webcam_object_detection.py`)
Utiliza a webcam para detectar mãos e classificar gestos em tempo real com o modelo treinado.

**Uso:**
```bash
python src/webcam_object_detection.py
```

---

## 📓 Notebooks Exploratórios

A pasta `notebooks/` contém implementações de outras subáreas da Visão Computacional:

- **`classify_with_timm.ipynb`**: Classificação de imagens com `timm` (MobileNetV3).
- **`huggingface_image_detection.ipynb`**: Detecção de objetos com `YOLOS` do Hugging Face.
- **`image_segmentation.ipynb`**: Segmentação de imagem baseada em texto.
- **`send_image_to_gemini.ipynb`**: Integração com a API do Google Gemini para análise de imagens.

---

## ⚙️ Instalação & Configuração

1. **Instalação**:
   Clone o repositório e sincronize as dependências:
   ```bash
   uv sync
   ```

2. **Download dos Modelos**:
   Para garantir que o sistema funcione, baixe os modelos pré-treinados do MediaPipe e coloque-os na pasta models:

   - **[gesture_recognizer.task](https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task)**: Essencial para extração de marcos das mãos.
   - **[efficientdet_lite0.tflite](https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite0/float16/1/efficientdet_lite0.tflite)**: Usado para detecção de objetos em notebooks auxiliares.

3. **Execução**:
   Siga os passos do "📽️ Pipeline de Reconhecimento de Gestos" para treinar e rodar seu modelo.

---

## 📂 Estrutura do Projeto
```
mediapipe-gesture-recognition/
├── src/
│   ├── collect_hand_data.py       # 1. Ferramenta de coleta de dados
|   ├── hand_landmarks_data.csv    # Dataset gerado
│   ├── train_gesture_model.py     # 2. Script de treinamento
│   └── webcam_object_detection.py # 3. Script de inferência em tempo real
├── notebooks/
│   ├── classify_with_timm.ipynb
│   ├── huggingface_image_detection.ipynb
│   └── ...
├── pyproject.toml            # Dependências do projeto
├── requirements.txt          # Dependências (pip)
└── README.md                 
```

