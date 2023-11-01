#Bibliotecas necessárias

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import inflection

#Import dataset
df=pd.read_csv( "zomato.csv" )

df1=df.copy()

#Modelo exibição da página.
st.set_page_config(page_title="Cuisines", page_icon="🍽️", layout="wide")

# ============================================================================
#Alterações no dataframe (pedidos no exercício)
# ============================================================================

#Aqui vamos renomear os nomes das colunas, deixando tudo maíusculo e onde tem espaço substituir por _
#Função
def rename_columns(df1):
    title = lambda x: inflection.titleize(x)
    
    snakecase = lambda x: inflection.underscore(x)
    
    spaces = lambda x: x.replace(" ", "")
    
    cols_old = list(df1.columns)
    
    cols_old = list(map(title, cols_old))
    
    cols_old = list(map(spaces, cols_old))
    
    cols_new = list(map(snakecase, cols_old))
    
    df1.columns = cols_new
    
    return df1

#Aqui temos que chamar a função, assim acontece a substituição dos nomes
rename_columns(df1)


#Aqui vamos alterar o nome dos Países para o código deles.
#Função
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}
def country_name(country_id):
    return COUNTRIES[country_id]


#Criação do Tipo de Categoria de Comida
#Função
def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"
    
    
    
#Criação do tipo das cores, nada mais do que substituir os códigos pelos nomes das cores.
COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}
def color_name(rating_color):
    return COLORS[rating_color]


#Devemos aplicar o .apply(country_name) para finalizar a função que criamos anteriormente.
df1["country_code"] = df1["country_code"].apply(country_name)
#Devemos aplicar o .apply(create_price_tye) para finalizar a função que criamos anteriormente.
df1["price_range"] = df1["price_range"].apply(create_price_tye)
#Devemos aplicar o .apply(color_name) para finalizar a função que criamos anteriormente.
df1["rating_color"] = df1["rating_color"].apply(color_name)


# ============================================================================
#Funções
# ============================================================================

def top_cuisines():
    """ Esta função tem a responsabilidade de mostrar informações.
        
        Tipo de informação: Melhores Restaurantes dos Principais tipos Culinários.
        
        Input: Dataframe
        Output: Informações sobre os melhores restaurantes e suas notas.
    """
    
    cuisines = {
        "Italian": "",
        "American": "",
        "Arabian": "",
        "Japanese": "",
        "Brazilian": "",
    }

    cols = [
        "restaurant_id",
        "restaurant_name",
        "country_code",
        "city",
        "cuisines",
        "average_cost_for_two",
        "currency",
        "aggregate_rating",
        "votes",
    ]

    for key in cuisines.keys():

        lines = df1["cuisines"] == key

        cuisines[key] = (
            df1.loc[lines, cols]
            .sort_values(["aggregate_rating", "restaurant_id"], ascending=[False, True])
            .iloc[0, :]
            .to_dict()
        )

    return cuisines

