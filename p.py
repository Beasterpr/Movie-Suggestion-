import streamlit as st
import pandas as pd
import pickle
import base64

st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎥",
    layout="wide",
)


def get_base64_of_bin_file(bin_file_path):
    with open(bin_file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to add background
def add_background():
    # Path to your image in the static folder
    image_path = "static/image.png"
    base64_image = get_base64_of_bin_file(image_path)
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add the background
add_background()


# Load similarity matrix and movies list
similarity = pickle.load(open("similarity.pkl", "rb"))
movies_list = pickle.load(open("movies.pkl", "rb"))
movies = pd.DataFrame(movies_list)

# Function to get poster URL for a movie
def poster(title):
    return movies[movies["title"] == title]["Poster_Url"].values[0]

# Function to get movie details
def info(title):
    movie_row = movies[movies["title"] == title]
    return [
        movie_row["title"].values[0],
        movie_row["release_date"].values[0],
        movie_row["tagline"].values[0],
        movie_row["overview"].values[0],
        movie_row["vote_average"].values[0],
        movie_row["ge"].values[0]
    ]

# Recommendation function
def recommend(movie):
    movie_index = int(movies[movies["title"] == movie].index[0])
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:7]
    
    recommended = []
    posters = []
    for i in movie_list:
        recommended_title = movies.iloc[i[0]].title
        recommended.append(recommended_title)
        posters.append(poster(recommended_title))
    
    return recommended, posters

# Streamlit app interface
st.title("Movie Recommender System")

# Dropdown for movie selection
selectboxs = st.selectbox(
    'Select a Movie:',
    movies["title"].values
)

