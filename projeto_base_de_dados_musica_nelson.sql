-- create database music_interface;
use music_interface;

drop table if exists soundtracks;
drop table if exists artists;
create table artists(
artist_id int auto_increment primary key,
artist_name varchar(50)
);

insert into artists(artist_name) values ("Lana del Rey");
insert into artists(artist_name) values ("Beyoncé");
insert into artists(artist_name) values ("Eminem");
insert into artists(artist_name) values ("Kendrick Lamar");
insert into artists(artist_name) values ("Linkin Park");
insert into artists(artist_name) values ("Limp Bizkit");
insert into artists(artist_name) values ("Dua Lipa");
insert into artists(artist_name) values ("Kanye West");
insert into artists(artist_name) values ("Bad Bunny");
insert into artists(artist_name) values ("Taylor Swift");

#select*
#from artists;

drop table if exists albums;
create table albums(
album_id int auto_increment primary key,
album_name varchar(100) 
);

insert into albums (album_name) values ("Born to die");
insert into albums (album_name) values ("Lemonade");
insert into albums (album_name) values ("Encore");
insert into albums (album_name) values ("Damn");
insert into albums (album_name) values ("Meteora");
insert into albums (album_name) values ("Chocolate Starfish and The Hot dog Flavored Water");
insert into albums (album_name) values ("Future Nostalgia");
insert into albums (album_name) values ("Graduation");
insert into albums (album_name) values ("Nadie Sabe Lo Que Va a Pasar Mañana");
insert into albums (album_name) values ("Midnights");

#select*
#from albums;



create table soundtracks(
soundtracks_id int auto_increment primary key,
title varchar(100),
duration time,
genre varchar(50),
artist_id int,
album_id int,
foreign key (artist_id) references artists(artist_id),
foreign key (album_id) references albums(album_id)
);



#criar registos
insert into soundtracks(title, duration, genre, artist_id, album_id) values ("Video Games", 0442, "Pop", 1, 1);
insert into soundtracks(title, duration, genre, artist_id, album_id) values ("Hold Up", 0341, "R&B", 2, 2);
insert into soundtracks(title, duration, genre, artist_id, album_id) values ("Like Toy Soldiers", 0457, "Hiphop/Rap", 3, 3);
insert into soundtracks(title, duration, genre, artist_id, album_id) values ("Damn", 0306, "Hiphop/Rap", 4, 4);
insert into soundtracks(title, duration, genre, artist_id, album_id) values ("Don't Stay", 0308, "Metal/Rock", 5, 5);
insert into soundtracks(title, duration, genre, artist_id, album_id) values ("Take a Look Around", 0520, "Metal/Rock", 6, 6);
insert into soundtracks(title, duration, genre, artist_id, album_id) values ("Hallucinate", 0329, "Pop", 7, 7);
insert into soundtracks(title, duration, genre, artist_id, album_id) values ("Can't Tell Me Nothing", 0431, "HipHop/Rap", 8, 8);
insert into soundtracks(title, duration, genre, artist_id, album_id) values ("Monaco", 0428, "Reggaeton/indie pop", 9, 9);
insert into soundtracks(title, duration, genre, artist_id, album_id) values ("Anti-Hero", 0322, "Pop", 10, 10);

select *
from soundtracks;

select soundtracks_id, title, artist_name
from soundtracks s right join artists ar
on s.artist_id = ar.artist_id;





