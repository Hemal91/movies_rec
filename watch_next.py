# import spacy module and load en_core_web_md
import spacy
nlp = spacy.load('en_core_web_md')

# create f_movies variable to contain file - set as value None
f_movies = None
# try to open movies.txt to read
try:
    f_movies = open("movies.txt", "r")

    # create empty list for movie descriptions
    movies = []

    # add each line to movies list after removal of "\n"
    for line in f_movies:
        line_update = line.replace("\n", "")
        movies.append(line_update)
# except statement in case file not found.
except FileNotFoundError:
    print("The movies.txt file cannot be found.")
# finally once data read, close file.
finally:
    if f_movies is not None:
        f_movies.close()

# dictionary variable created with one entry, key as movie name 
user_watched_movie_list = ["Planet Hulk"]
user_watched_desc_list = ["""Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""]

# variable created to contain index for movie being compared - with only one movie in above lists index is 0.
movie_comparison = 0

# nlp description from desc_list using movie_comparison
nlp_user_movie = nlp(user_watched_desc_list[movie_comparison])

# create two empty lists to contain the movie name for each movie in "movies" list and similarity to user movie.
movie_names = []
movie_similarity = []
# for loop through each movie description to extract required info for each movie and nlp for each movie description
for item in movies:
    movie_name = item[0:7]
    movie_desc = item[9::]

    nlp_movie_desc = nlp(movie_desc)

    # similarity value compared against nlp_user_movie and data appended to movie_names list and movie_similarity list.
    similarity_with_movie = nlp_user_movie.similarity(nlp_movie_desc)

    movie_names.append(movie_name)
    movie_similarity.append(similarity_with_movie)
    

# creation of variable to track index of value of highest similarity
highest_similarity_index = 0

# for range of len movie_similarity
for index in range(len(movie_similarity)):
    # if movie_similarity is more than similarity of highest_similarity_index replace highest_similarity_indext with index and less than 1
    # less than 1 included here as a value of 1 would mean identical and so to avoid recommending the same movie.
    if movie_similarity[index] > movie_similarity[highest_similarity_index]:
        highest_similarity_index = index

# match percent calculation
movie_perc = round((movie_similarity[highest_similarity_index]*100))

# final print statement to indicate recommended movie using highest_similarity_index with movie_names list.
print(f"\nBased on your recently watched movie \"{user_watched_movie_list[movie_comparison]}\", your recommended movie is \"{movie_names[highest_similarity_index]}\" with a match of {movie_perc}%.\n")