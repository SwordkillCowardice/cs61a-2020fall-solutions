# Q2.1-Q2.3
# SELECT name FROM records WHERE supervisor = "Oliver Warbucks";
# SELECT * FROM records WHERE supervisor = name;
# SELECT name FROM records WHERE salary > 50000 ORDER BY name;

# Q3.1-Q3.4
# SELECT day, time FROM records AS A, meetings AS B 
# WHERE A.supervisor = "Oliver Warbucks" AND A.division = B.division;
# SELECT a.name, b.name FROM records AS a, records AS b WHERE a.division = b.division and a.name < b.name union
# SELECT a.name, b.name FROM records AS a, records AS b, meetings AS c, meetings AS d WHERE a.division = c.division
# and b.division = d.division and c.time = d.time and c.day = d.day and c.division <> d.division and a.name < b.name;
# YES
# SELECT A.name FROM records AS A, records AS B WHERE A.division != B.division AND A.supervisor = B.name;

# Q4.1-Q4.3
# SELECT supervisor, SUM(salary) FROM records GROUP BY supervisor;
# SELECT a.day FROM meetings AS a, records AS b WHERE a.division = b.division GROUP BY a.day having count(*) < 5;
# SELECT a.division FROM records AS a, records AS b WHERE a.division = b.division and a.name < b.name 
# GROUP BY a.division having MAX(a.salary + b.salary) < 100000;

# Q5.1-Q5.3
# CREATE TABLE num_taught AS 
# SELECT professor AS professor, course AS course, COUNT(*) AS times FROM courses GROUP BY professor, course;
# SELECT a.professor, b.professor, a.course FROM num_taught AS a, num_taught AS b 
# WHERE a.times = b.times and a.course = b.course and a.professor < b.professor;
# SELECT a.professor, b.professor FROM courses AS a, courses AS b WHERE a.course = b.course and a.semester = b.semester 
# and a.professor < b.professor GROUP BY a.course, a.professor, b.professor having count(*) >= 2;