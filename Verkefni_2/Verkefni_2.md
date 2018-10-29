## Höfundur

_Pétur Steinn Guðmundsson_  

## Áfangi

_GAGN2VG05CU Venslaðir gagnagrunnar 2018H_

# Verkefni 2

#### 1: Design extensions to the ProgressTracker database so that it becomes possible to register students and they can choose a track(within a division).

```sql
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
  INSERT INTO `Students` (
    `studentName`,
    `studentSSN`,
    `trackID`
  )
  VALUES (
    `param_studentName`,
    `param_studentSSN`,
    `param_trackID`
  );

END //
DELIMITER ;
CALL `AddStudent`("Róbert Ingi", "1707001234", 2);
```

* * *

#### 2: Create a trigger for the insert operation on the table Restrictors. The trigger prevents the case of the courseNumber and restrictorID being the same (a course cannot be a restrictor on it self). If this is the case then the trigger prevents the insert by throwing and error and writes a error message. Example of an insert operation that the trigger stops: insert into Restrictors values('GSF2B3U','GSF2B3U',1);

```sql
DELIMITER //
DROP TRIGGER IF EXISTS `DetectSameRestrictorInsert` //
CREATE TRIGGER `DetectSameRestrictorInsert`
BEFORE INSERT ON `Restrictors`
FOR EACH ROW
BEGIN
  IF (new.courseNumber = new.restrictorID) THEN
    signal sqlstate '45000' set message_text = "A course cannot be a restrictor on it self";
  END IF;
END //
DELIMITER ;
```

* * *

#### 3: Write an identical trigger for the update operation on the table Restrictors

```sql
DELIMITER //
DROP TRIGGER IF EXISTS `DetectSameRestrictorUpdate` //
CREATE TRIGGER `DetectSameRestrictorUpdate`
BEFORE UPDATE ON `Restrictors`
FOR EACH ROW
BEGIN
  IF (new.courseNumber = new.restrictorID) THEN
    signal sqlstate '45000' set message_text = "A course cannot be a restrictor on it self";
  END IF;
END //
DELIMITER ;
```

* * *

#### 4: Write a stored procedure that sums up the course credits that a student has finished arranged by the divisions offering these courses.

#### NOTE: The general courses(physics, mathematics, sociology, etc.) actually belong to the General Study Division(Tæknimenntaskólinn NTT13). This in fact means that if the student has completed four, three credit courses of general studies(say math and physics) and five, three credit courses at the computer division(Tölvubraut TBR16) the results would look something like this:

`NTT13 12`  
`TBR16 15`

#### Only courses that are graded >= 5 or are graded ‘passed’ should be chosen.

```sql
DROP TABLE IF EXISTS `StudentCourses`;
CREATE TABLE `StudentCourses` (
  studentID INT NOT NULL,
  trackID INT NOT NULL,
  courseNumber CHAR(10),
  grade FLOAT,
  semester CHAR(10),
  CONSTRAINT FK_studentID_StudentCourses FOREIGN KEY(studentID) REFERENCES Students(studentID),
  CONSTRAINT FK_trackID_StudentCourses FOREIGN KEY(trackID) REFERENCES Tracks(trackID),
  CONSTRAINT FK_courseNumber_StudentCourses FOREIGN KEY(courseNumber) REFERENCES Courses(courseNumber)
);

INSERT INTO `StudentCourses`(studentID, trackID, courseNumber, grade, semester)
VALUES
(1, 9, 'STÆ103', 8.14, '2018V'),
(2, 9, 'GSF2A3U', 7.4, '2018V'),
(3, 6, 'EÐL103', 8.2, '2018V'),
(3, 2, 'STÆ103', 5.6, '2018V'),
(3, 6, 'STÆ203', 3.6, '2018H'),
(3, 6, 'FOR3L3U', 7.5, '2018V'),
(4, 6, 'FOR3D3U', 9.5, '2018V'),
(5, 9, 'STÆ203', 7, '2018V'),
(6, 2, 'STÆ603', 3.3, '2018V');

DELIMITER //
DROP PROCEDURE IF EXISTS `StudentCourseCreditSum` //
CREATE PROCEDURE `StudentCourseCreditSum` (
  `param_studentID` INT
)
BEGIN
	SELECT `Tracks`.trackName, SUM(`Courses`.courseCredits) AS `Credits`
	FROM  `StudentCourses`
	INNER JOIN `Students` ON `StudentCourses`.studentID = `Students`.studentID
	INNER JOIN `Tracks` ON `StudentCourses`.trackID = `Tracks`.trackID
	INNER JOIN `Courses` ON `StudentCourses`.courseNumber = `Courses`.courseNumber
	WHERE `StudentCourses`.studentID = `param_studentID`
    AND `StudentCourses`.grade >= 5
	GROUP BY `Tracks`.trackName;
END //
DELIMITER ;

CALL `StudentCourseCreditSum`(3);
```