# Recommend button and display recommendations
if st.button("Recommend"):
    recommended, posters = recommend(selectboxs)

    # Display selected movie details
    col1, col2 = st.columns(2)
    with col1:
        st.image(poster(selectboxs))  # Use the movie title to get the poster
    with col2:
        movie_info = info(selectboxs)
        st.title(movie_info[0])
        st.markdown(f"**Overview:** {movie_info[3]}")
        col3 ,col4 = st.columns([1,8])
        with col3:
            st.markdown("**Release Date:**")
        with col4:
            st.markdown(f"<h6 style='color:green;'>{movie_info[1]}</h6>",unsafe_allow_html=True)
        st.markdown(f"**Tagline:** {movie_info[2]}")
        col5, col6 = st.columns([1, 15])   
        with col5:
            st.markdown("**Rating:**")
        with col6:
            st.markdown(f"<h6 style='color:green;'>{movie_info[4]:.2f}</h6>", unsafe_allow_html=True)
        st.markdown(f"**Genre:** {', '.join(map(str, movie_info[5]))}")

    # Display recommendations in columns
    col7, col8 , col9 = st.columns(3)
    with col7:
        st.header(recommended[0])
        st.image(posters[0])
        with st.expander("Movie Info"):
            movie_info = info(recommended[0])  # Call info() once and store the result
            st.markdown(f"**Overview:** {movie_info[3]}")
            col10,col11 = st.columns([1,2])
            with col10:
                st.markdown(f"**Release Date:**")
            with col11:
                st.markdown(f"<h6 style='color:green;'>{movie_info[1]}</h6>",unsafe_allow_html=True)
            st.markdown(f"**Tagline:** {movie_info[2]}")
            col12,col13 = st.columns([1,5])
            with col12:
                st.markdown(f"**Rating:**")
            with col13:
                st.markdown(f"<h6 style='color:green;'>{movie_info[4]}</h6>",unsafe_allow_html=True)
            st.markdown(f"**Genre:** {', '.join(map(str, movie_info[5]))}")
    
    with col8:
        st.header(recommended[1])
        st.image(posters[1])
        with st.expander("Movie Info"):
            movie_info = info(recommended[1])
            st.markdown(f"**Overview:** {movie_info[3]}")
            col14,col15 = st.columns([1,2])
            with col14:
                st.markdown(f"**Release Date:**")
            with col15:
                st.markdown(f"<h6 style='color:green;'>{movie_info[1]}</h6>",unsafe_allow_html=True)
            st.markdown(f"**Tagline:** {movie_info[2]}")
            col16,col17 = st.columns([1,5])
            with col16:
                st.markdown(f"**Rating:**")
            with col17:
                st.markdown(f"<h6 style='color:green;'>{movie_info[4]}</h6>",unsafe_allow_html=True)
            st.markdown(f"**Genre:** {', '.join(map(str, movie_info[5]))}")
    

    with col9:
        st.header(recommended[2])
        st.image(posters[2])
        with st.expander("Movie Info"):
            movie_info = info(recommended[2]) 
            st.markdown(f"**Overview:** {movie_info[3]}")
            col18,col19 = st.columns([1,2])
            with col18:
                st.markdown(f"**Release Date:**")
            with col19:
                st.markdown(f"<h6 style='color:green;'>{movie_info[1]}</h6>",unsafe_allow_html=True)
            st.markdown(f"**Tagline:** {movie_info[2]}")
            col20,col21 = st.columns([1,5])
            with col20:
                st.markdown(f"**Rating:**")
            with col21:
                st.markdown(f"<h6 style='color:green;'>{movie_info[4]}</h6>",unsafe_allow_html=True)
            st.markdown(f"**Genre:** {', '.join(map(str, movie_info[5]))}")
    

    col22, col23 , col24 = st.columns(3)
    with col22:
        st.header(recommended[3])
        st.image(posters[3])
        with st.expander("Movie Info"):
            movie_info = info(recommended[3])
            st.markdown(f"**Overview:** {movie_info[3]}")
            col25,col26 = st.columns([1,2])
            with col25:
                st.markdown(f"**Release Date:**")
            with col26:
                st.markdown(f"<h6 style='color:green;'>{movie_info[1]}</h6>",unsafe_allow_html=True)
            st.markdown(f"**Tagline:** {movie_info[2]}")
            col27,col28 = st.columns([1,5])
            with col27:
                st.markdown(f"**Rating:**")
            with col28:
                st.markdown(f"<h6 style='color:green;'>{movie_info[4]}</h6>",unsafe_allow_html=True)
            st.markdown(f"**Genre:** {', '.join(map(str, movie_info[5]))}")
    
    
    with col23:
        st.header(recommended[4])
        st.image(posters[4])
        with st.expander("Movie Info"):
            movie_info = info(recommended[4])
            st.markdown(f"**Overview:** {movie_info[3]}")
            col29,col30 = st.columns([1,2])
            with col29:
                st.markdown(f"**Release Date:**")
            with col30:
                st.markdown(f"<h6 style='color:green;'>{movie_info[1]}</h6>",unsafe_allow_html=True)
            st.markdown(f"**Tagline:** {movie_info[2]}")
            col31,col32 = st.columns([1,5])
            with col31:
                st.markdown(f"**Rating:**")
            with col32:
                st.markdown(f"<h6 style='color:green;'>{movie_info[4]}</h6>",unsafe_allow_html=True)
            st.markdown(f"**Genre:** {', '.join(map(str, movie_info[5]))}")
    

    with col24:
        st.header(recommended[5])
        st.image(posters[5])
        with st.expander("Movie Info"):
            movie_info = info(recommended[5])
            st.markdown(f"**Overview:** {movie_info[3]}")
            col33,col34 = st.columns([1,2])
            with col33:
                st.markdown(f"**Release Date:**")
            with col34:
                st.markdown(f"<h6 style='color:green;'>{movie_info[1]}</h6>",unsafe_allow_html=True)
            st.markdown(f"**Tagline:** {movie_info[2]}")
            col35,col36 = st.columns([1,5])
            with col35:
                st.markdown(f"**Rating:**")
            with col36:
                st.markdown(f"<h6 style='color:green;'>{movie_info[4]}</h6>",unsafe_allow_html=True)
            st.markdown(f"**Genre:** {', '.join(map(str, movie_info[5]))}")
    

