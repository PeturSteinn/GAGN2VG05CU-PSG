## Höfundur

_Pétur Steinn Guðmundsson_  

## Áfangi

_GAGN2VG05CU Venslaðir gagnagrunnar 2018H_

# Verkefni 1A

#### Auka data sem þarf að vera til staðar

```sql
INSERT INTO `Tracks` (trackName, divisionID)
VALUES
('TestTrack1', 2),
('TestTrack2', 2),
('TestTrack3', 5);

INSERT INTO TrackCourses (trackID, courseNumber, mandatory)
VALUES
    (9, 'FOR3D3U', 1),
    (9, 'FOR3G3U', 1),
    (9, 'FOR3L3U', 0),
    (9, 'GSF2A3U', 1),
    (9, 'GSF2B3U', 0),
    (9, 'GSF3A3U', 0),
    (9, 'GSF3B3U', 0),
    (9, 'STÆ103', 1),
    (9, 'STÆ203', 1),
    (9, 'STÆ303', 1),
    (9, 'STÆ313', 1),
    (9, 'STÆ403', 1),
    (9, 'STÆ503', 1),
    (9, 'STÆ603', 0),
    (9, 'EÐL103', 1),
    (6, 'EÐL103', 0),
    (6, 'STÆ103', 1),
    (6, 'STÆ203', 1),
    (6, 'STÆ303', 0);
```

* * *

#### 1:	CourseList()

#### Birtir lista(yfirlit) af öllum áföngum sem geymdir eru í gagnagrunninum. Áfangarnir eru birtir í stafrófsröð

```sql
DELIMITER //
DROP PROCEDURE IF EXISTS `CourseList` //
CREATE PROCEDURE `CourseList` ()
BEGIN
  SELECT * FROM `Courses`
  ORDER BY `courseName` ASC;
END //
DELIMITER ;
CALL `CourseList`();
```

* * *

#### 2:	SingleCourse()

#### Birtir upplýsingar um einn ákveðin kúrs. Færibreytan er áfanganúmerið

```sql
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
```

* * *

#### 3:   NewCourse()

#### Nýskráir áfanga í gagnagrunninn. Skoðið ERD myndina til að finna út hvaða gögn á að vista(hvaða færibreytur á að nota)

#### NewCourse er með out parameterinn number_of_inserted_rows sem skilar fjölda þeirra raða sem vistaðar voru í gagnagrunninum.  Til þess notið þið MySQL function: row_count()

```sql
DELIMITER //
DROP PROCEDURE IF EXISTS `NewCourse` //
CREATE PROCEDURE `NewCourse`(
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
CALL`NewCourse`('test101', 'Test 101 kúrs', 3);
```

* * *

#### 4:	UpdateCourse()

#### Hér eru notaðar sömu færibreytur og í lið 3.  Áfanganúmerið er notað til að uppfæra réttan kúrs row_count( fallið er hér notað líka.

```sql
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
```

* * *

#### 5:	DeleteCourse()

#### Áfanganúmer(courseNumber) er notað hérna til að eyða réttum kúrs. ATH: Ef verið er að nota kúrsinn einhversstaðar(sé hann skráður á TrackCourses) þá má EKKI eyða honum. Sé hins vegar hvergi verið að nota hann má eyða honum úr Courses töflunni og einnig Restrictors töflunni sem fyrr er out parameter notaður til að "skila" fjölda þeirra raða sem eytt var úr töflunni COurses

```sql
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
```

* * *

#### 6:	NumberOfCourses()

#### Fallið skilar heildarfjölda allra áfanga í grunninum

```sql
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
```

* * *

#### 7:	TotalTrackCredits()

#### Fallið skilar heildar einingafjölda ákveðinnar námsbrautar(track). Senda þarf trackID inn sem færibreytu

```sql
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
```

* * *

#### 8: HighestCredits()

#### Fallið skilar einingafjölda þess námskeiðs(þeirra námskeiða) sem hafa flestar eininar. ATH: Það geta fleiri en einn kúrs verið með sama einingafjöldann. Það á ekki að hafa áhfri á niðurstöðuna.

```sql
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
```

* * *

