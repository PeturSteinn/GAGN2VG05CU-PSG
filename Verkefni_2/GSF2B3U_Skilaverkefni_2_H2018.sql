DROP TABLE IF EXISTS `Students`;
CREATE TABLE `Students`
(
  studentID INT NOT NULL AUTO_INCREMENT,
  studentName VARCHAR(140),
  studentSSN VARCHAR(10),
  trackID INT NOT NULL,
  CONSTRAINT studentTrack FOREIGN KEY(trackID) REFERENCES Tracks(trackID),
  CONSTRAINT student_PK PRIMARY KEY(studentID)
);

INSERT INTO `Students` (studentName, studentSSN, trackID)
VALUES
('Þórir Emilsson', '1505957542', 9),
('Elín Axelsdóttir', '0110929823', 9),
('Birkir Geir Alexandersson', '2001979230', 6),
('Ingvar Hlynsson', '1108993608', 6),
('Reynir Ingvarsson', '1508984089', 9);

DELIMITER //
DROP PROCEDURE IF EXISTS `AddStudent` //
CREATE PROCEDURE `AddStudent` (
  param_studentName VARCHAR(140),
  param_studentSSN VARCHAR(10),
  param_trackID INT
)
BEGIN
  SELECT * FROM `Courses`
  ORDER BY `courseName` ASC;
END //
DELIMITER ;
