from frameworks.recommender_systems import *

movie_reviews = {
    'Lisa Rose': {'Catch Me If You Can': 3.0, 'Snakes on a Plane': 3.5, 'Superman Returns': 3.5,
                  'You, Me and Dupree': 2.5, 'The Night Listener': 3.0, 'Snitch': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'The Night Listener': 3.0,
                     'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Catch Me If You Can': 2.5, 'Lady in the Water': 2.5, 'Superman Returns': 3.5,
                         'The Night Listener': 4.0, 'Snitch': 2.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0,
                     'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0,
                     'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Catch Me If You Can': 4.5, 'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                      'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'Snitch': 4.5},
    'Toby': {'Snakes on a Plane': 4.5, 'Snitch': 5.0},
    'Michelle Nichols': {'Just My Luck': 1.0, 'The Night Listener': 4.5, 'You, Me and Dupree': 3.5,
                         'Catch Me If You Can': 2.5, 'Snakes on a Plane': 3.0},
    'Gary Coleman': {'Lady in the Water': 1.0, 'Catch Me If You Can': 1.5, 'Superman Returns': 1.5,
                     'You, Me and Dupree': 2.0},
    'Larry': {'Lady in the Water': 3.0, 'Just My Luck': 3.5, 'Snitch': 1.5, 'The Night Listener': 3.5}
}


def tabela_na_slichni_korisnici(reviews):
    slicnosti = {}
    users = []
    for key, value in reviews.items():
        users.append(key)

    for user in users:
        recnik = dict()
        movies = []
        for key,value in reviews.items():
            if user == key:
                for movie,rating in value.items():
                    movies.append(movie)
        for user2 in users:
            if user!=user2:
                counter = 0
                for movie in movies:
                    if movie in reviews[user2].keys():
                        counter+=1

                evk = round(sim_distance(reviews, user, user2), 3)
                pir = round(sim_pearson(reviews, user, user2), 3)
                recnik.setdefault(user2,(evk,pir,counter))
        slicnosti.setdefault(user, recnik)
    return slicnosti


if __name__ == "__main__":
    korisnik1 = input()
    korisnik2 = input()

    tabela = tabela_na_slichni_korisnici(movie_reviews)
    print(tabela[korisnik1][korisnik2])