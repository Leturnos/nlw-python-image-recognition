# LeNet-5 — Classificação de Dígitos MNIST

Este projeto implementa a arquitetura LeNet-5 em PyTorch para classificar dígitos manuscritos do dataset MNIST. Faz parte da Aula 1 da NLW (Next Level Week) Operator da Rocketseat.

## Sobre o Projeto
O notebook `lenet5.ipynb` cobre:
- Definição da arquitetura LeNet-5 (com ReLU e Max Pooling).
- Visualização de filtros e ativações.
- Treinamento e avaliação no MNIST.
- Análise de erros.

## Estrutura do Projeto
```
lenet-5-mnist/
├── lenet5.ipynb        # Notebook principal
├── lenet5_mnist.pth    # Pesos treinados (gerado)
├── pyproject.toml      # Dependências
├── requirements.txt    # Dependências (pip)
└── README.md
```

## Como Executar
1. Instale as dependências:
   ```bash
   uv sync
   ```
2. Abra o notebook:
   ```bash
   jupyter notebook lenet5.ipynb
   ```
3. Execute as células sequencialmente.

## Resultados Esperados
Acurácia > 98% no teste após treinamento.
