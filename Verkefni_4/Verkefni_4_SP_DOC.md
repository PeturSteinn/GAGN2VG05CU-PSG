# Documentation of database library

### **Custom Stored Procedures**

## _CourseList_

**Parameters:** _None_
**Description:**
Birtir lista(yfirlit) af öllum áföngum sem geymdir eru í gagnagrunninum. Áfangarnir eru birtir í stafrófsröð.
**Output:** `courseNumber`, `courseName`, `courseCredits`

## _SingleCourse_

**Parameters:** `param_courseNumber CHAR(10)`
**Description:**
Birtir upplýsingar um einn ákveðin kúrs. Færibreytan er áfanganúmerið
**Output:** `courseNumber`, `courseName`, `courseCredits`

## _AddCourse_

**Parameters:**
`param_courseNumber CHAR(10)`
`param_courseName VARCHAR(75)`
`param_courseCredits TINYINT(4)`
**Description:**
Nýskráir áfanga í gagnagrunninn. Skoðið ERD myndina til að finna út hvaða gögn á að vista(hvaða færibreytur á að nota)
AddCourse er með out parameterinn number_of_inserted_rows sem skilar fjölda þeirra raða sem vistaðar voru í gagnagrunninum. Til þess notið þið MySQL function: row_count()
**Output:** `ROW_COUNT`

## _UpdateCourse_

**Parameters:**
`param_oldCourseNumber CHAR(10)`
`param_newCourseNumber CHAR(10)`
`param_newCourseName VARCHAR(75)`
`param_newCourseCredits TINYINT(4)`
**Description:**
Hér eru notaðar sömu færibreytur og í lið 3.  Áfanganúmerið er notað til að uppfæra réttan kúrs row_count( fallið er hér notað líka.
**Output:** `ROW_COUNT`

## _DeleteCourse_

**Parameters:**
`param_courseNumber CHAR(10)`
**Description:**
Áfanganúmer(courseNumber) er notað hérna til að eyða réttum kúrs.
ATH: Ef verið er að nota kúrsinn einhversstaðar(sé hann skráður á TrackCourses) þá má EKKI eyða honum. Sé hins vegar hvergi verið að nota hann má eyða honum úr Courses töflunni og einnig Restrictors töflunni sem fyrr er out parameter notaður til að "skila" fjölda þeirra raða sem eytt var úr töflunni Courses
**Output:** `ROW_COUNT`

## _TrackOverview_

**Parameters:**
`param_trackID INT`
**Description:**
Write a stored procedure TrackOverview()
TrackOverview() displays the name of the track(trackName), number of courses supplied by that track and if possible how high a percentage that course number is of the total number of courses in the database. This is a good place to use the AfangaFjoldi() / NumberOfCourses() from first part of this assignment.
**Output:** `trackName`, `NumOfCourses`, `Percentage`

## _TrackTotalCredits_

**Parameters:** _None_
**Description:**
Write a stored procedure TrackTotalCredits()
TrackTotalCredits() displays track names, division names that the track belongs to and the total number of courses for that track. It would be a good idea to order the results by the total number of courses. The track containing the highest number of courses would be on top and in the case of more than one sharing that number a alphabetical order of track names would be used as well.
**Output:** `trackName`, `divisionName`, `NumOfCourses`

## _CourseRestrictorList_

**Parameters:** _None_
**Description:**
Write a stored procedure CourseRestrictorList()
CourseRestrictorList() displays all course names that are in the database along with their respective restirctors and the type of restrictor(s). If courses are not associated with any restrictors they are displayed wthout these information. Order the results in a way you deem to be helpful for the end user.
NOTE: If a course has more than one restrictor it is listed more than once.
**Output:** `courseNumber`, `restrictorID`, `restrictorType`

## _RestrictorList_

**Parameters:** _None_
**Description:**
Write a stored procedure RestrictorList()
RestrictorList() displays information about all the courses that are restrictors along with the courses they restrict. You could perhaps look at this as a invertet part3 of this assignment.
NOTE: You are given a free play as to the design of this procedure but it has to display a clear results that are profiting to the ProgressTracker system.
**Output:** `restrictorID`, `courseNumber`

## _AddStudent_

**Parameters:**
`param_studentName VARCHAR(140)`
`param_studentSSN VARCHAR(10)`
`param_trackID INT`
**Description:**
Design extensions to the ProgressTracker database so that it becomes possible to register students and they can choose a track(within a division).
**Output:** _None_

## _StudentCourseCreditSum_

**Parameters:**
`param_studentID INT`
**Description:**
Write a stored procedure that sums up the course credits that a student has finished arranged by the divisions offering these courses.

NOTE: The general courses(physics, mathematics, sociology, etc.) actually belong to the General Study Division(Tæknimenntaskólinn NTT13). This in fact means that if the student has completed four, three credit courses of general studies(say math and physics) and five, three credit courses at the computer division(Tölvubraut TBR16) the results would look something like this:

`NTT13 12`  
`TBR16 15`

Only courses that are graded >= 5 or are graded ‘passed’ should be chosen.
**Output:** `trackName`, `Credits`

## _AddMandatoryCourses_

**Parameters:**
`param_studentID INT`
`param_trackID INT`
`param_currSemester CHAR(10)`
`param_nextSemester CHAR(10)`
**Description:**
Write a cursor that selects all the mandatory courses for a student and puts them into the table that stores the student courses. Put this cursor in a stored procedure that can be called “AddMandatoryCourses” and is run when a student selects courses for the first time. The selection process could be implemented in another stored procedure, perhaps called AddStudentCourses. In that one a check is performed to see if the student has chosen courses before and if that is then the AddMandatoryCourses has already been run and is NOT run again.
**Output:** _None_

## _AddStudentCourses_

**Parameters:**
`param_studentID INT`
`param_trackID INT`
`param_currSemester CHAR(10)`
`param_nextSemester CHAR(10)`
`param_courseNumber CHAR(10)`
**Description:**
Write a cursor that selects all the mandatory courses for a student and puts them into the table that stores the student courses. Put this cursor in a stored procedure that can be called “AddMandatoryCourses” and is run when a student selects courses for the first time. The selection process could be implemented in another stored procedure, perhaps called AddStudentCourses. In that one a check is performed to see if the student has chosen courses before and if that is then the AddMandatoryCourses has already been run and is NOT run again.
**Output:** _None_

## _SemesterInfo_

**Parameters:** _None_
**Description:**
Skrifið Stored Procedure "SemesterInfo" sem sækir upplýsingar um nemendur og þau fög sem þeir taka á ákveðinni önn(semester). SemesterInfo skilar JSon formuðum textastreng þar sem listuð eru út nöfn nemenda ásamt þeim áfanganúmerum sem þeir eru í á viðkomandi önn.
**Output:** `infoJson`

## _GetSchoolInfo_

**Parameters** `param_schoolID INT`
**Description**
Bætið dálkinum schoolInfo við í töfluna Schools. Dálkurinn er af taginu JSon Aflið ykkur upplýsinga um 3 - 5 framhaldsskóla á Íslandi og notið sem grunn að því hvernig þið viljið byggja upp gögnin í schoolInfo. Hér er gott að átta sig á því að þessi gögn þurfa EKKI að vera eins milli skóla. Notið JSon föll til að vista þessar upplýsingar í schoolInfo dálknum og skrifið SP sem sækir þessar upplýsingar úr grunninum.
**Output** `schoolInfo`
