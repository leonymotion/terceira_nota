from plotnine import ggplot, aes, geom_point, labs, theme_bw, theme, geom_boxplot
import seaborn as sns

# Carregar o dataset iris usando seaborn
iris = sns.load_dataset('iris')

# Gráfico 1: Dispersão com Plotnine
grafico1 = (
    ggplot(iris) 
    + aes(x='sepal_length', y='sepal_width', color='species')
    + geom_point(alpha=0.7)
    + labs(x='Comprimento da Sépala (cm)', 
           y='Largura da Sépala (cm)',
           title='Relação entre Comprimento e Largura da Sépala por Espécie')
    + theme_bw()
    + theme(figure_size=(10, 6))
)

# Gráfico 2: Boxplot com Plotnine
grafico2 = (
    ggplot(iris) 
    + aes(x='species', y='petal_length', fill='species')
    + geom_boxplot()
    + labs(x='Espécie', 
           y='Comprimento da Pétala (cm)',
           title='Distribuição do Comprimento da Pétala por Espécie')
    + theme_bw()
    + theme(figure_size=(12, 6))
)

grafico1.save("grafico1.png")
grafico2.save("grafico2.png")