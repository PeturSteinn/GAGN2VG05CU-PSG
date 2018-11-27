-- Courses
-- courseNumber, char(10)
-- courseName, varchar(75)
-- courseCredits, tinyint(4)

DELIMITER //
DROP PROCEDURE IF EXISTS `CoursesAdd` //
CREATE PROCEDURE `CoursesAdd` (
  `param_courseNumber` CHAR(10),
  `param_courseName` VARCHAR(75),
  `param_courseCredits` TINYINT(4)
)
BEGIN
  INSERT INTO `Courses` (
    `courseNumber`,
    `courseName`,
    `courseCredits`
  )
  VALUES (
    `param_courseNumber`,
    `param_courseName`,
    `param_courseCredits`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `CoursesList` //
CREATE PROCEDURE `CoursesList` ()
BEGIN
  SELECT * FROM `Courses`
  ORDER BY `courseName`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `CoursesSingle` //
CREATE PROCEDURE `CoursesSingle` (
  `param_courseNumber` CHAR(10)
)
BEGIN
  SELECT * FROM `Courses`
  WHERE `courseNumber` = `param_courseNumber`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `CoursesUpdate` //
CREATE PROCEDURE `CoursesUpdate` (
  `param_oldCourseNumber` CHAR(10),
  `param_newCourseNumber` CHAR(10),
  `param_newCourseName` VARCHAR(75),
  `param_newCourseCredits` TINYINT(4)
)
BEGIN
  UPDATE `Courses`
  SET
  `CourseNumber` = `param_newCourseNumber`,
  `CourseName` = `param_newCourseName`,
  `courseCredits` = `param_newCourseCredits`
  WHERE `CourseNumber` = `param_oldCourseNumber`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `CoursesDelete` //
CREATE PROCEDURE `CoursesDelete` (
  `param_courseNumber` CHAR(10)
)
BEGIN
  IF (SELECT COUNT(`courseNumber`) FROM `TrackCourses` WHERE `courseNumber` = `param_courseNumber`) = 0 AND
     (SELECT COUNT(`courseNumber`) FROM `Restrictors` WHERE `courseNumber` = `param_courseNumber`) = 0 AND
     (SELECT COUNT(`restrictorID`) FROM `Restrictors` WHERE `restrictorID` = `param_courseNumber`) = 0 THEN
     DELETE FROM `Courses`
     WHERE `courseNumber` = `param_courseNumber`;
     END IF;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- /Courses
-- Divisions
-- divisionID, int(11)
-- divisionName, varchar(75)
-- schoolID, int(11)


DELIMITER //
DROP PROCEDURE IF EXISTS `DivisionsAdd` //
CREATE PROCEDURE `DivisionsAdd` (
  `param_divisionName` VARCHAR(75),
  `param_schoolID` INT(11)
)
BEGIN
  INSERT INTO `Divisions` (
    `divisionName`,
    `schoolID`
  )
  VALUES (
    `param_divisionName`,
    `param_schoolID`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `DivisionsList` //
CREATE PROCEDURE `DivisionsList` ()
BEGIN
  SELECT `divisionID`, `divisionName`, `schoolID`
  FROM `Divisions`
  ORDER BY `divisionName` ASC;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `DivisionsSingle` //
CREATE PROCEDURE `DivisionsSingle` (
  `param_divisionID` INT(11)
)
BEGIN
  SELECT `divisionID`, `divisionName`, `schoolID`
  FROM `Divisions`
  WHERE `divisionID` = `param_divisionID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `DivisionsUpdate` //
CREATE PROCEDURE `DivisionsUpdate` (
  `param_divisionID` INT(11),
  `param_divisionName` VARCHAR(75),
  `param_schoolID` INT(11)
)
BEGIN
  UPDATE `Divisions`
  SET
  `divisionName` = `param_divisionName`,
  `schoolID` = `param_schoolID`
  WHERE `divisionID` = `param_divisionID`;
  SELECT ROW_COUNT();
  END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `DivisionsDelete` //
CREATE PROCEDURE `DivisionsDelete` (
  `param_divisionID` INT
)
BEGIN
  IF (SELECT COUNT(`divisionID`) FROM `Tracks` WHERE `divisionID` = `param_divisionID`) = 0 THEN
    DELETE FROM `Divisions`
    WHERE `divisionID` = `param_divisionID`;
  END IF;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- /Divisions
-- Restrictors
-- courseNumber, char(10)
-- restrictorID, char(10)
-- restrictorType, char(1)


DELIMITER //
DROP PROCEDURE IF EXISTS `RestrictorsAdd` //
CREATE PROCEDURE `RestrictorsAdd` (
  `param_courseNumber` CHAR(10),
  `param_restrictorID` CHAR(10),
  `param_restrictorType` CHAR(1)
)
BEGIN
  INSERT INTO `Restrictors` (
    `courseNumber`,
    `restrictorID`,
    `restrictorType`
  )
  VALUES (
    `param_courseNumber`,
    `param_restrictorID`,
    `param_restrictorType`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `RestrictorsList` //
CREATE PROCEDURE `RestrictorsList` ()
BEGIN
  SELECT `courseNumber`, `restrictorID`, `restrictorType`
  FROM `Restrictors`
  ORDER BY `courseNumber` ASC;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `RestrictorsSingle` //
CREATE PROCEDURE `RestrictorsSingle` (
  `param_courseNumber` CHAR(10),
  `param_restrictorID` CHAR(10)
)
BEGIN
  SELECT `courseNumber`, `restrictorID`, `restrictorType`
  FROM `Restrictors`
  WHERE `courseNumber` = `param_courseNumber`
  AND `restrictorID` = `param_restrictorID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `RestrictorsUpdate` //
CREATE PROCEDURE `RestrictorsUpdate` (
  `param_oldCourseNumber` CHAR(10),
  `param_oldRestrictorID` CHAR(10),
  `param_newCourseNumber` CHAR(10),
  `param_newRestrictorID` CHAR(10),
  `param_restrictorType` CHAR(1)
)
BEGIN
  UPDATE `Restrictors`
  SET
  `courseNumber` = `param_newCourseNumber`,
  `restrictorID` = `param_newRestrictorID`,
  `restrictorType` = `param_restrictorType`
  WHERE `courseNumber` = `param_oldCourseNumber`
  AND `restrictorID` = `param_oldRestrictorID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `RestrictorsDelete` //
CREATE PROCEDURE `RestrictorsDelete` (
  `param_courseNumber` CHAR(10),
  `param_restrictorID` CHAR(10)
)
BEGIN
  DELETE FROM `Restrictors`
  WHERE `RestrictorID` = `param_restrictorID`
  AND `CourseNumber` = `param_courseNumber`;
  SELECT ROW_COUNT();
END //
DELIMITER ;


-- /Restrictors
-- Schools
-- schoolID, int(11)
-- schoolName, varchar(75)
-- schoolInfo, json


DELIMITER //
DROP PROCEDURE IF EXISTS `SchoolsAdd` //
CREATE PROCEDURE `SchoolsAdd` (
  `param_schoolName` VARCHAR(75),
  `param_schoolInfo` JSON
)
BEGIN
  INSERT INTO `Schools` (
    `schoolName`,
    `schoolInfo`
  )
  VALUES (
    `param_schoolName`,
    `param_schoolInfo`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `SchoolsList` //
CREATE PROCEDURE `SchoolsList` ()
BEGIN
  SELECT `schoolID`, `schoolName`, `schoolInfo`
  FROM `Schools`
  ORDER BY `schoolName` ASC;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `SchoolsSingle` //
CREATE PROCEDURE `SchoolsSingle` (
  `param_schoolID` INT(11)
)
BEGIN
  SELECT `schoolID`, `schoolName`, `schoolInfo`
  FROM `Schools`
  WHERE `schoolID` = `param_schoolID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `SchoolsUpdate` //
CREATE PROCEDURE `SchoolsUpdate` (
  `param_schoolID` INT(11),
  `param_schoolName` VARCHAR(75),
  `param_schoolInfo` JSON
)
BEGIN
  UPDATE `Schools`
  SET
  `schoolName` = `param_schoolName`,
  `schoolInfo` = `param_schoolInfo`
  WHERE `schoolID` = `param_schoolID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `SchoolsDelete` //
CREATE PROCEDURE `SchoolsDelete` (
  `param_schoolID` INT
)
BEGIN
  IF (SELECT COUNT(`schoolID`) FROM `Divisions` WHERE `schoolID` = `param_schoolID`) = 0 THEN
    DELETE FROM `Schools`
    WHERE `schoolID` = `param_schoolID`;
  END IF;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- /Schools
-- StudentCourses
-- studentID, int(11)
-- trackID, int(11)
-- courseNumber, char(10)
-- grade, float
-- semester, char(10)


DELIMITER //
DROP PROCEDURE IF EXISTS `StudentCoursesAdd` //
CREATE PROCEDURE `StudentCoursesAdd` (
  `param_studentID` INT(11),
  `param_trackID` INT(11),
  `param_courseNumber` CHAR(10),
  `param_grade` FLOAT,
  `param_semester` CHAR(10)
)
BEGIN
  INSERT INTO `StudentCourses` (
    `studentID`,
    `trackID`,
    `courseNumber`,
    `grade`,
    `semester`
  )
  VALUES (
    `param_studentID`,
    `param_trackID`,
    `param_courseNumber`,
    `param_grade`,
    `param_semester`
  );
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `StudentCoursesList` //
CREATE PROCEDURE `StudentCoursesList` ()
BEGIN
  SELECT `studentID`, `trackID`, `courseNumber`, `grade`, `semester`
  FROM `StudentCourses`
  ORDER BY `studentID`; -- `semester`, `studentID` ASC;

END //
DELIMITER ;


DELIMITER //
DROP PROCEDURE IF EXISTS `StudentCoursesSingle` //
CREATE PROCEDURE `StudentCoursesSingle` (
  `param_studentID` INT(11),
  `param_trackID` INT(11),
  `param_courseNumber` CHAR(10),
  `param_semester` CHAR(10)
)
BEGIN
  SELECT `studentID`, `trackID`, `courseNumber`, `grade`, `semester`
  FROM `StudentCourses`
  WHERE `studentID` = `param_studentID`
  AND `trackID` = `param_trackID`
  AND `courseNumber` = `param_courseNumber`
  AND `semester` = `param_semester`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `StudentCoursesUpdate` //
CREATE PROCEDURE `StudentCoursesUpdate` (
  `param_oldStudentID` INT(11),
  `param_newStudentID` INT(11),
  `param_oldTrackID` INT(11),
  `param_newTrackID` INT(11),
  `param_oldCourseNumber` CHAR(10),
  `param_newCourseNumber` CHAR(10),
  `param_newGrade` FLOAT,
  `param_oldSemester` CHAR(10),
  `param_newSemester` CHAR(10)
)
BEGIN
  UPDATE `StudentCourses`
  SET
  `studentID` = `param_newStudentID`,
  `trackID` = `param_newTrackID`,
  `courseNumber` = `param_newCourseNumber`,
  `grade` = `param_newGrade`,
  `semester` = `param_newSemester`
  WHERE `studentID` = `param_oldStudentID`
  AND `trackID` = `param_oldTrackID`
  AND `courseNumber` = `param_oldCourseNumber`
  AND `semester` = `param_oldSemester`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `StudentCoursesDelete` //
CREATE PROCEDURE `StudentCoursesDelete` (
  `param_studentID` INT,
  `param_trackID` INT,
  `param_courseNumber` CHAR(10),
  `param_semester` CHAR(10)
)
BEGIN
  DELETE FROM `StudentCourses`
  WHERE `studentID` = `param_studentID` AND
  `trackID` = `param_trackID` AND
  `courseNumber` = `param_courseNumber` AND
  `semester` = `param_semester`;
END //
DELIMITER ;

-- /StudentCourses
-- Students
-- studentID, int(11)
-- studentName, varchar(140)
-- studentSSN, varchar(10)
-- trackID, int(11)


DELIMITER //
DROP PROCEDURE IF EXISTS `StudentsAdd` //
CREATE PROCEDURE `StudentsAdd` (
  `param_studentName` VARCHAR(140),
  `param_studentSSN` VARCHAR(10),
  `param_trackID` INT(11)
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
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `StudentsList` //
CREATE PROCEDURE `StudentsList` ()
BEGIN
  SELECT `studentID`, `studentName`, `studentSSN`, `trackID`
  FROM `Students`
  ORDER BY `studentName` ASC;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `StudentsSingle` //
CREATE PROCEDURE `StudentsSingle` (
  `param_studentID` INT(11)
)
BEGIN
  SELECT `studentID`, `studentName`, `studentSSN`, `trackID`
  FROM `Students`
  WHERE `studentID` = `param_studentID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `StudentsUpdate` //
CREATE PROCEDURE `StudentsUpdate` (
  `param_studentID` INT(11),
  `param_studentName` VARCHAR(140),
  `param_studentSSN` VARCHAR(10),
  `param_trackID` INT(11)
)
BEGIN
  UPDATE `Students`
  SET
  `studentName` = `param_studentName`,
  `studentSSN` = `param_studentSSN`,
  `trackID` = `param_trackID`
  WHERE `studentID` = `param_studentID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `StudentsDelete` //
CREATE PROCEDURE `StudentsDelete` (
  `param_studentID` INT
)
BEGIN
  IF (SELECT COUNT(`studentID`) FROM `StudentCourses` WHERE `studentID` = `param_studentID`) = 0 THEN
    DELETE FROM `Students`
    WHERE `studentID` = `param_studentID`;
  END IF;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- /Students
-- TrackCourses
-- trackID, int(11)
-- courseNumber, char(10)
-- semester, tinyint(3) unsigned
-- mandatory, tinyint(3) unsigned


DELIMITER //
DROP PROCEDURE IF EXISTS `TrackCoursesAdd` //
CREATE PROCEDURE `TrackCoursesAdd` (
  `param_trackID` INT(11),
  `param_courseNumber` CHAR(10),
  `param_semester` TINYINT(3),
  `param_mandatory` TINYINT(3)
)
BEGIN
  INSERT INTO `TrackCourses` (
    `trackID`,
    `courseNumber`,
    `semester`,
    `mandatory`
  )
  VALUES (
    `param_trackID`,
    `param_courseNumber`,
    `param_semester`,
    `param_mandatory`
  );
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `TrackCoursesList` //
CREATE PROCEDURE `TrackCoursesList` ()
BEGIN
  SELECT `trackID`, `courseNumber`, `semester`, `mandatory`
  FROM `TrackCourses`
  ORDER BY `trackID`, `courseNumber` ASC;
END //
DELIMITER ;


DELIMITER //
DROP PROCEDURE IF EXISTS `TrackCoursesSingle` //
CREATE PROCEDURE `TrackCoursesSingle` (
  `param_trackID` INT(11),
  `param_courseNumber` CHAR(10)
)
BEGIN
  SELECT `trackID`, `courseNumber`, `semester`, `mandatory`
  FROM `TrackCourses`
  WHERE `trackID` = `param_trackID`
  AND `courseNumber` = `param_courseNumber`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `TrackCoursesUpdate` //
CREATE PROCEDURE `TrackCoursesUpdate` (
  `param_oldTrackID` INT(11),
  `param_newTrackID` INT(11),
  `param_oldCourseNumber` CHAR(10),
  `param_newCourseNumber` CHAR(10),
  `param_newSemester` TINYINT(3),
  `param_newMandatory` TINYINT(3)
)
BEGIN
  UPDATE `TrackCourses`
  SET
  `trackID` = `param_newTrackID`,
  `courseNumber` = `param_newCourseNumber`,
  `semester` = `param_newSemester`,
  `mandatory` = `param_newMandatory`
  WHERE `trackID` = `param_oldTrackID`
  AND `courseNumber` = `param_oldCourseNumber`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `TrackCoursesDelete` //
CREATE PROCEDURE `TrackCoursesDelete` (
  `param_trackID` INT,
  `param_courseNumber` CHAR(10)
)
BEGIN
  DELETE FROM `TrackCourses`
  WHERE `trackID` = `param_trackID` AND
  `courseNumber` = `param_courseNumber`;
END //
DELIMITER ;

-- /TrackCourses
-- Tracks
-- trackID, int(11)
-- trackName, varchar(75)
-- validFrom, date
-- divisionID, int(11)


DELIMITER //
DROP PROCEDURE IF EXISTS `TracksAdd` //
CREATE PROCEDURE `TracksAdd` (
  `param_trackName` VARCHAR(75),
  `param_validFrom` DATE,
  `param_divisionID` INT(11)
)
BEGIN
  INSERT INTO `Tracks` (
    `trackName`,
    `validFrom`,
    `divisionID`
  )
  VALUES (
    `param_trackName`,
    `param_validFrom`,
    `param_divisionID`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `TracksList` //
CREATE PROCEDURE `TracksList` ()
BEGIN
  SELECT `trackID`, `trackName`, `validFrom`, `divisionID`
  FROM `Tracks`
  ORDER BY `divisionID`, `trackName` ASC;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `TracksSingle` //
CREATE PROCEDURE `TracksSingle` (
  `param_trackID` INT(11)
)
BEGIN
  SELECT `trackID`, `trackName`, `validFrom`, `divisionID`
  FROM `Tracks`
  WHERE `trackID` = `param_trackID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `TracksUpdate` //
CREATE PROCEDURE `TracksUpdate` (
  `param_trackID` INT(11),
  `param_trackName` VARCHAR(75),
  `param_validFrom` DATE,
  `param_divisionID` INT(11)
)
BEGIN
  UPDATE `Tracks`
  SET
  `trackName` = `param_trackName`,
  `validFrom` = `param_validFrom`,
  `divisionID` = `param_divisionID`
  WHERE `trackID` = `param_trackID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `TracksDelete` //
CREATE PROCEDURE `TracksDelete` (
  `param_trackID` INT
)
BEGIN
  IF (SELECT COUNT(`trackID`) FROM `StudentCourses` WHERE `trackID` = `param_trackID`) = 0 AND
     (SELECT COUNT(`trackID`) FROM `Students` WHERE `trackID` = `param_trackID`) = 0 AND
     (SELECT COUNT(`trackID`) FROM `TrackCourses` WHERE `trackID` = `param_trackID`) = 0 THEN
    DELETE FROM `Tracks`
    WHERE `trackID` = `param_trackID`;
  END IF;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- Get info about tables

DELIMITER //
DROP PROCEDURE IF EXISTS `describeCourses` //
CREATE PROCEDURE `describeCourses`()
BEGIN
	SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = '0408982209_progresstracker_v1'
  AND TABLE_NAME = 'courses';
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `describeDivisions` //
CREATE PROCEDURE `describeDivisions`()
BEGIN
	SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = '0408982209_progresstracker_v1'
  AND TABLE_NAME = 'divisions';
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `describeRestrictors` //
CREATE PROCEDURE `describeRestrictors`()
BEGIN
	SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = '0408982209_progresstracker_v1'
  AND TABLE_NAME = 'restrictors';
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `describeSchools` //
CREATE PROCEDURE `describeSchools`()
BEGIN
	SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = '0408982209_progresstracker_v1'
  AND TABLE_NAME = 'schools';
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `describeStudentCourses` //
CREATE PROCEDURE `describeStudentCourses`()
BEGIN
	SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = '0408982209_progresstracker_v1'
  AND TABLE_NAME = 'studentcourses';
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `describeStudents` //
CREATE PROCEDURE `describeStudents`()
BEGIN
	SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = '0408982209_progresstracker_v1'
  AND TABLE_NAME = 'students';
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `describeTrackCourses` //
CREATE PROCEDURE `describeTrackCourses`()
BEGIN
	SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = '0408982209_progresstracker_v1'
  AND TABLE_NAME = 'trackcourses';
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `describeTracks` //
CREATE PROCEDURE `describeTracks`()
BEGIN
	SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = '0408982209_progresstracker_v1'
  AND TABLE_NAME = 'tracks';
END //
DELIMITER ;

-- Custom

DELIMITER //
DROP PROCEDURE IF EXISTS `GetNextClasses` //
CREATE PROCEDURE `GetNextClasses`(
  `param_studentID` INT,
  `param_trackID` INT,
  `param_currSemester` CHAR(10)
)
BEGIN
  SELECT `TrackCourses`.courseNumber, `Restrictors`.restrictorID, `TrackCourses`.semester, `Restrictors`.restrictorType -- `TrackCourses`.courseNumber, `TrackCourses`.trackID, `TrackCourses`.semester, `Restrictors`.courseNumber, `Restrictors`.restrictorID, `Restrictors`.restrictorType
    FROM `TrackCourses`
    LEFT JOIN `Restrictors` ON `TrackCourses`.courseNumber = `Restrictors`.courseNumber
    WHERE `TrackCourses`.courseNumber
    NOT IN (
    	SELECT `StudentCourses`.courseNumber
    	FROM `StudentCourses`
    	WHERE `StudentCourses`.studentID = `param_studentID`
    	AND (`StudentCourses`.grade >= 5 OR `StudentCourses`.semester = `param_currSemester`)
    )
    AND `TrackCourses`.mandatory != 0
    AND `TrackCourses`.trackID = `param_trackID`
    AND
    (`Restrictors`.restrictorID IN (
    SELECT `StudentCourses`.courseNumber
    	FROM `StudentCourses`
    	WHERE `StudentCourses`.studentID = `param_studentID`
    	AND (`StudentCourses`.grade >= 5 OR `StudentCourses`.semester = `param_currSemester`)
    )
    OR
    `Restrictors`.restrictorID IS NULL);
END //
DELIMITER ;

CALL `GetNextClasses`(3, 9, '2020H');