* * *

#### 5: Write a cursor that selects all the mandatory courses for a student and puts them into the table that stores the student courses. Put this cursor in a stored procedure that can be called “AddMandatoryCourses” and is run when a student selects courses for the first time. The selection process could be implemented in another stored procedure, perhaps called NewStudentCourses. In that one a check is performed to see if the student has chosen courses before and if that is then the AddMandatoryCourses has already been run and is NOT run again.

```sql
DELIMITER //
DROP PROCEDURE IF EXISTS `AddMandatoryCourses` //
CREATE PROCEDURE `AddMandatoryCourses` (
  param_studentID INT,
  param_trackID INT,
  param_currSemester CHAR(10),
  param_nextSemester CHAR(10)
)
BEGIN

-- Current course number that the cursor holds on to
DECLARE currCourseNumber CHAR(10);
-- A default grade that a student is initialized with when they choose a class; which is a 0
DECLARE defaultGrade INT DEFAULT 0;
-- Is the loop finished
DECLARE finished BOOLEAN DEFAULT FALSE;

-- Get the all of the classes that are mandatory that a student is cabable of taking next semester
DECLARE cur_nextClasses CURSOR FOR
SELECT `TrackCourses`.courseNumber -- , `TrackCourses`.trackID, `TrackCourses`.semester, `Restrictors`.courseNumber, `Restrictors`.restrictorID, `Restrictors`.restrictorType
FROM `TrackCourses`
LEFT JOIN `Restrictors` ON `TrackCourses`.courseNumber = `Restrictors`.courseNumber
WHERE `TrackCourses`.courseNumber
-- Ignore classes that a student is already done with with a grade of >= 5 or ignore any class that student is taking at the moment
NOT IN (
	SELECT `StudentCourses`.courseNumber
	FROM `StudentCourses`
	WHERE `StudentCourses`.studentID = param_studentID
	AND (`StudentCourses`.grade >= 5 OR `StudentCourses`.semester = param_currSemester)
)
-- Get all classes that are flagged as mandatory
AND `TrackCourses`.mandatory != 0
-- Get all classes that are for the decleared track
AND `TrackCourses`.trackID = param_trackID
-- Finally without getting for example STÆ303, STÆ313, STÆ403, STÆ503... you only want the one that you have to take next
-- To do so you've got to look at what is required to take each class, if you're done with what's required then you're assigned to the next class afther that one
-- But let's say you are in STÆ403, you don't need to worry about being assigned again to STÆ103, STÆ203, STÆ303, STÆ313... because it ignores the ones you're already done with
AND
(`Restrictors`.restrictorID IN (
SELECT `StudentCourses`.courseNumber
	FROM `StudentCourses`
	WHERE `StudentCourses`.studentID = param_studentID
	AND (`StudentCourses`.grade >= 5 OR `StudentCourses`.semester = param_currSemester)
)
OR
`Restrictors`.restrictorID IS NULL
);
DECLARE CONTINUE HANDLER FOR NOT FOUND SET FINISHED := TRUE;
OPEN cur_nextClasses;

-- Loop that goes through cur_nextClasses's results
nextClassLoop: LOOP

  -- Get the current course number that's in cur_nextClasses's results
  FETCH cur_nextClasses INTO currCourseNumber;

  -- If we're done then quit
  IF finished THEN
    LEAVE nextClassLoop;
  END IF;

  -- There's a problem where you can be assigned to the same class because there might be two or more restrictors to the same class
  -- An example of this would be as follows

  -- courseNumber   trackID  courseNumber  restrictorID  restrictorType
  -- STÆ303	        9		     STÆ303	       STÆ203	       1
  -- STÆ303	        9		     STÆ303	       STÆ313	       2

INSERT IGNORE INTO `StudentCourses` (studentID, trackID, courseNumber, grade, semester) VALUES (param_studentID, param_trackID, currCourseNumber, defaultGrade, param_nextSemester);

END LOOP nextClassLoop;

END //
DELIMITER ;

CALL `AddMandatoryCourses`(3, 9, '2018V', '2018H');

SELECT `TrackCourses`.courseNumber, `TrackCourses`.trackID, `TrackCourses`.semester, `Restrictors`.courseNumber, `Restrictors`.restrictorID, `Restrictors`.restrictorType
  FROM `TrackCourses`
  LEFT JOIN `Restrictors` ON `TrackCourses`.courseNumber = `Restrictors`.courseNumber
  WHERE `TrackCourses`.courseNumber
  NOT IN (
  	SELECT `StudentCourses`.courseNumber
  	FROM `StudentCourses`
  	WHERE `StudentCourses`.studentID = 1
  	AND (`StudentCourses`.grade >= 5 OR `StudentCourses`.semester = '2019V')
  )
  AND `TrackCourses`.mandatory != 0
  AND `TrackCourses`.trackID = 9
  AND
  (`Restrictors`.restrictorID IN (
  SELECT `StudentCourses`.courseNumber
  	FROM `StudentCourses`
  	WHERE `StudentCourses`.studentID = 1
  	AND (`StudentCourses`.grade >= 5 OR `StudentCourses`.semester = '2019V')
  )
  OR
  `Restrictors`.restrictorID IS NULL);

DELIMITER //
DROP PROCEDURE IF EXISTS `NewStudentCourses` //
CREATE PROCEDURE `NewStudentCourses` (
  param_studentID INT,
  param_trackID INT,
  param_currSemester CHAR(10),
  param_nextSemester CHAR(10),
  param_courseNumber CHAR(10)
)
BEGIN

DECLARE defaultGrade INT DEFAULT 0;

IF ((SELECT COUNT(`StudentCourses`.courseNumber) FROM `StudentCourses` WHERE `StudentCourses`.studentID = param_studentID AND `StudentCourses`.semester = param_nextSemester) = 0) THEN
  CALL `AddMandatoryCourses`(param_studentID, param_trackID, param_currSemester, param_nextSemester);
END IF;

INSERT INTO `StudentCourses` (studentID, trackID, courseNumber, grade, semester) VALUES (param_studentID, param_trackID, param_courseNumber, defaultGrade, param_nextSemester);
END //

DELIMITER ;

-- In order to not allow for duplicates
ALTER TABLE `StudentCourses` ADD UNIQUE `unique_index_st_tr_co_se`(`studentID`, `trackID`, `courseNumber`, `semester`);

CALL `NewStudentCourses`(1, 9, '2019V', '2020H', 'test101');

/*
SELECT * FROM StudentCourses WHERE studentID = 1;
DELETE FROM StudentCourses WHERE studentID = 1 AND courseNumber != 'STÆ103';
INSERT INTO StudentCourses (studentID, trackID, courseNumber, grade, semester) VALUES (1, 9, 'STÆ203', 8.6, '2018H');
INSERT INTO StudentCourses (studentID, trackID, courseNumber, grade, semester) VALUES (1, 9, 'STÆ313', 8.6, '2019V');
*/
/*
SELECT * FROM StudentCourses WHERE studentID = 3;
DELETE FROM StudentCourses WHERE studentID = 3 AND courseNumber = 'EÐL103';
DELETE FROM StudentCourses WHERE studentID = 3 AND courseNumber = 'STÆ203';
DELETE FROM StudentCourses WHERE studentID = 3 AND courseNumber = 'STÆ303';
DELETE FROM StudentCourses WHERE studentID = 3 AND courseNumber = 'STÆ313';
DELETE FROM StudentCourses WHERE studentID = 3 AND courseNumber = 'STÆ403';
DELETE FROM StudentCourses WHERE studentID = 3 AND courseNumber = 'STÆ503';
INSERT INTO StudentCourses (studentID, trackID, courseNumber, grade, semester) VALUES (3, 6, 'EÐL103', 8.6, '2018V');
INSERT INTO StudentCourses (studentID, trackID, courseNumber, grade, semester) VALUES (3, 6, 'STÆ203', 2, '2018V');
INSERT INTO StudentCourses (studentID, trackID, courseNumber, grade, semester) VALUES (3, 6, 'STÆ303', 2, '2018V');
INSERT INTO StudentCourses (studentID, trackID, courseNumber, grade, semester) VALUES (3, 6, 'STÆ313', 2, '2018V');
INSERT INTO StudentCourses (studentID, trackID, courseNumber, grade, semester) VALUES (3, 6, 'STÆ503', 7, '2018V');
INSERT INTO StudentCourses (studentID, trackID, courseNumber, grade, semester) VALUES (3, 6, 'STÆ403', 7, '2018V');
SELECT * FROM TrackCourses WHERE trackID = 9 AND mandatory = 1;
*/
```
