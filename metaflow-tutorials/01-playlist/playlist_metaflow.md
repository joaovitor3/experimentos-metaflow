```python




from metaflow import FlowSpec, step, IncludeFile, Parameter

@step
def start(self):
    columns = ['movie_title', 'genres']

    self.dataframe = dict((column, list()) \
                            for column in columns)

    # Parse the CSV header.
    lines = self.movie_data.split('\n')
    header = lines[0].split(',')
    idx = {column: header.index(column) for column in columns}

    # Populate our dataframe from the lines of the CSV file.
    for line in lines[1:]:
        if not line:
            continue

        fields = line.rsplit(',', 4)
        for column in columns:
            self.dataframe[column].append(fields[idx[column]])

    # Compute genre specific movies and a bonus movie in parallel.
    self.next(self.bonus_movie, self.genre_movies)

@step
def bonus_movie(self):
    from random import choice

    # Find all the movies that are not in the provided genre.
    movies = [(movie, genres) \
                for movie, genres \
                in zip(self.dataframe['movie_title'],
                        self.dataframe['genres']) \
                if self.genre.lower() not in genres.lower()]

    # Choose one randomly.
    self.bonus = choice(movies)

    self.next(self.join)

@step
def genre_movies(self):
    from random import shuffle

    # Find all the movies titles in the specified genre.
    self.movies = [movie \
                    for movie, genres \
                    in zip(self.dataframe['movie_title'],
                            self.dataframe['genres']) \
                    if self.genre.lower() in genres.lower()]

    # Randomize the title names.
    shuffle(self.movies)

    self.next(self.join)

@step
def join(self, inputs):
    # Reassign relevant variables from our branches.
    self.playlist = inputs.genre_movies.movies
    self.bonus = inputs.bonus_movie.bonus

    self.next(self.end)

@step
def end(self):
    print("Playlist for movies in genre '%s'" % self.genre)
    for pick, movie in enumerate(self.playlist, start=1):
        print("Pick %d: '%s'" % (pick, movie))
        if pick >= self.recommendations:
            break

    print("Bonus Pick: '%s' from '%s'" % (self.bonus[0], self.bonus[1]))
```