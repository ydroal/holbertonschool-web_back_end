-- creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$

CREATE PROCEDURE AddBonus (
	IN in_user_id int,
	IN in_project_name varchar(255),
	IN in_score int
)
BEGIN
  DECLARE new_project_id INT;
  SELECT id INTO new_project_id FROM projects WHERE name = in_project_name LIMIT 1;
  IF new_project_id IS NULL THEN
      INSERT INTO projects (name) VALUES (in_project_name);
      SET new_project_id = LAST_INSERT_ID();
  END IF;

	INSERT INTO corrections (user_id, project_id, score)
      VALUES (in_user_id, new_project_id, in_score);
END$$

DELIMITER ;
