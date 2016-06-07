INSERT INTO EyesColor (person_id, color) VALUES (6, 'Brown');
INSERT INTO EyesColor (person_id, color) VALUES (7, 'Green');

CREATE TABLE TVShow (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  name char(128) NOT NULL
);

CREATE TABLE TVShowPerson (
  tvshow_id INTEGER NOT NULL,
  person_id INTEGER NOT NULL,
  FOREIGN KEY(tvshow_id) REFERENCES TVShow(id),
  FOREIGN KEY(person_id) REFERENCES Person(id)
);

INSERT INTO TVShow (name) VALUES ('Homeland');
INSERT INTO TVShow (name) VALUES ('The big bang theory');
INSERT INTO TVShow (name) VALUES ('Game of Thrones');
INSERT INTO TVShow (name) VALUES ('Breaking Bad');

INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (4, 2);
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (3, 3);
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (2, 4);
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (3, 5);
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (3, 6);
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (3, 7);

SELECT * FROM Person;
SELECT * FROM EyesColor;
SELECT * FROM TVShow;
SELECT * FROM TVShowPerson;
