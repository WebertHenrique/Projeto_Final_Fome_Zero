#Bibliotecas necessárias
from folium.plugins import HeatMap, MarkerCluster
from PIL import Image
from streamlit_folium import folium_static
import folium
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import inflection



#Import dataset
df=pd.read_csv( "zomato.csv" )

df1=df.copy()

#Modelo exibição da página.
st.set_page_config(page_title="Home", page_icon="📊", layout="wide")

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

def create_map(dataframe):
    """ Esta função tem a responsabilidade de plotar um mapa.
        
        Tipo de informação: No mapa você encontrará os dados referentes aos Países,
        Cidades e Restaurantes.
        
        Input: Dataframe
        Output: Mapa.
    """
    f = folium.Figure(width=1920, height=1080)

    m = folium.Map(max_bounds=True).add_to(f)

    marker_cluster = MarkerCluster().add_to(m)

    for _, line in dataframe.iterrows():

        name = line["restaurant_name"]
        price_for_two = line["average_cost_for_two"]
        cuisine = line["cuisines"]
        currency = line["currency"]
        rating = line["aggregate_rating"]
        color = f'{line["rating_color"]}'

        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: {},00 ({}) para dois"
        html += "<br />Type: {}"
        html += "<br />Aggragate Rating: {}/5.0"
        html = html.format(name, price_for_two, currency, cuisine, rating)

        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )

        folium.Marker(
            [line["latitude"], line["longitude"]],
            popup=popup,
            icon=folium.Icon(color=color, icon="home", prefix="fa"),
        ).add_to(marker_cluster)

    folium_static(m , width=800, height=600 )


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

st.sidebar.markdown("# Fome Zero")

#image_path = "LogoFlecha.jpg"
image = Image.open( "LogoFlecha.jpg" )
st.sidebar.image( image, width=110 )


st.sidebar.markdown ("""---""")

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

st.markdown ("# Fome Zero! ")

st.markdown ("### O melhor lugar para encontrar o seu mais novo restaurante favorito! ")

st.markdown ("##### Dentro da nossa plataforma você vai encontrar: ")


with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        rest_cadastrados = df1["restaurant_id"].nunique()
        col1.metric("Restaurantes Cadastrados", rest_cadastrados)
        
    with col2:
        paises_unicos = df1["country_code"].nunique()
        col2.metric("Países Cadastrados", paises_unicos)
        
    with col3:
        cidades_unicas = df1["city"].nunique()
        col3.metric("Cidades Cadastradas", cidades_unicas)
    
    with col4:
        av_feitas = df1["votes"].sum()
        col4.metric("Avaliações na Plataforma", f"{av_feitas:,}".replace(",", "."))
        
    with col5:
        tipos_culinarias = df1["cuisines"].nunique()
        col5.metric("Diferentes Culinárias", tipos_culinarias)
        

with st.container():
    map_df = df1.loc[df1["country_code"].isin(countries), :]
    create_map(map_df)
    