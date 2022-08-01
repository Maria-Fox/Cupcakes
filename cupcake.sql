DROP DATABASE IF EXISTS cupcake;

CREATE DATABASE cupcake;

\c cupcake 

CREATE TABLE cupcakes (
  id SERIAL PRIMARY KEY, 
  flavor TEXT not null,
  size TEXT not null,
  rating FLOAT not null,
  image_url TEXT
);

