import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)
        self.df['overview'] = self.df['overview'].fillna('')
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.df['overview'])
        self.cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    def recommend(self, title, top_n=5):
        try:
            idx = self.df[self.df['title'] == title].index[0]
        except IndexError:
            return ["Movie not found in database!"]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1]
        movie_indices = [i[0] for i in sim_scores]
        return self.df['title'].iloc[movie_indices].tolist()
