import media
import fresh_tomatoes

#Movie is the class that is defined within the media file
#when this is run, __init__ func runs
#some_module.ClassName(): similar to turtle.Turtle()

forgetting_sarah_marshall = media.Movie("Forgetting Sarah Marshall",
                                        "Devastated Peter takes a Hawaiian vacation in order to deal with the recent break-up with his TV star girlfriend, Sarah. Little does he know, Sarah's traveling to the same resort as her ex - and she's bringing along her new boyfriend.",
                                        "https://static.rogerebert.com/uploads/movie/movie_poster/forgetting-sarah-marshall-2008/large_qOU52lsRkXgJiW5oSrLrmTfBcOz.jpg",
                                        "https://www.youtube.com/watch?v=3xuMfKxXnDk")

role_models = media.Movie("Elf",
                          "One of Santa's elves who learns he is actually a human and goes to  New York City to meet his biological father.",
                          "http://www.thebostoncalendar.com/system/events/photos/000/157/944/original/elf-movie-poster-2003-1020190734.jpg?1512394748",
                          "https://www.youtube.com/watch?v=a54yC1etmVc")

no_reservations = media.Movie("No Reservations",
                              "The life of a top chef changes when she becomes the guardian of her young niece.",
                              "https://www.movieposter.com/posters/archive/main/49/MPW-24543",
                              "https://www.youtube.com/watch?v=2-5RJTf0-Jk")                                                                

hot_rod = media.Movie("Hot Rod",
                      "Self-proclaimed stuntman Rod Kimble is preparing for the jump of his life - to clear fifteen buses to raise money for his abusive stepfather Frank's life-saving heart operation.",
                      "http://oneguyrambling.com/wp-content/uploads/2011/12/Hot-Rod.jpg",
                      "https://www.youtube.com/watch?v=8PlrxUzKYoI")

bridesmaids = media.Movie("Bridesmaids",
                          "Competition between the maid of honor and a bridesmaid, over who is the bride's best friend, threatens to upend the life of an out-of-work pastry chef.",
                          "https://www.movieposter.com/posters/archive/main/141/MPW-70687",
                          "https://www.youtube.com/watch?v=1UW9Zks5L2A")                                            

i_love_you_man = media.Movie("I Love You, Man",
                             "Friendless Peter Klaven goes on a series of man-dates to find a Best Man for his wedding.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU4MjI5NTEyNV5BMl5BanBnXkFtZTcwNjQ1NTMzMg@@._V1_UY1200_CR72,0,630,1200_AL_.jpg",
                            "https://www.youtube.com/watch?v=kRLf04gH7mc")

#function open_movies_page takes in a list, so we need to create an list
movies = [forgetting_sarah_marshall, role_models, no_reservations, hot_rod, bridesmaids, i_love_you_man]
fresh_tomatoes.open_movies_page(movies)
