-- creates an index idx_name_first_score on the table names and the first letter of name and the score.
ALTER TABLE names ADD INDEX idx_name_first_score (name(1), score);
