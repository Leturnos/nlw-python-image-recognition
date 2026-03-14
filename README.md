# NLW Python Image Recognition

Este repositório faz parte da NLW (Next Level Week) da Rocketseat e contém um projeto em Python voltado para reconhecimento de padrões em imagens usando redes neurais.

## Aula 1 – LeNet5
Na primeira aula, trabalhamos com o notebook **`lenet5.ipynb`**, que implementa a arquitetura LeNet-5 em PyTorch.

### O que está incluso
- Implementação da arquitetura **LeNet-5** em PyTorch
- Visualização dos filtros iniciais da rede
- Carregamento do dataset **MNIST** (imagens de dígitos manuscritos)
- Treinamento e avaliação da rede no conjunto de teste
- Visualização de exemplos mal classificados
- Salvamento e recarregamento do modelo treinado
- Visualização das ativações da primeira camada convolucional

## Como executar
1. Crie um ambiente virtual (recomendado)
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
   ou usando o gerenciador `uv`:
   ```bash
   uv add torch torchvision matplotlib ipykernel
   ```
3. Abra o notebook:
   ```bash
   jupyter notebook lenet5.ipynb
   ```

## Observações
- A estrutura do projeto está pensada para ser incrementada nas próximas aulas, adicionando mais notebooks e implementações.
- O dataset MNIST será baixado automaticamente ao executar o notebook.
