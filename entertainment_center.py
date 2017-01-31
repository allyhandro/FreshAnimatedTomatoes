# author: Ally Han
# entertainment_center uses code from Udacity's fresh_tomatoes.py file to show movies in local web format
# this file holds the instances of my favorite movies and their information.

import fresh_tomatoes
import media


# movie instantiation
httyd = media.Movie("How to Train Your Dragon",
                    "The story of Viking Jay Baruchel and his dragon.",
                    "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg", 
                    "https://www.youtube.com/watch?v=oKiYuIsPxYk&t=78s")


spirited_away = media.Movie("Spirited Away",
                            "A young girls journey to the spirit world and back.",
                            "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG", 
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

paprika = media.Movie("Paprika",
                      "Dream Girl fixes reality.",
                      "https://upload.wikimedia.org/wikipedia/en/1/16/Paprikaposter.jpg",
                      "https://www.youtube.com/watch?v=yn7U1KIGeuQ")

kimi_no_na_wa = media.Movie("Kimi no Na wa (Your Name)",
                                 "High stakes, gorgeous, anime 'Freaky Friday.'",
                                 "https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png", 
                                 "https://www.youtube.com/watch?v=k4xGqY5IDBE")


bakemono_no_ko = media.Movie("Boy and the Beast",
                             "Bearman adopts a boy and brings him to a world of beasts.",
                             "https://upload.wikimedia.org/wikipedia/en/c/c4/The_Boy_and_the_Beast_poster.jpg",
                             "https://www.youtube.com/watch?v=uifJLWoWv8c")


madoka = media.Movie("Madoka Magica: Rebellion",
                       "Third in the series. Magical Girls. Their lives must be so colorful and happy...",
                       "https://upload.wikimedia.org/wikipedia/en/0/00/Madokarebellion.jpg",
                       "https://www.youtube.com/watch?v=HnGESq_CiQY")


#fresh_tomatoes accepts a list of Movie objects
movies = [httyd, spirited_away, paprika, kimi_no_na_wa, bakemono_no_ko, madoka]
fresh_tomatoes.open_movies_page(movies)
