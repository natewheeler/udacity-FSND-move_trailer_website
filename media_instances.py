'''
Objective: Create multiple instances of that Python Class to represent
your favorite movies;group all the instances together in a list.
'''

import media_constructor
import fresh_tomatoes

puddle_cruiser = media_constructor.Movie("Puddle Cruiser","http://image.tmdb.org/t/p/w960_and_h1440_bestv2//8saqqv2K5QEZJO8lk8WyK9wQTwV.jpg","https://youtu.be/kz0gYktuLmo")
super_troopers = media_constructor.Movie("Super Troopers","https://da4pli3l5vc0d.cloudfront.net/79/e4/79e4378f7c7c20f812acb8eab6616b123f3b751f","https://youtu.be/2-9D2qUHN-E")
club_dread = media_constructor.Movie("Club Dread","https://da4pli3l5vc0d.cloudfront.net/e9/09/e9097d006e91725c26295f932cc7e29048f95737","https://youtu.be/e2NILS4EIf8")
beerfest = media_constructor.Movie("Beerfest","https://da4pli3l5vc0d.cloudfront.net/aa/7a/aa7a937c796e883852b698e16f4707bb2f5cd4d9","https://youtu.be/aDaxX_bGsDc")
the_slammin_salmon = media_constructor.Movie("The Slammin' Salmon","https://i.jeded.com/i/the-slammin-salmon.32328.jpg","https://youtu.be/4-RjVZ5E3Vg")
super_troopers_2 = media_constructor.Movie("Super Troopers 2","http://image.tmdb.org/t/p/w960_and_h1440_bestv2//8t1WVafwXYrZ1vmaNB3Xc4wrhpE.jpg","https://youtu.be/pa8peFktFi8")


movies = [puddle_cruiser,super_troopers,club_dread,beerfest,the_slammin_salmon,super_troopers_2]

fresh_tomatoes.open_movies_page(movies)


