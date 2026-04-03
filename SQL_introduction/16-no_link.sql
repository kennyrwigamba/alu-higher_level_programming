-- List score and name where name is not null or empty, ordered by score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
  AND name != ''
ORDER BY score DESC;
