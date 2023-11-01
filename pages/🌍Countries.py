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
st.set_page_config(page_title="Countries", page_icon="🌍", layout="wide")

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

def restaurant_countries (df1):
    """ Esta função tem a responsabilidade de plotar um gráfico
        
        Tipo de gráfico: De barras
        Informação do gráfico: Quantidade de Restaurantes Registrados por País.
        
        Input: Dataframe
        Output: Gráfico
    """
    
    df_aux = (
            df1.loc[df1["country_code"].isin(countries), ["restaurant_id", "country_code"]]
               .groupby("country_code")
               .nunique()
               .sort_values("restaurant_id", ascending=False)
               .reset_index()
            )
        
    fig = px.bar(
        df_aux,
        x="country_code",
        y="restaurant_id",
        text="restaurant_id",
        title="Quantidade de Restaurantes Registrados por País",
        labels={
            "country_code": "Paises",
            "restaurant_id": "Quantidade de Restaurantes",
        },
    )
    
    return fig


def cities_countries (df1):
    """ Esta função tem a responsabilidade de plotar um gráfico
        
        Tipo de gráfico: De barras
        Informação do gráfico: Quantidade de Cidades Registradas por País.
        
        Input: Dataframe
        Output: Gráfico
    """
    
    df_aux = (
            df1.loc[df1["country_code"].isin(countries), ["country_code", "city"]]
               .groupby(["country_code"])
               .nunique()
               .sort_values("city", ascending=False)
               .reset_index()
            )
        
    fig = px.bar(
        df_aux,
        x="country_code",
        y="city",
        text="city",
        title="Quantidade de Cidades Registradas por País",
        labels={
            "country_code": "Paises",
            "city": "Quantidade de Cidades",
        }
    )

    return fig

def votes_countries (df1):
    """ Esta função tem a responsabilidade de plotar um gráfico
        
        Tipo de gráfico: De barras
        Informação do gráfico: Média de Avaliação feitas por País.
        
        Input: Dataframe
        Output: Gráfico
    """
    
    df_aux = round (
             df1.loc[df1["country_code"].isin(countries), ["country_code", "votes"]]
                .groupby(["country_code"])
                .mean()
                .sort_values("votes", ascending=False)
                .reset_index(),2
            )
        
    fig = px.bar(
        df_aux,
        x="country_code",
        y="votes",
        text="votes",
        title="Média de Avaliação feitas por País",
        labels={
            "country_code": "País",
            "votes": "Quantidade de Votos",
        }
    )
    
    return fig 


def avg_two_peoples_countries (df1):
    """ Esta função tem a responsabilidade de plotar um gráfico
        
        Tipo de gráfico: De barras
        Informação do gráfico: Média de Preço de um prato para duas pessoas por País.
        
        Input: Dataframe
        Output: Gráfico
    """
    
    df_aux = round ( 
             df1.loc[df1["country_code"].isin(countries), ["country_code", "average_cost_for_two"]]
                .groupby(["country_code"])
                .mean()
                .sort_values("average_cost_for_two", ascending=False)
                .reset_index(),2
            )
        
    fig = px.bar(
        df_aux,
        x="country_code",
        y="average_cost_for_two",
        text="average_cost_for_two",
        title="Média de Preço de um prato para duas pessoas por País",
        labels={
            "country_code": "País",
                "average_cost_for_two": "Preço Médio do Prato para 2 Pessoas",
        }
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

st.markdown( "# 🌍 Visão Países" )

with st.container ():
        fig = restaurant_countries (df1)
        st.plotly_chart( fig )
        
        
with st.container ():
        fig = cities_countries (df1)
        st.plotly_chart(fig)
        
        
with st.container ():
    col1, col2 = st.columns(2)
    with col1:
        fig = votes_countries (df1)
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        fig = avg_two_peoples_countries (df1)
        st.plotly_chart(fig, use_container_width=True)