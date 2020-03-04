-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- aa
SELECT tv_genres.name AS ggenres ON tv_show_genresenre, count(*) AS number_of_shows FROM tv_show_genres INNER JOIN tv_ .genre_id = tv_genres.id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
