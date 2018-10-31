DELIMITER //
DROP PROCEDURE IF EXISTS `SemesterInfo` //
CREATE PROCEDURE `SemesterInfo`()
BEGIN
  DECLARE firstRun BOOLEAN DEFAULT TRUE;
  DECLARE done BOOLEAN DEFAULT FALSE;
  DECLARE infoJson JSON DEFAULT '[]';

  -- Current variables
  DECLARE currSemesterIndex INT UNSIGNED DEFAULT 0;
  DECLARE currStudentIndex INT UNSIGNED DEFAULT 0;
  DECLARE currSemester CHAR(10);
  DECLARE currStudentID INT;
  DECLARE currStudentName VARCHAR(140);
  DECLARE currStudentSSN VARCHAR(10);
  DECLARE currCourseNumber CHAR(10);

  -- Current cursor variables
  DECLARE currCurSemester CHAR(10);
  DECLARE currCurStudentID INT;
  DECLARE currCurStudentName VARCHAR(140);
  DECLARE currCurStudentSSN VARCHAR(10);
  DECLARE currCurCourseNumber CHAR(10);

  -- Main cursor
  DECLARE curStudentsInfo CURSOR FOR SELECT `StudentCourses`.semester, `Students`.studentID, `Students`.studentName,`Students`.studentSSN, `StudentCourses`.courseNumber
  FROM `StudentCourses`
  INNER JOIN `Students` ON `StudentCourses`.studentID = `Students`.studentID
  ORDER BY `StudentCourses`.semester;

  -- Continue handler
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done := TRUE;

  -- Open main cursor
  OPEN curStudentsInfo;

  -- Loop through cursor
  infoLoop: LOOP
    IF done THEN -- Check if main cursor is done
      CLOSE curStudentsInfo;
      LEAVE infoLoop;
    END IF;
    -- Code here

    -- If this is the first run then fetch information now
    -- If this isn't the first run then we already have data that hasn't been addressed at line [PUT IN LINE]
    IF firstRun IS TRUE THEN
      FETCH curStudentsInfo INTO currCurSemester, currCurStudentID, currCurStudentName, currCurStudentSSN, currCurCourseNumber;
      SET firstRun = FALSE;
    END IF;

    --  Set up a structure for a new semester
    SET infoJson = JSON_ARRAY_APPEND(infoJson, '$', JSON_OBJECT(currCurSemester, JSON_OBJECT("nemendur", JSON_ARRAY())));

    -- /Code here

    -- Add students to semester here below
    -- Keep track of what semester we're dealing with, if this changes then we back up and create a new semester
    SET currSemester = currCurSemester;
    WHILE currSemester = currCurSemester DO -- While semester is the same
      IF done THEN -- Check if main cursor is done
        CLOSE curStudentsInfo;
        LEAVE infoLoop;
      END IF;
      -- Code here

      SET currStudentID = currCurStudentID;
      SET currStudentName = currCurStudentName;
      SET currStudentSSN = currCurStudentSSN;
      SET currCourseNumber = currCurCourseNumber;

      -- Create a student within a semester
      SET infoJson = JSON_ARRAY_APPEND(infoJson, CONCAT('$[', currSemesterIndex, ']."', currCurSemester, '".nemendur'), JSON_OBJECT(currCurStudentID, JSON_OBJECT("name", currCurStudentName, "ssn", currCurStudentSSN, "afangar", JSON_ARRAY())));

      -- /Code here

      -- Add classes to student here below
      -- Keep track of which student we're dealing with, if this changes we back up and create a new student
      SET currStudentID = currCurStudentID;
      WHILE currStudentID = currCurStudentID DO -- While student is the same
        IF done THEN -- Check if main cursor is done
          CLOSE curStudentsInfo;
          LEAVE infoLoop;
        END IF;
        -- Code here

        SET currCourseNumber = currCurCourseNumber;

        -- Add class to student
        SET infoJson = JSON_ARRAY_APPEND(infoJson, CONCAT('$[', currSemesterIndex, ']."', currCurSemester, '".nemendur[', currStudentIndex, ']."', currCurStudentID, '".afangar'), currCurCourseNumber);
        FETCH curStudentsInfo INTO currCurSemester, currCurStudentID, currCurStudentName, currCurStudentSSN, currCurCourseNumber;

        -- /Code here

      END WHILE; -- End add-class-to-student loop

      -- In order to navigate to a student (which is stored in a list in json) we have to keep track of an index
      SET currStudentIndex = currStudentIndex + 1;

    END WHILE; -- End add-student-to-semester loop

  -- In order to navigate to a semester (which is stored in a list in json) we have to keep track of an index
  SET currSemesterIndex = currSemesterIndex + 1;

  -- When we switch to a new semester we reset the studentIndex to 0
  SET currStudentIndex = 0;
  END LOOP infoLoop;

  -- Finish with returning the complete JSON string
  SELECT infoJson;
END //
DELIMITER ;

CALL `SemesterInfo`();

-- The query that's used
-- SELECT `StudentCourses`.semester, `Students`.studentID, `Students`.studentName,`Students`.studentSSN, `StudentCourses`.courseNumber
-- FROM `StudentCourses`
-- INNER JOIN `Students` ON `StudentCourses`.studentID = `Students`.studentID
-- ORDER BY `StudentCourses`.semester;


ALTER TABLE `Schools` ADD COLUMN `schoolInfo` JSON DEFAULT NULL;
INSERT INTO `Schools`(`schoolName`, `schoolInfo`)
VALUES
('Menntaskólinn í Reykjavík', ),
('Verzlunarskóli Íslands'),
('Menntaskólinn við Sund'),
('Menntaskólinn að Laugarvatni'),
('Fjölbrautaskóli Suðurlands');

SELECT * FROM `Schools`;
