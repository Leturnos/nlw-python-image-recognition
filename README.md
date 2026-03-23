# 🚀 NLW Operator — Trilha Python: Visão Computacional

Bem-vindo ao repositório do projeto desenvolvido durante a **NLW (Next Level Week) Operator** da Rocketseat. Este workspace contém uma coleção de projetos e experimentos focados em Deep Learning, Reconhecimento de Gestos e técnicas avançadas de Visão Computacional.

## 🔗 Referências

- Rocketseat: https://rocketseat.com.br
- Repositório base do professor: https://github.com/rocketseat-education/nlw-operator-computer-vision

## 📂 Estrutura do Projeto

Este monorepo está organizado em três módulos principais, cada um correspondendo a uma etapa do aprendizado e desenvolvimento.

### 1. 🧠 `lenet-5-mnist`
Uma implementação da clássica arquitetura LeNet-5 utilizando PyTorch para classificação de dígitos manuscritos do dataset MNIST. Utilizado para entender os fundamentos de Redes Neurais Convolucionais (CNNs).

- **Tecnologias:** PyTorch, Jupyter, Matplotlib.
- **Destaques:** Definição de uma arquitetura CNN, treinamento e avaliação de modelo, e análise de filtros e ativações.

### 2. 🔬 `mediapipe-gesture-recognition`
O "laboratório" do projeto. Aqui se encontram as ferramentas para criar um sistema de reconhecimento de gestos customizado que é utilizado pela etapa posterior, desde a coleta de dados até o treinamento do modelo. Além disso, contém notebooks para exploração de modelos SOTA (State-of-the-Art).

- **Tecnologias:** Scikit-Learn, MediaPipe, OpenCV.
- **Destaques:** Pipeline de coleta de dados de landmarks da mão, treinamento de um classificador de gestos (Random Forest) e notebooks exploratórios com YOLOS, CLIPSeg e Gemini Vision API.
- **⚠️ Requisito:** Necessário baixar modelos do MediaPipe. Consulte o `README.md` do módulo para mais detalhes.

### 3. 🖐️ `gesture-recognition-app`
Uma aplicação web que utiliza o modelo treinado no módulo anterior para reconhecer gestos em tempo real através da webcam.

- **Tecnologias:** FastHTML, OpenCV, MediaPipe, Scikit-Learn, WebSockets.
- **Destaques:** Processamento de vídeo de baixa latência, interface reativa que exibe o gesto reconhecido e monitoramento de FPS.
- **⚠️ Requisito:** Necessário baixar o modelo de reconhecimento de gestos do MediaPipe. Consulte o `README.md` do módulo para mais detalhes.

## 🛠️ Tecnologias (Global)

- **Linguagem:** Python
- **Gerenciador de Pacotes:** `uv`
- **Frameworks e Bibliotecas:** PyTorch, Scikit-Learn, OpenCV, MediaPipe
- **Web:** FastHTML, Uvicorn, WebSockets
- **IA/ML (Exploratório):** YOLOS, CLIPSeg, Google Gemini API

## 🚀 Como Começar

### Pré-requisitos
- Python 3.10+
- `uv` instalado globalmente (`pip install uv`).

### Instalação
1. **Clone o repositório**
```bash
git clone https://github.com/Leturnos/nlw-python-image-recognition.git
```

2. **Entre no diretório**
```bash
cd nlw-python-image-recognition
```

3. **Escolha um módulo**

   Cada subpasta (`lenet-5-mnist`, `mediapipe-gesture-recognition`, `gesture-recognition-app`) é um projeto independente.

Exemplo:
```bash
cd gesture-recognition-app
```

---

# 🔹 Opção 1 — Usando uv (recomendado)

Instale as dependências com:
```bash
uv sync
```

Depois siga as instruções do `README.md` do módulo.

---

# 🔹 Opção 2 — Usando pip + requirements.txt

Caso você prefira não usar `uv`, cada módulo possui um `requirements.txt`.

1. Crie um ambiente virtual:
```bash
python -m venv .venv
```

2. Ative o ambiente:

    **Linux / Mac**
    ```bash
    source .venv/bin/activate
    ```

    **Windows**
    ```bash
    .venv\Scripts\activate
    ```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## 📝 Licença
Este projeto está sob a licença MIT.

Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


