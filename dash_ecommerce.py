import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

#DEFINE VARIAVEIS
df = pd.read_csv('/Users/carolinecarvalho/Documents/EBAC/analista_de_dados/modulo 22/visualizacao_dados/ecommerce_estatistica.csv')

df_corr=df[['Qtd_Vendidos_Cod', 'Nota', 'N_Avaliações_MinMax', 'Desconto', 'Preço', 'Marca_Freq', 'Material_Freq']].corr()

lista_temporada = df['Temporada'].unique()
options = [{'label': temporada, 'value': temporada} for temporada in lista_temporada]


#FUNCOES - CRIAR GRAFICOS
def grafico_histograma():
    fig1 = px.histogram(df, x="Nota", nbins=10, title="Distribuição de Notas",color_discrete_sequence=['#FF6F61'])
    fig1.update_layout(
        title='Distribuicao de Notas',
        xaxis_title='Nota',
        yaxis_title='Frequencia',
        plot_bgcolor='#FDF6F0',  
        paper_bgcolor='#EBE9E6'
    )
    return fig1


def grafico_dispersao():
    fig2 = px.scatter(df, x = 'Preço', y = 'N_Avaliações', color='Nota', color_continuous_scale='Viridis', hover_data=['Nota', 'Preço', 'N_Avaliações'])
    fig2.update_layout(
        title = 'Relacao entre Preco e Numero de Avaliacoes',
        xaxis_title = 'Preco',
        yaxis_title = 'Numero de Avaliacoes',
        plot_bgcolor='#FDF6F0',  
        paper_bgcolor='#EBE9E6'
    )
    return fig2


def grafico_mapacalor(df_corr):
    fig3 = px.imshow(df_corr, text_auto = '.2f', aspect = 'auto', color_continuous_scale='Viridis')
    fig3.update_layout(
        title = 'Mapa de Calor - Relacao entre as Variaveis',
        plot_bgcolor='#FDF6F0',  
        paper_bgcolor='#EBE9E6'
    )
    return fig3


def grafico_barra(selecao_temporada):
    filtro_df = df[df['Temporada'].isin(selecao_temporada)]
    fig4 = px.bar(filtro_df, x = 'Temporada', color_discrete_sequence=['#FF6F61'])
    fig4.update_layout(
        title = 'Quantidade de Produtos por Temporada',
        xaxis_title = 'Temporada',
        yaxis_title = 'Quantidade de Produtos',
        plot_bgcolor='#FDF6F0',
        paper_bgcolor='#EBE9E6'
    )
    return fig4


def grafico_pizza():
    contagem_genero = df['Gênero'].value_counts().reset_index()
    contagem_genero.columns = ['Gênero', 'Quantidade']
    fig5 = px.pie(contagem_genero, names = 'Gênero', values = 'Quantidade', color_discrete_sequence=['#16697A'], hover_data=['Quantidade'])
    fig5.update_layout(
        title = 'Distribuicao de Genero',
        legend_title='Gênero',
        plot_bgcolor='#FDF6F0',
        paper_bgcolor='#EBE9E6'
    )
    return fig5

def grafico_densidade():
    fig6 = px.histogram(df, x = 'Preço', histnorm='density')
    fig6.update_traces(
        marker_color="#FF6F61",
        opacity=0.7
    )
    fig6.update_layout(
        title="Densidade de Preços",
        xaxis_title="Preço",
        yaxis_title="Densidade",
        plot_bgcolor='#FDF6F0',
        paper_bgcolor='#EBE9E6'
    )
    return fig6

def grafico_regressao():
    fig7 = px.scatter(df, x='Qtd_Vendidos_Cod', y='Nota', color_discrete_sequence=['#16697A'])
    fig7.update_layout(
        title = 'Regressao Frequencia de Nota por Quantidade de Vendidos',
        xaxis_title = 'Quantidade de Vendidos',
        yaxis_title = 'Nota',
         plot_bgcolor='#FDF6F0',
        paper_bgcolor='#EBE9E6'
    )
    return fig7


#CRIAR APP
def cria_app():
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1('Dashboard interativo - Ecommerce'),
        html.Br(),
        html.H2('Graficos fixos'), 
        dcc.Graph(figure = grafico_histograma()),
        dcc.Graph(figure = grafico_dispersao()),
        dcc.Graph(figure = grafico_mapacalor(df_corr)),
        dcc.Graph(figure = grafico_pizza()),
        dcc.Graph(figure = grafico_densidade()),
        dcc.Graph(figure = grafico_regressao()),
        html.H2('Grafico de barras interativo'), 
        dcc.Checklist(
            id='id_selecao_temporada',
            options = options,
            value = lista_temporada[:7],
        ),
        dcc.Graph(id = 'id_grafico_barra')
    ])

    return app


if __name__ == '__main__':
    app = cria_app()

    @app.callback(
            Output('id_grafico_barra', 'figure'),
        Input('id_selecao_temporada', 'value')
    )
    def atualiza_grafico(id_selecao_temporada):
        fig4= grafico_barra(id_selecao_temporada)
        return fig4
    app.run(debug=True, port=8050)
