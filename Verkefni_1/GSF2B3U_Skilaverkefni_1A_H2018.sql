-- ********************** -- Skrifið eftirfarandi stored procedures: --**********************

USE 0408982209_ProgressTracker_V1;

-- Höfundur:
-- Pétur Steinn Guðmundsson
-- GAGN2VG05CU Venslaðir gagnagrunnar 2018H

-- Auka data sem þarf að vera til fyrir eftirfarandi dæmi

INSERT INTO `Tracks` (trackName, divisionID)
VALUES
('TestTrack1', 2),
('TestTrack2', 2),
('TestTrack3', 5);

INSERT INTO TrackCourses (trackID, courseNumber, semester, mandatory)
VALUES
	(9, 'FOR3D3U', 3, 0),
    (9, 'FOR3G3U', 4, 0),
    (9, 'FOR3L3U', 5, 0),
    (9, 'GSF2A3U', 1, 1),
    (9, 'GSF2B3U', 2, 2),
    (9, 'GSF3A3U', 3, 0),
    (9, 'GSF3B3U', 4, 0),
    (9, 'STÆ103', 1, 1),
    (9, 'STÆ203', 2, 1),
    (9, 'STÆ303', 3, 1),
    (9, 'STÆ313', 3, 0),
    (9, 'STÆ403', 4, 1),
    (9, 'STÆ503', 5, 1),
    (9, 'STÆ603', 6, 0),
    (9, 'EÐL103', 1, 1),
    (6, 'EÐL103', 1, 0),
    (6, 'STÆ103', 1, 1),
    (6, 'STÆ203', 2, 1),
    (6, 'STÆ303', 3, 0);



-- 1:	CourseList()
-- Birtir lista(yfirlit) af öllum áföngum sem geymdir eru í gagnagrunninum.
-- Áfangarnir eru birtir í stafrófsröð

DELIMITER //
DROP PROCEDURE IF EXISTS `CourseList` //
CREATE PROCEDURE `CourseList` ()
BEGIN
  SELECT * FROM `Courses`
  ORDER BY `courseName` ASC;
END //
DELIMITER ;
CALL `CourseList`();

-- 2:	SingleCourse()
-- 	Birtir upplýsingar um einn ákveðin kúrs.
--  Færibreytan er áfanganúmerið

DELIMITER //
DROP PROCEDURE IF EXISTS `SingleCourse` //
CREATE PROCEDURE `SingleCourse` (
  `param_courseNumber` CHAR(10)
)
BEGIN
  SELECT * FROM `Courses`
  WHERE `courseNumber` = `param_courseNumber`;
END //
DELIMITER ;
CALL `SingleCourse`('STÆ503');

-- 3:   AddCourse()
--  Nýskráir áfanga í gagnagrunninn.
--  Skoðið ERD myndina til að finna út hvaða gögn á að vista(hvaða færibreytur á að nota)
--  AddCourse er með out parameterinn number_of_inserted_rows sem skilar fjölda þeirra
--  raða sem vistaðar voru í gagnagrunninum.  Til þess notið þið MySQL function: row_count()

