DELIMITER //
DROP PROCEDURE IF EXISTS `SemesterInfo` //
CREATE PROCEDURE `SemesterInfo`()
BEGIN
  DECLARE firstRun BOOLEAN DEFAULT TRUE;
  DECLARE done BOOLEAN DEFAULT FALSE;
  DECLARE infoJson JSON DEFAULT '{}';

  -- Current variables
  DECLARE currSemester CHAR(10);
  DECLARE currStudentID INT;

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
    -- If this isn't the first run then we already have data that hasn't been addressed at line 81
    IF firstRun IS TRUE THEN
      FETCH curStudentsInfo INTO currCurSemester, currCurStudentID, currCurStudentName, currCurStudentSSN, currCurCourseNumber;
      SET firstRun = FALSE;
    END IF;

    --  Set up a structure for a new semester
    SET infoJson = JSON_INSERT(infoJson, CONCAT('$."', currCurSemester, '"'), JSON_OBJECT('nemendur', JSON_OBJECT()));

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

      -- Create a student within a semester
      SET infoJson = JSON_INSERT(infoJson, CONCAT('$."', currCurSemester, '".nemendur."', currCurStudentID, '"'), JSON_OBJECT("name", currCurStudentName, "ssn", currCurStudentSSN, "afangar", JSON_ARRAY()));

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

        -- Add class to student
        SET infoJson = JSON_ARRAY_APPEND(infoJson, CONCAT('$."', currCurSemester, '".nemendur."', currCurStudentID, '".afangar'), currCurCourseNumber);
        FETCH curStudentsInfo INTO currCurSemester, currCurStudentID, currCurStudentName, currCurStudentSSN, currCurCourseNumber;


        -- /Code here

      END WHILE; -- End add-class-to-student loop
    END WHILE; -- End add-student-to-semester loop
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

-- 2:
-- Bætið dálkinum schoolInfo við í töfluna Schools. Dálkurinn er af taginu JSon Aflið ykkur upplýsinga um 3 - 5 framhaldsskóla á Íslandi og notið sem grunn að því hvernig þið viljið byggja upp gögnin í schoolInfo. Hér er gott að átta sig á því að þessi gögn þurfa EKKI að vera eins milli skóla.
-- Notið JSon föll til að vista þessar upplýsingar í schoolInfo dálknum og skrifið SP sem
-- sækir þessar upplýsingar úr grunninum.

ALTER TABLE `Schools` ADD COLUMN `schoolInfo` JSON DEFAULT NULL;
INSERT INTO `Schools`(`schoolName`)
VALUES
('Menntaskólinn í Reykjavík'),
('Fjölbrautaskóli Suðurlands'),
('Menntaskólinn við Sund');

SELECT * FROM `Schools`;

UPDATE `Schools`
SET schoolInfo = '{"nafn":"Menntaskólinn í Reykjavík","stuttNafn":"MR","stadsetning":{"lat":64.1460669,"lon":-21.9368808},"starfsfolk":{"1":{"nafn":"Margrét...","titill":"Skólastýra","kennitala":"000000-0000"}}}'
WHERE schoolID = 2;

UPDATE `Schools`
SET schoolInfo = '{"heiti":"Fjölbrautaskóli Suðurlands","skammStafir":"FSu","simi":4808100,"stadur":{"postNumer":800,"gata":"Tryggvagata","gataNr":25},"brautir":{"1":{"heiti":"Grunndeild Rafiðnaða","einingar":120,"student":false,"kennarar":["Þór","Grímur"]}},"storf":{"skolastjori":{"laun":0,"timar":0},"kennariAlmennur":{"laun":0,"timar":0},"kennariIdnadar":{"laun":0,"timar":0},"kennariSertharfir":{"laun":0,"timar":0},"kokkur":{"laun":0,"timar":0}}}'
WHERE schoolID = 3;

UPDATE `Schools`
SET schoolInfo = '{"heiti":"Menntaskólinn við Sund","stuttNafn":"MS","stadsetning":{"lat":0,"lon":0},"fjoldiNemenda":1100,"fjoldiKennara":90,"samstarfsadilar":["Strætó","Erasmus+"],"skrifstofa":{"simi":1234567,"opnun":"Mán-Fös, 8-16"}}'
WHERE schoolID = 4;

DELIMITER //
DROP PROCEDURE IF EXISTS `GetSchoolInfo` //
CREATE PROCEDURE `GetSchoolInfo` (
  `param_schoolID` INT
)
BEGIN
  SELECT schoolInfo FROM `Schools` WHERE `Schools`.schoolID = `param_schoolID`;
END //
DELIMITER ;

CALL `GetSchoolInfo`(2);
