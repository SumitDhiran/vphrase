import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

def preprocess(file_path: str) -> None:
    from core.models import Movie
    try:
        Movie.objects.all().delete()
        df = pd.read_csv(file_path)

        # removing rows with no movie name
        df = df.dropna(axis=0, subset=['MOVIES'])

        # fixing Gross column
        df["Gross"] = df["Gross"].str.replace("$","").str.replace("M","").astype(float).fillna(0)

        # fixing VOTES column
        # votes_df = df["VOTES"].str.replace(",","")
        # df["VOTES"] = pd.to_numeric(votes_df, errors='coerce')
        df["VOTES"] = df["VOTES"].str.replace(",","").astype(float)

        #filling NaN values using SimpleImputer: good for MCAR Category
        fea_transformer = SimpleImputer(strategy="median")
        df[["RATING","VOTES"]] = fea_transformer.fit_transform(df[["RATING","VOTES"]])

        movie_objs = [
            Movie(
                movie = row["MOVIES"],
                year = row["YEAR"],
                genre = row["GENRE"],
                rating = row["RATING"],
                one_line = row["ONE-LINE"],
                stars = row["STARS"],
                votes = row["VOTES"],
                runtime = row["RunTime"],
                gross = row["Gross"],
            ) for index, row in df.iterrows()
        ]

        Movie.objects.bulk_create(movie_objs)
        print("Record Inserted successfully")

    except Exception as e:
        raise Exception("error: ", str(e))

if __name__ == '__main__':
    import os, sys
    path = os.getcwd()
    print(path)
    sys.path.append(path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vphrase.settings")
    import django
    django.setup()
    preprocess("assignment movies.xlsx - Sheet1.csv")