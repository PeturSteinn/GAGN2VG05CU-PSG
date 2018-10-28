#### Höfundur

_Pétur Steinn Guðmundsson_  

#### Áfangi

_GAGN2VG05CU Venslaðir gagnagrunnar 2018H_

# Verkefni 1

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