def write_metrics():

    cuisines = top_cuisines()

    italian, american, arabian, japonese, brazilian = st.columns(len(cuisines))

    with italian:
        st.metric(
            label=f'Italiana: {cuisines["Italian"]["restaurant_name"]}',
            value=f'{cuisines["Italian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Italian"]['country_code']}\n
            Cidade: {cuisines["Italian"]['city']}\n
            Média Prato para dois: {cuisines["Italian"]['average_cost_for_two']} ({cuisines["Italian"]['currency']})
            """,
        )

    with american:
        st.metric(
            label=f'Americana: {cuisines["American"]["restaurant_name"]}',
            value=f'{cuisines["American"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["American"]['country_code']}\n
            Cidade: {cuisines["American"]['city']}\n
            Média Prato para dois: {cuisines["American"]['average_cost_for_two']} ({cuisines["American"]['currency']})
            """,
        )

    with arabian:
        st.metric(
            label=f'Árabe: {cuisines["Arabian"]["restaurant_name"]}',
            value=f'{cuisines["Arabian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Arabian"]['country_code']}\n
            Cidade: {cuisines["Arabian"]['city']}\n
            Média Prato para dois: {cuisines["Arabian"]['average_cost_for_two']} ({cuisines["Arabian"]['currency']})
            """,
        )

    with japonese:
        st.metric(
            label=f'Japonesa: {cuisines["Japanese"]["restaurant_name"]}',
            value=f'{cuisines["Japanese"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Japanese"]['country_code']}\n
            Cidade: {cuisines["Japanese"]['city']}\n
            Média Prato para dois: {cuisines["Japanese"]['average_cost_for_two']} ({cuisines["Japanese"]['currency']})
            """,
        )

    with brazilian:
        st.metric(
            label=f'Brasileira: {cuisines["Brazilian"]["restaurant_name"]}',
            value=f'{cuisines["Brazilian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Brazilian"]['country_code']}\n
            Cidade: {cuisines["Brazilian"]['city']}\n
            Média Prato para dois: {cuisines["Brazilian"]['average_cost_for_two']} ({cuisines["Brazilian"]['currency']})
            """,
        )

    return None

def top10_restaurants (df1):
    """ Esta função tem a responsabilidade de mostrar um dataframe.
        
        Tipo de informação: Top 10 restaurantes.
        
        Input: Dataframe
        Output: Informações sobre os melhores restaurantes perante a média de suas avaliações.
    """
    
    cols = [
            "restaurant_id",
            "restaurant_name",
            "country_code",
            "city",
            "cuisines",
            "average_cost_for_two",
            "aggregate_rating",
            "votes",
    ]

    lines = (df1["cuisines"].isin(cuisines)) & (df1["country_code"].isin(countries))

    top10 = df1.loc[lines, cols].sort_values(
        ["aggregate_rating", "restaurant_id"], ascending=[False, True]
    )


    top10 = top10.head(qnt_restaurantes).reset_index(drop=True)
    top10
        
def top10_best_cuisines (df1):
    """ Esta função tem a responsabilidade de plotar um gráfico
        
        Tipo de gráfico: De barras
        Informação do gráfico: Top 10 melhores tipos de culinária.
        
        Input: Dataframe
        Output: Gráfico
    """
    
    df_aux = ( 
            df1.loc[df1['country_code'].isin(countries), ['cuisines', 'restaurant_id', 'aggregate_rating']]
               .groupby(['cuisines'])
               .mean()
               .sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True])
               .reset_index()
               .head(qnt_restaurantes)
            )
        
    fig = px.bar(
        df_aux.head(qnt_restaurantes),
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        title=f"Top {qnt_restaurantes} Melhores Tipos de Culinárias",
        labels={
            "cuisines": "Tipo de Culinária",
            "aggregate_rating": "Média da Avaliação Média",
        },
    )
    
    return fig

def top10_worst_cuisines (df1):
    """ Esta função tem a responsabilidade de plotar um gráfico
        
        Tipo de gráfico: De barras
        Informação do gráfico: Top 10 piores tipos de culinária.
        
        Input: Dataframe
        Output: Gráfico
    """
    
    df_aux = (
            df1.loc[df1['country_code'].isin(countries), ['cuisines', 'aggregate_rating']]
               .groupby(['cuisines'])
               .mean()
               .sort_values('aggregate_rating')
               .reset_index()
               .head(qnt_restaurantes)
            )

    fig = px.bar(
        df_aux.head(qnt_restaurantes),
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        title=f"Top {qnt_restaurantes} Piores Tipos de Culinárias",
        labels={
            "cuisines": "Tipo de Culinária",
            "aggregate_rating": "Média da Avaliação Média",
        },
    )
    
    return fig

# ============================================================================
#Limpeza DataFrame
# ============================================================================

#Aqui categorizamos os restaurantes por só UM tipo de comida, o exercício pede assim
df1["cuisines"] = df1.loc[:, "cuisines"].astype(str).apply(lambda x: x.split(",")[0])

#Aqui vamos fazer a exclusão de uma coluna com valores únicos
df1 = df1.drop("switch_to_order_menu", axis=1)

#Excluíndo valores duplicados
df1 = df1.drop_duplicates().reset_index()
del df1["index"]


# ============================================================================
# Barra Lateral no StreamLit
# ============================================================================

st.sidebar.markdown( "## Filtros" )

countries = st.sidebar.multiselect(
    "Quais países você deseja visualizar informações?",
    df1.loc[:, "country_code"].unique().tolist(),
    default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"])


st.sidebar.markdown ("""---""")


qnt_restaurantes = st.sidebar.slider ( 
    "Selecione a quantidade de Restaurantes que deseja visualizar", 1, 20, 10
)


st.sidebar.markdown ("""---""")


cuisines = st.sidebar.multiselect(
    "Escolha quais os tipos de culinária",
    df1.loc[:, "cuisines"].unique().tolist(),
    default=["Home-made",
            "BBQ",
            "Japanese",
            "Brazilian",
            "Arabian",
            "American",
            "Italian",
            ],
)


st.sidebar.markdown ( """---""" )
st.sidebar.markdown ( "### Powered by Webert Bortolotti" )

# ============================================================================
# Layout no StreamLit
# ============================================================================

st.markdown("# Cuisines 🍽️")


with st.container():
    st.markdown("### Melhores Restaurantes dos Principais tipos Culinários")
    write_metrics()    
            
    
with st.container():
    st.markdown("### Top 10 Restaurantes")
    top10_restaurants(df1)
    

with st.container():
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = top10_best_cuisines (df1)
        st.plotly_chart( fig, use_container_width=True )
        
    with col2:
        fig = top10_worst_cuisines (df1)
        st.plotly_chart( fig, use_container_width=True )