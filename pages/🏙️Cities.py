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
st.set_page_config(page_title="Cities", page_icon="🏙️", layout="wide")

#----------------------------
#Alterações no dataframe (pedidos no exercício)
#----------------------------

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


#----------------------------
#Funções
#----------------------------


def top_cities_restaurants (df1):
    """ Esta função tem a responsabilidade de plotar um gráfico
        
        Tipo de gráfico: De barras
        Informação do gráfico: Top 10 cidades com mais restaurantes na base de dados.
        
        Input: Dataframe
        Output: Gráfico
    """
    
    df_aux = (
            df1.loc[df1["country_code"].isin(countries), ['restaurant_id', 'country_code', 'city']]
               .groupby(['city', 'country_code'])
               .count()
               .sort_values(['restaurant_id', 'city'] , ascending=[False,True])
               .reset_index()
            )
        
    fig = px.bar(
        df_aux.head(10),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=".2f",
        color="country_code",
        title="Top 10 cidades com mais restaurantes na base de dados",
        labels={
        "city": "Cidade",
        "restaurant_id": "Quantidade de Restaurantes",
        "country_code": "País",
        },
    )
    return fig

def top7_best_restaurants (df1):
    """ Esta função tem a responsabilidade de plotar um gráfico
        
        Tipo de gráfico: De barras
        Informação do gráfico: Top 7 Cidades com Restaurantes com média de avaliação acima de 4.
        
        Input: Dataframe
        Output: Gráfico
    """
    
    df_aux = (
            df1.loc[
                 (df1["aggregate_rating"] >= 4) & (df1["country_code"].isin(countries)),
                 ["city", "country_code", "restaurant_id"],
            ]
               .groupby(["country_code", "city"])
               .count()
               .sort_values(["restaurant_id", "city"], ascending=[False, True])
              .reset_index()
            )
        
    fig = px.bar(
        df_aux.head(7),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=".2f",
        color="country_code",
        title="Top 7 Cidades com Restaurantes com média de avaliação acima de 4",
        labels={
        "city": "Cidade",
        "restaurant_id": "Quantidade de Restaurantes",
        "country_code": "País",
        },
    )
    
    return fig

def top7_worst_restaurants (df1):
    """ Esta função tem a responsabilidade de plotar um gráfico
        
        Tipo de gráfico: De barras
        Informação do gráfico: Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5.
        
        Input: Dataframe
        Output: Gráfico
    """
    
    df_aux = (
            df1.loc[
                 (df1["aggregate_rating"] <= 2.5) & (df1["country_code"].isin(countries)), 
                 ["city", "country_code", "restaurant_id"],
            ]
               .groupby(["city", "country_code"])
               .count()
               .sort_values(["restaurant_id", "city"], ascending=[False,True])
               .reset_index()
            )
        
    fig = px.bar(
        df_aux.head(7),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=".2f",
        color="country_code",
        title="Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5",
        labels={
        "city": "Cidade",
        "restaurant_id": "Quantidade de Restaurantes",
        "country_code": "País",
        },
    )
    
    return fig

def cities_different_cuisines (df1):
    """ Esta função tem a responsabilidade de plotar um gráfico
        
        Tipo de gráfico: De barras
        Informação do gráfico: Top 10 Cidades mais restaurantes com tipos culinários distintos.
        
        Input: Dataframe
        Output: Gráfico
    """
    
    df_aux = (
            df1.loc[df1["country_code"].isin(countries), ["city", "country_code", "cuisines"]]
               .groupby(["city", "country_code"])
               .nunique()
               .sort_values(["cuisines", "city"], ascending=[False, True])
               .reset_index()
        )
        
    fig = px.bar(
        df_aux.head(10),
        x="city",
        y="cuisines",
        text="cuisines",
        text_auto=".2f",
        color="country_code",
        title="Top 10 Cidades mais restaurantes com tipos culinários distintos",
        labels={
        "city": "Cidade",
        "cuisines": "Quantidade de Tipos Culinários Únicos",
        "country_code": "País",
        },
    )
    
    return fig

#----------------------------
#Limpeza DataFrame
#----------------------------

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

st.sidebar.markdown ( """---""" )
st.sidebar.markdown ( "### Powered by Webert Bortolotti" )


# ============================================================================
# Layout no StreamLit
# ============================================================================

st.markdown('# Cities 🏙️')

with st.container():
        fig = top_cities_restaurants (df1)
        st.plotly_chart( fig, use_container_width=True )
        
        
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        fig = top7_best_restaurants (df1)
        st.plotly_chart( fig, use_container_width=True )
    
    
    with col2:
        fig = top7_worst_restaurants (df1)
        st.plotly_chart( fig, use_container_width=True )
        
        
with st.container():
        fig = cities_different_cuisines (df1)
        st.plotly_chart( fig, use_container_width=True )