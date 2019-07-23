import sqlite3

open('database.sqlite', 'w').close()

conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

create = (
"""
CREATE TABLE competition(
  competition_id INTEGER PRIMARY key,
  competition_name varchar(25),
  world_record float,
  set_date date
);
""",
"""
CREATE TABLE sportsman(
  sportsman_id integer PRIMARY key,
  sportsman_name varchar(15),
  rank integer,
  year_of_birth year,
  personal_record FLOAT,
  country varchar(20)
);
""",
"""
CREATE TABLE result(
  competition_id INTEGER,
  sportsman_id integer,
  result FLOAT,
  city varchar(15),
  hold_date date,
  FOREIGN key (competition_id) REFERENCES competition (competition_id),
  FOREIGN key (sportsman_id) REFERENCES sportsman (sportsman_id)
);
"""
)

insert = (
"""
INSERT INTO sportsman VALUES
(1, 'Sidorov A.A', 1, 1999, 12.4, 'Russia'),
(2, 'Petrov V.A', 2, 1990, 15.5, 'China'),
(3, 'Ignatenko I.V.', 1, 1996, 12.4, 'Japan'),
(4, 'Moskovich M.A.', 3, 1954, 17.6, 'Germany'),
(5, 'Ivanov P.I.', 1, 1990, 12.1, 'Russia'),
(6, 'Akmeev S.E.', 2, 2005, 26.4, 'Ukrain'),
(7, 'Grenko D.A.', 1, 2001, 12.4, 'Belarus');
""",
"""
INSERT INTO competition VALUES
(1, 'WAAA', 25, '12/05/2010'),
(2, 'WAGV', 12, '15/05/2010'),
(3, 'HDGFS', 2, '2/06/2013'),
(4, 'AQWF', 5, '7/01/2012');
""",
"""
INSERT INTO result VALUES
(1, 1, 12, 'Togliatty', '12/02/2010'),
(1, 2, 10, 'Moscow', '21/05/2010'),
(1, 3, 25, 'Samara', '12/02/2010'),
(2, 4, 67, 'Kazan', '12/05/2011'),
(2, 5, 16, 'Togliatty', '12/03/2010'),
(3, 6, 5, 'Volgograd', '2/01/2000'),
(3, 7, 23, 'Sochi', '12/02/2019');
"""
)

commands = (
	'CREATE TABLE new_table AS SELECT * FROM competition;',
	'SELECT * FROM sportsman;',
	'SELECT competition_name, world_record FROM competition;',
	'SELECT sportsman_name FROM sportsman WHERE year_of_birth=1990;',
	'SELECT competition_name, world_record FROM competition WHERE set_date="12/05/2010" or set_date="15/05/2010";',
	'SELECT hold_date FROM result WHERE city="Moscow" AND result=10;',
	'SELECT sportsman_name FROM sportsman WHERE personal_record < 25;'
)

for cr in create:
	cursor.executescript(cr)
	conn.commit()

for ins in insert:
	cursor.executescript(ins)
	conn.commit()

for comm in commands:
	cursor.execute(comm)
	result = cursor.fetchall()
	print(f'{comm}\n{result}\n\n')
	conn.commit()

conn.close()