-- stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. 
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser (
	IN in_user_id int
)
BEGIN
  DECLARE computes_average FLOAT;
  SELECT SUM(score)/COUNT(*) INTO computes_average FROM corrections WHERE user_id = in_user_id;
  UPDATE users
  SET average_score = computes_average
  WHERE id = in_user_id;
END$$

DELIMITER ;