DELIMITER //
DROP PROCEDURE IF EXISTS `AddCourse` //
CREATE PROCEDURE `AddCourse`(
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
  SELECT ROW_COUNT();
END //
DELIMITER ;
CALL`AddCourse`('test101', 'Test 101 kúrs', 3);

-- 4:	UpdateCourse()
--  Hér eru notaðar sömu færibreytur og í lið 3.  Áfanganúmerið er notað til að uppfæra réttan kúrs
--  row_count( fallið er hér notað líka.

DELIMITER //
DROP PROCEDURE IF EXISTS `UpdateCourse` //
CREATE PROCEDURE `UpdateCourse`(
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
  SELECT row_count();
END //
DELIMITER ;
CALL `UpdateCourse`('betra', 'betra1', 'Betra Nafn', 4);

-- 5:	DeleteCourse()
-- Áfanganúmer(courseNumber) er notað hérna til að eyða réttum kúrs.
-- ATH: Ef verið er að nota kúrsinn einhversstaðar(sé hann skráður á TrackCourses) þá má EKKI eyða honum.
-- Sé hins vegar hvergi verið að nota hann má eyða honum úr Courses töflunni og einnig Restrictors töflunni.alter
-- sem fyrr er out parameter notaður til að "skila" fjölda þeirra raða sem eytt var úr töflunni COurses

DELIMITER //
DROP PROCEDURE IF EXISTS `DeleteCourse` //
CREATE PROCEDURE `DeleteCourse`(
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
CALL `DeleteCourse`('');


-- ********************** -- Skrifið eftirfarandi functions: --**********************

-- 6:	NumberOfCourses()
-- fallið skilar heildarfjölda allra áfanga í grunninum

DELIMITER //
DROP FUNCTION IF EXISTS `NumberOfCourses` //
CREATE FUNCTION `NumberOfCourses` ()
RETURNS INTEGER
DETERMINISTIC
BEGIN
  RETURN (SELECT COUNT(courseName) FROM `Courses`);
END //
DELIMITER ;
SELECT `NumberOfCourses`();

-- 7:	TotalTrackCredits()
--  Fallið skilar heildar einingafjölda ákveðinnar námsbrautar(track)
--  Senda þarf trackID inn sem færibreytu

DELIMITER //
DROP FUNCTION IF EXISTS `TotalTrackCredits` //
CREATE FUNCTION `TotalTrackCredits` (
  `param_trackID` INT(11)
)
RETURNS INTEGER
DETERMINISTIC
BEGIN
  RETURN (SELECT SUM(courseCredits) FROM `Courses` NATURAL JOIN `TrackCourses` WHERE `trackID` = `param_trackID`);
END //
DELIMITER ;
SELECT `TotalTrackCredits`(9);

-- 8:   HighestCredits()
-- Fallið skilar einingafjölda þess námskeiðs(þeirra námskeiða) sem hafa flestar eininar.
-- ATH:  Það geta fleiri en einn kúrs verið með sama einingafjöldann. :að á ekki að hafa
-- áhfri á niðurstöðuna.

DELIMITER //
DROP FUNCTION IF EXISTS `HighestCredits` //
CREATE FUNCTION `HighestCredits` ()
RETURNS INTEGER
DETERMINISTIC
BEGIN
  RETURN (SELECT MAX(courseCredits) FROM `Courses`);
END //
DELIMITER ;
SELECT `HighestCredits`();

-- 9:  TopTracksDivision()
-- Fallið skilað toppfjölda námsbrauta(tracks) sem tilheyra námsbrautum(Divisions)

DELIMITER //
DROP FUNCTION IF EXISTS `TopTracksDivision` //
CREATE FUNCTION `TopTracksDivision` ()
RETURNS INTEGER
DETERMINISTIC
BEGIN
  DECLARE `MaxTracks` INTEGER;
  SET `MaxTracks` = (SELECT MAX(`count`) FROM
(
 SELECT COUNT(Divisions.divisionName) AS `count`
	FROM `Tracks`
	INNER JOIN `Divisions` ON Tracks.divisionID = Divisions.divisionID
	GROUP BY Divisions.divisionName
	ORDER BY `count` DESC
) AS i);
RETURN `MaxTracks`;
END //
DELIMITER ;
SELECT `TopTracksDivision`();


-- 10:  leastRestrictedCourseNumber()
-- Fallið skilar minnsta fjölda kúrsa í Restrictors töflunni.
-- ATH:  Ef kúrs eða kúrsar eru t.d. með einn undanfara þog ekkert meir þá myndi fallið skila 1



DELIMITER //
DROP FUNCTION IF EXISTS `leastRestrictedCourseNumber` //
CREATE FUNCTION `leastRestrictedCourseNumber` ()
RETURNS INTEGER
DETERMINISTIC
BEGIN
	DECLARE `minUndanfarar` INTEGER;
	SET `minUndanfarar` = (
		SELECT MIN(undanfarar) FROM
		(SELECT courseNumber, COUNT(courseNumber) AS undanfarar FROM
		(SELECT Restrictors.courseNumber, restrictorID, restrictorType FROM `Restrictors` INNER JOIN `Courses` ON Restrictors.`CourseNumber` = Courses.`CourseNumber`) AS coursesAndRes
		GROUP BY courseNumber ORDER BY undanfarar DESC) AS result);
	RETURN `minUndanfarar`;
END //
DELIMITER ;
SELECT `leastRestrictedCourseNumber`();
