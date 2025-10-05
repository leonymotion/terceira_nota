# Visualização e Aceleração Computacional em Python

Para vizualização do conteudo, você pode acessar o site: https://leonymotion.github.io/terceira_nota

Este projeto demonstra o uso de ferramentas do ecossistema Python para ciência de dados, incluindo visualização de dados com Matplotlib e Plotnine, e aceleração computacional com Numba.

## Estrutura

- `index.qmd`: Documento principal do projeto em Quarto.
- `index.html`: Versão renderizada do documento.
- `imagens/`: Pasta com gráficos gerados (`grafico1.png`, `grafico2.png`, `matplot_dispersao.png`, `matplot_boxplot.png`).
- `codigos/`: Scripts Python para geração dos gráficos e testes de desempenho.

## Ferramentas Utilizadas

- **Matplotlib**: Visualização tradicional de dados.
- **Plotnine**: Visualização baseada na gramática de gráficos.
- **Numba**: Aceleração de código Python com compilação JIT.

## Como usar

1. Instale as dependências:
   ```
   pip install matplotlib seaborn plotnine numba quarto
   ```
2. Gere os gráficos executando os scripts Python.
3. Renderize o documento com Quarto:
   ```
   quarto render index.qmd
   ```
4. Veja os resultados em `index.html`.
