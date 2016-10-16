import media
import fresh_tomatoes

toy_story = media.Movie( "Toy Story" , "A story of boys & his toy come into live",
                            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=vwyZH85NQC4" )
# print(toy_story.title)

avatar = media.Movie( "avatar" , "A marine on an alien planet",
                            "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                            "https://www.youtube.com/watch?v=5PSNL1qE6VY" )
# print(avatar.title)
# avatar.show_trailer()

ddlg = media.Movie( "DDLG" , "A marine on an alien planet",
                            "https://upload.wikimedia.org/wikipedia/en/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg",
                            "https://www.youtube.com/watch?v=Z4uh71stnPM" )

# ddlg.show_trailer()
# movies = [toy_story,avatar,ddlg]
# fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
