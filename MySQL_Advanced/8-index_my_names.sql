-- creates an index idx_name_first on the table names and the first letter of name
ALTER TABLE names ADD INDEX idx_name_first(name(1));