#### 9: TopTracksDivision()

#### Fallið skilað toppfjölda námsbrauta(tracks) sem tilheyra námsbrautum(Divisions)

```sql
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
```

* * *

#### 10: leastRestrictedCourseNumber()

#### Fallið skilar minnsta fjölda kúrsa í Restrictors töflunni. ATH: Ef kúrs eða kúrsar eru t.d. með einn undanfara þog ekkert meir þá myndi fallið skila 1

```sql
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
```

* * *

# Verkefni 1B

#### 1: Write a stored procedure

#### TrackOverview() TrackOverview() displays the name of the track(trackName), number of courses supplied by that track and if possible how high a percentage that course number is of the total number of courses in the database. This is a good place to use the AfangaFjoldi() / NumberOfCourses() from first part of this assignment.

```sql
DELIMITER //
DROP PROCEDURE IF EXISTS `TrackOverview` //
CREATE PROCEDURE `TrackOverview` (
  `param_trackID` INT
)
BEGIN
	SELECT `Tracks`.trackName,
	COUNT(`TrackCourses`.courseNumber) AS NumOfCourses,
	CONCAT(TRUNCATE((COUNT(`TrackCourses`.courseNumber) / NumberOfCourses()) * 100, 2), "%") AS Percentage
	FROM `Tracks`
	INNER JOIN `TrackCourses` ON `Tracks`.trackID = `TrackCourses`.trackID
	WHERE `Tracks`.trackID = param_trackID;
END //
DELIMITER ;
CALL `TrackOverview`(9);
```

* * *

#### 2: Write a stored procedure TrackTotalCredits()

#### TrackTotalCredits() displays track names, division names that the track belongs to and the total number of courses for that track. It would be a good idea to order the results by the total number of courses. The track containing the highest number of courses would be on top and in the case of more than one sharing that number a alphabetical order of track names would be used as well.

```sql
DELIMITER //
DROP PROCEDURE IF EXISTS `TrackTotalCredits` //
CREATE PROCEDURE `TrackTotalCredits` ()
BEGIN
	SELECT `trackName`, `divisionName`, COUNT(`TrackCourses`.trackID) AS NumOfCourses
	FROM `TrackCourses`
	INNER JOIN `Tracks` ON `TrackCourses`.trackID = `Tracks`.trackID
	INNER JOIN `Divisions` ON `Tracks`.divisionID = `Divisions`.divisionID
	GROUP BY `Tracks`.trackName ORDER BY NumOfCourses DESC;
END //
DELIMITER ;
CALL `TrackTotalCredits`();
```

* * *

#### 3: Write a stored procedure CourseRestrictorList()

#### CourseRestrictorList() displays all course names that are in the database along with their respective restirctors and the type of restrictor(s). If courses are not associated with any restrictors they are displayed wthout these information. Order the results in a way you deem to be helpful for the end user. NOTE: If a course has more than one restrictor it is listed more than once.

```sql
DELIMITER //
DROP PROCEDURE IF EXISTS `CourseRestrictorList` //
CREATE PROCEDURE `CourseRestrictorList`()
BEGIN
	SELECT `Courses`.courseNumber,
	`Restrictors`.restrictorID,
	`Restrictors`.restrictorType
	FROM `Restrictors`
	RIGHT OUTER JOIN `Courses` ON `Restrictors`.courseNumber = `Courses`.courseNumber
	ORDER BY `Courses`.courseNumber;
END //
DELIMITER ;
CALL `CourseRestrictorList`();
```

#### 4: Write a stored procedure RestrictorList()

#### RestrictorList() displays information about all the courses that are restrictors along with the courses they restrict. You could perhaps look at this as a invertet part3 of this assignment. NOTE: You are given a free play as to the design of this procedure but it has to display a clear results that are profiting to the ProgressTracker system.

```sql
DELIMITER //
DROP PROCEDURE IF EXISTS `RestrictorList` //
CREATE PROCEDURE `RestrictorList`()
BEGIN
	SELECT `restrictorID`, `courseNumber` FROM `Restrictors`
	ORDER BY `restrictorID`;
END //
DELIMITER ;
CALL `RestrictorList`();
```
