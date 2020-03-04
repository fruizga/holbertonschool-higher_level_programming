-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- Dexter
SELECT tv_genres.name FROM tv_shows INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_genres.name = 'Comedy' ORDER BY tv_shows.title;
