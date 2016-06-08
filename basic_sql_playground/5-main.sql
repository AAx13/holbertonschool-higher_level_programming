SELECT DISTINCT last_name
  FROM Person INNER JOIN TVShowPerson 
  ON Person.id=TVShowPerson.person_id
  AND TVShowPerson.tvshow_id=(SELECT id FROM TVShow WHERE name='Game of Thrones')
  ORDER BY last_name ASC;

SELECT COUNT(age) FROM Person WHERE Person.age > 30;

SELECT Person.id, Person.first_name, Person.last_name, Person.age, EyesColor.color, TVShow.name
  FROM Person INNER JOIN EyesColor, TVShowPerson, TVShow
  ON Person.id=EyesColor.person_id
  AND Person.id=TVShowPerson.person_id
  AND TVShow.id=TVShowPerson.tvshow_id;

SELECT SUM(age) FROM Person;
