import pickle
import re

import pandas as pd
from owner.models import OwnerProducts
from sklearn.feature_extraction.text import TfidfVectorizer


def clear_text(text):
    text = re.sub(r'"{2}|[/]', ' ',
                  text)  # убирает 2 подряд кавычки (") + убирает слэш
    text = re.sub(r'(?<=[а-я])[A-Z]', r' \g<0>',
                  text)  # разделяет пробелом слип. англ. и русское слова
    text = re.sub(r'[A-Za-z](?=[а-я])', r'\g<0> ',
                  text)  # разделяет пробелом слип. англ. и русское слова
    text = re.sub(r'(?<=[А-Я]{2})[а-я]', r' \g<0>',
                  text)  # разделяет пробелом слип. русские слова
    text = re.sub(r'\W', ' ', text)  # убирает знаки препинания
    text = re.sub(r'\d', '', text)  # убирает цифры
    text = text.lower()  # в нижний регистр
    return ' '.join(text.split())


def count_tfidf(data):
    count_tf_idf = TfidfVectorizer()
    count_tf_idf.fit_transform(data)
    return count_tf_idf


def prepare_data():
    owner_products = OwnerProducts.objects.exclude(name_1c='')
    df_product = pd.DataFrame(list(owner_products.values()))
    # main base
    data_product = df_product[['id', 'name_1c', 'recommended_price']].copy()
    data_product = data_product.loc[
        data_product['name_1c'].notna()].reset_index()
    data_product = data_product.drop(['index'], axis=1)
    # normalizing name product in main base
    data_product['clear_name'] = data_product['name_1c'].apply(clear_text)

    return data_product


def fit_tfidf():
    # load dataset
    data_product = prepare_data()
    # fit tf_idf
    fitted_tf_idf = count_tfidf(data_product['clear_name'])
    return fitted_tf_idf


def prepare_query(query):
    # normalizing query name product
    clear_name_product = clear_text(query)
    tfidf = fit_tfidf()
    # calculating tfidf
    query_tfidf = tfidf.transform([clear_name_product])
    return query_tfidf


def load_model():
    with open('data/knn_model.pkl', 'rb') as file:
        clf = pickle.load(file)
    return clf


def matching(query):
    # load clf
    clf = load_model()
    # calc query tfidf
    query_tfidf = prepare_query(query)
    # compute 5 neighbors for query
    neighbors = clf.kneighbors(query_tfidf, n_neighbors=5,
                               return_distance=False)
    data_product = prepare_data()
    result_matching = []
    # listing 5 neighbors
    for i in range(len(neighbors)):
        for j in neighbors[i]:
            result_matching.append(data_product.iloc[j]['name_1c'])
    return result_matching
