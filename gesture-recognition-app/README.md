# Aplicação de Reconhecimento de Gestos 

Este projeto é uma aplicação web construída com FastHTML que utiliza MediaPipe e um modelo de Machine Learning customizado para reconhecer gestos da mão em tempo real através da webcam. Faz parte da Aula 3 da NLW (Next Level Week) Operator da Rocketseat.

O projeto combina um backend em Python para processamento de imagem com um frontend simples para exibir o vídeo e os resultados da classificação.

**Tecnologias:**
- **FastHTML**: Para a construção da interface web com Python.
- **MediaPipe**: Para detecção dos landmarks da mão.
- **OpenCV**: Para manipulação de imagem.
- **Scikit-Learn**: Para o modelo de classificação de gestos.
- **uv**: Para gerenciamento de pacotes.

## Como Começar

### 1. Modelo de Gestos
Para que a aplicação funcione, é necessário baixar o modelo `gesture_recognizer.task` do MediaPipe.

- **Link para download:** [gesture_recognizer.task](https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task)

Após o download, coloque o arquivo na pasta `models/` deste projeto. Os modelos `gesture_model.joblib` e `label_encoder.joblib` são gerados pela etapa anterior do projeto (mediapipe-gesture-recognition) e também devem estar nesta pasta, substitua-os caso deseje.

> [!NOTE]
> Para que a imagem do gesto seja exibida corretamente, o nome do arquivo da imagem em ``assets/img`` (sem a extensão) deve ser exatamente igual ao `label` do gesto correspondente.

### 2. Instalação
Navegue até a pasta do projeto e sincronize as dependências usando `uv`:
```bash
uv sync
```

### 3. Execução
Inicie o servidor da aplicação:
```bash
uv run app.py
```
Abra seu navegador e acesse `http://localhost:5001`.

## Estrutura do Projeto
```
gesture-recognition-app/
├── app.py                  # Ponto de entrada principal do FastHTML & handlers de WebSocket
├── core/
│   ├── processor.py        # Lógica de processamento de gestos & integração com MediaPipe
│   ├── models.py           # Carregamento de modelos de ML e classes de predição
│   └── utils.py            # Utilitários de codificação/decodificação de imagem
├── models/                 # Modelos de ML. Contém os .joblib (rastreados) e o .task (não rastreado).
├── assets/
│   ├── script.js           # Lógica do frontend para WebSocket & Webcam
│   ├── style.css           # Estilos da UI e animações
│   └── images/             # Imagens de gestos
├── pyproject.toml          # Dependências e metadados do projeto
├── requirements.txt        # Dependências (pip)
└── README.md               
```