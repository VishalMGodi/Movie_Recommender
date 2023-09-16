# Movie_Recommender
 A Content-Based Recommender System with a simple UI

-> This recommender model uses about 5000 Hollywood movies until 2016 as its dataset with various features in 2 separate datasets called movies.csv and credits.csv 

-> We combine the datasets in the notebook file and perform a set of preprocessing and NLP techniques on the data to derive meaning from it

-> You can run all cells of the Notebook file where all these tasks take place and in the end it creates 2 new datasets called cleaned_movies.csv and dirty_movies.csv which store the preprocessed data in them and can be used directly while running the UI

-> We use Tf-Idf Vectorizer to create feature vectors for the movies and use cosine similarity to find similarity between the movies

-> The UI is made with streamlit which is a simple web app interface using python and it directly calls the matrix with the similarity scores 
-> To run the file with UI directly, use the command
```streamlit run main.py```

-> Remember to install the requirements from the requirements file before trying it out 

Command: ```pip install -r requirements.txt```

You are free to create a virtual environment for this
