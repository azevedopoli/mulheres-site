import streamlit as st
from PIL import Image

# Definindo o CSS para remover funções de adm e customização da interface do site
customizando_site = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background: radial-gradient(circle, violet, pink); /* Gradiente rosa-roxo */
        font-family: 'Roboto', sans-serif; /* Aplicando a fonte Roboto */
    }
    .nome {
        text-align: center; /* Centraliza o texto */
        font-size: 24px; /* Tamanho do texto dos nomes */
        color: #C71585; /* Cor do texto em rosa escuro */
        background-color: rgba(255, 255, 255, 0.5); /* Cor de fundo branca com 50% de transparência */
        padding: 3px; /* Espaçamento interno da caixa reduzido */
        border-radius: 5px; /* Bordas arredondadas */
        margin: 3px; /* Margem reduzida */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Sombra para destacar */
    }
    .imagem-container {
        display: flex;
        flex-direction: column;
        align-items: center; /* Centraliza horizontalmente */
        justify-content: center; /* Centraliza verticalmente */
        margin: 20px 0; /* Espaçamento entre cada contêiner */
    }
    .titulo {
        color: white; /* Cor do texto do título */
        font-size: 4vw; /* Tamanho responsivo do texto do título */
        text-align: center; /* Centraliza o texto */
        text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.6); /* Sombra para o título */
        border-bottom: 4px solid #C71585; /* Linha embaixo do título */
        padding-bottom: 5px; /* Espaçamento abaixo do título */
        width: 100%; /* Largura total */
        margin: -20px 0 0 0; /* Margens */
    }
    </style>
    """

# Aplicando o CSS
st.markdown(customizando_site, unsafe_allow_html=True)

# Definição do título centralizado
st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; width: 100%;">
        <h1 class='titulo'>
            A Influência das Mulheres Gonçalenses na Construção Identitária da Sociedade
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)


# Função para exibir a legenda com estilo
def styled_caption(text):
    # Separar a legenda em duas partes: antes e depois do "-"
    parts = text.split(" - ")
    if len(parts) == 2:
        first_part = parts[0]
        second_part = parts[1]
        # Parte após o "-"
        return f"<span style='color: white; font-size: 23px;'>{first_part}<br><span style='color: black; font-size: 18px;'>{second_part}</span></span>"
    return f"<span style='color: white; font-size: 23px;'>{text}</span>"

# Nomes e imagens
images = {
    "Aline": "IMAGES.SITE/Aline.jpg",
    "Elaine": "IMAGES.SITE/Elaine.jpg",
    "Maria José": "IMAGES.SITE/Maria José.jpg",
    "Maria Albêrtina": "IMAGES.SITE/Maria Albêrtina.jpg",
    "Cynthia da Silva": "IMAGES.SITE/Cynthia.jpg",
    "Daniele da Silva": "IMAGES.SITE/Daniele.jpg",
    "Kelly Francisco": "IMAGES.SITE/Kelly.jpg",
    "Rosa Mendonça": "IMAGES.SITE/Rosa.jpg",
    "Shirley": "IMAGES.SITE/Shirley.jpg",
    "Poliana Melo": "IMAGES.SITE/Poliana.jpg",
    "Ana Paula": "IMAGES.SITE/Ana Paula.jpg",
    "Elizangela": "IMAGES.SITE/Elizangela.jpg",
    "Sheila Mota": "IMAGES.SITE/Sheila.jpg",
    "Rana Victória": "IMAGES.SITE/Rana.jpg",
    "Ana Suelen": "IMAGES.SITE/Ana Suelen.jpg",
    "Adriana": "IMAGES.SITE/Adriana.jpg",
    "Roberta": "IMAGES.SITE/Roberta.jpg",
    "Dona Beta": "IMAGES.SITE/Beta.jpg",
    "Leandra": "IMAGES.SITE/Leandra.jpg",
    "Stella": "IMAGES.SITE/Stella.jpg",
}

# Legendas correspondentes
captions = [
    "Minha professora que me ensinou que sempre devemos acreditar em nós mesmos, e também não desistir do que almejamos. - ~ Pedro Henrique (3004)",
    "Me formou como pessoa e me ensinou que amor não é só falando mas também pode ser demonstrado com ações. - ~ Pedro Henrique (3004)",
    "Me ensinou que podem tirar tudo da gente menos o conhecimento. - ~ Ana Clara Souza (2003)",
    "Me ensinou que saudade é o amor que permanece, mesmo quando a presença se transforma em lembrança. - ~ Luísa (2003)",
    "Me ensinou que vencer o câncer é acreditar na vida, mesmo quando o corpo fraqueja. - ~ Luísa (2003)",
    "Me ensinou que ser forte é abraçar a fragilidade, mas nunca deixar que ela defina quem somos. - ~ Luísa (2003)",
    "Ela sempre acreditou no meu potencial! - ~ Vinícius (2003)",
    "Me ensinou a enfrentar a vida de cabeça erguida, meu exemplo de força e coragem - ~ Lívia (1003)",
    "Essa mulher me ensinou a importância de estar com nossos exames sempre dia para vencer a luta contra o câncer de mama. - ~ Lívia (1003)",
    "Ela me criou com muito carinho - ~ Lívia (1003)",
    "Me ensinou que ser forte não é nunca cair, mas sempre se levantar e seguir em frente, mesmo quando tudo parece difícil. - ~ Ana Beatriz Xavier (2003)",
    "Me ensinou a ser amorosa! - ~ Khemeronn (1003)",
    "Me mostrou o que é amor e foi capaz de ir muito longe apenas por me amar. Nunca conheci alguém mais forte que ela, e com um nome tão lindo. - ~ Ana Clara Mota (2003)",
    "Por ter crescido comigo, me mostrou o quanto somos responsáveis pela identidade uma da outra. - ~ Ana Clara Mota (2003)",
    "A mulher que me inspira todos os dias com sua força e dedicação e que transforma desafios em lições de vida. - ~ Ester (3006)",
    "Tia e mãe incrível que entre todos os ensinamentos importantes, me ensinou a importância do amor. - ~ Samuel (2003)",
    "Me ensinou muito sobre persistência, pois mesmo lidando com diversos problemas de saúde nunca deixou de trabalhar para me dar uma boa qualidade de vida - ~ Fabiane (3006)",
    "Cuidou de mim nos momentos que eu mais precisei. - ~ Laís Rocha (2003)",
    "Me ensinou a ser a pessoa que eu sou hoje e cuidou de mim para que eu nunca passasse por maus momentos - ~ Laís Rocha (2003)",
    "Inspirou gerações de alunos com sua dedicação ao ensino e amor pela educação. - ~ Miguel Maia (2003)"
]

# Exibindo as imagens e legendas em uma única coluna
for i, (name, path) in enumerate(images.items()):
    # Criar um contêiner para centralizar o nome e a imagem
    st.markdown("<div class='imagem-container'>", unsafe_allow_html=True)
    st.markdown(f"<div class='nome'>{name}</div>", unsafe_allow_html=True)  # Exibindo o nome com estilo
    try:
        image = Image.open(path)
        st.image(image, caption="", width=150, use_column_width=True)
    except Exception as e:
        st.error(f"Erro ao carregar a imagem: {e}")

    st.markdown(styled_caption(captions[i]), unsafe_allow_html=True)  # Legenda na mesma coluna
    st.markdown("</div>", unsafe_allow_html=True)  # Fechar o contêiner

# Adiciona um espaço entre as linhas
st.markdown("<br>", unsafe_allow_html=True)
