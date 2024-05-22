-- Lists all records of the table second_table
-- No records without a name value
-- Results should display the score and the name
-- Records should be listed by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
