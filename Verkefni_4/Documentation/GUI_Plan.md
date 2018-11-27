# Plan for client

-   ### Búa til

    -   Courses

        -   coursesAdd
            `param_courseNumber` CHAR(10),
            `param_courseName` VARCHAR(75),
            `param_courseCredits` TINYINT(4)

    -   Divisions

        -   divisionsAdd
            `param_divisionName` VARCHAR(75),
            `param_schoolID` INT(11)

    -   Restrictors

        -   restrictorsAdd
            `param_courseNumber` CHAR(10),
            `param_restrictorID` CHAR(10),
            `param_restrictorType` CHAR(1)

    -   Schools

        -   schoolsAdd
            `param_schoolName` VARCHAR(75),
            `param_schoolInfo` JSON

    -   StudentCourses

        -   studentCoursesAdd
            `param_studentID` INT(11),
            `param_trackID` INT(11),
            `param_courseNumber` CHAR(10),
            `param_grade` FLOAT,
            `param_semester` CHAR(10)

    -   Students

        -   studentsAdd
            `param_studentName` VARCHAR(140),
            `param_studentSSN` VARCHAR(10),
            `param_trackID` INT(11)

    -   TrackCourses

        -   trackCoursesAdd
            `param_trackID` INT(11),
            `param_courseNumber` CHAR(10),
            `param_semester` TINYINT(3),
            `param_mandatory` TINYINT(3)

    -   Tracks

        -   tracksAdd
            `param_trackName` VARCHAR(75),
            `param_validFrom` DATE,
            `param_divisionID` INT(11)

-   ### Leita

    -   Courses

        -   coursesList

        -   coursesSingle
            `param_courseNumber` CHAR(10)

    -   Divisions

        -   divisionsList

        -   divisionsSingle
            `param_divisionID` INT(11)

    -   Restrictors

        -   restrictorsList

        -   restrictorsSingle
            `param_courseNumber` CHAR(10),
            `param_restrictorID` CHAR(10)

    -   Schools

        -   schoolsList

        -   schoolsSingle
            `param_schoolID` INT(11)

    -   StudentCourses

        -   studentCoursesList

        -   studentCoursesSingle
            `param_studentID` INT(11),
            `param_trackID` INT(11),
            `param_courseNumber` CHAR(10),
            `param_semester` CHAR(10)

    -   Students

        -   studentsList

        -   studentsSingle
            `param_studentID` INT(11)

    -   TrackCourses

        -   trackCoursesList

        -   trackCoursesSingle
            `param_trackID` INT(11),
            `param_courseNumber` CHAR(10)

    -   Tracks

        -   tracksList

        -   tracksSingle
            `param_trackID` INT(11)

-   ### Uppfæra

    -   Courses

        -   coursesUpdate
            `param_oldCourseNumber` CHAR(10),
            `param_newCourseNumber` CHAR(10),
            `param_newCourseName` VARCHAR(75),
            `param_newCourseCredits` TINYINT(4)

    -   Divisions

        -   divisionsUpdate
            `param_divisionID` INT(11),
            `param_divisionName` VARCHAR(75),
            `param_schoolID` INT(11)

    -   Restrictors

        -   restrictorsUpdate
            `param_oldCourseNumber` CHAR(10),
            `param_oldRestrictorID` CHAR(10),
            `param_newCourseNumber` CHAR(10),
            `param_newRestrictorID` CHAR(10),
            `param_restrictorType` CHAR(1)

    -   Schools

        -   schoolsUpdate
            `param_schoolID` INT(11),
            `param_schoolName` VARCHAR(75),
            `param_schoolInfo` JSON

    -   StudentCourses

        -   studentCoursesUpdate
            `param_oldStudentID` INT(11),
            `param_newStudentID` INT(11),
            `param_oldTrackID` INT(11),
            `param_newTrackID` INT(11),
            `param_oldCourseNumber` CHAR(10),
            `param_newCourseNumber` CHAR(10),
            `param_newGrade` FLOAT,
            `param_oldSemester` CHAR(10),
            `param_newSemester` CHAR(10)

    -   Students

        -   studentsUpdate
            `param_studentID` INT(11),
            `param_studentName` VARCHAR(140),
            `param_studentSSN` VARCHAR(10),
            `param_trackID` INT(11)

    -   TrackCourses

        -   trackCoursesUpdate
            `param_oldTrackID` INT(11),
            `param_newTrackID` INT(11),
            `param_oldCourseNumber` CHAR(10),
            `param_newCourseNumber` CHAR(10),
            `param_oldSemester` TINYINT(3),
            `param_newSemester` TINYINT(3),
            `param_newMandatory` TINYINT(3)

    -   Tracks

        -   tracksUpdate
            `param_trackID` INT(11),
            `param_trackName` VARCHAR(75),
            `param_validFrom` DATE,
            `param_divisionID` INT(11)

-   ### Eyða

    -   Courses

        -   coursesDelete
            `param_courseNumber` CHAR(10)

    -   Divisions

        -   divisionsDelete

    -   Restrictors

        -   restrictorsDelete

    -   Schools

        -   schoolsDelete

    -   StudentCourses

        -   studentCoursesDelete

    -   Students

        -   studentsDelete

    -   TrackCourses

        -   trackCoursesDelete

    -   Tracks

        -   tracksDelete


-   ### Extra

    -   Val

        -   Skrá áfanga á nemanda fyrir næstu önn

    -   Statistics

        -   Áfangafjöldi

    -   TotalTrackCredits
