-- ********************** -- Skrifið eftirfarandi stored procedures: --**********************

USE 0408982209_ProgressTracker_V1;

-- 1:
-- Write a stored procedure TrackOverview()
-- TrackOverview() displays the name of the track(trackName), number of courses
-- supplied by that track and if possible how high a percentage that course number
-- is of the total number of courses in the database. This is a good place to use
-- the AfangaFjoldi() / NumberOfCourses() from first part of this assignment.

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

-- 2:
-- Write a stored procedure TrackTotalCredits()
-- TrackTotalCredits() displays track names, division names that the track
-- belongs to and the total number of courses for that track. It would be a good
-- idea to order the results by the total number of courses. The track containing
-- the highest number of courses would be on top and in the case of more than one
-- sharing that number a alphabetical order of track names would be used as well.

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

-- 3:
-- Write a stored procedure CourseRestrictorList()
-- CourseRestrictorList() displays all course names that are in the database
-- along with their respective restirctors and the type of restrictor(s).
-- If courses are not associated with any restrictors they are displayed wthout
-- these information. Order the results in a way you deem to be helpful for the
-- end user.
-- NOTE: If a course has more than one restrictor it is listed more than once.

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

-- 4:
-- Write a stored procedure RestrictorList()
-- RestrictorList() displays information about all the courses that are
-- restrictors along with the courses they restrict. You could perhaps look at
-- this as a invertet part3 of this assignment.
-- NOTE: You are given a free play as to the design of this procedure but it
-- has to display a clear results that are profiting to the ProgressTracker system.
