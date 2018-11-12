from mysql.connector import MySQLConnection, Error
from .python_mysql_dbconfig import read_db_config


class DbConnector:
    def __init__(self):
        self.db_config = read_db_config()
        self.status = ' '
        try:
            self.conn = MySQLConnection(**self.db_config)
            if self.conn.is_connected():
                self.status = 'OK'
            else:
                self.status = 'connection failed.'
        except Error as error:
            self.status = error

    def execute_function(self, func_header=None, argument_list=None):
        cursor = self.conn.cursor()
        try:
            if argument_list:
                func = func_header % argument_list
            else:
                func = func_header
            cursor.execute(func)
            result = cursor.fetchone()
        except Error as e:
            self.status = e
            result = None
        finally:
            cursor.close()
        return result[0]

    def execute_procedure(self, proc_name, argument_list=None):
        result_list = list()
        cursor = self.conn.cursor()
        try:
            if argument_list:
                cursor.callproc(proc_name, argument_list)
            else:
                cursor.callproc(proc_name)
            self.conn.commit()
            for result in cursor.stored_results():
                result_list = [list(elem) for elem in result.fetchall()]
        except Error as e:
            self.status = e
            print(e)
        finally:
            cursor.close()
        return result_list


class CustomSP(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def deleteCourse(self, param_courseNumber):
        result = self.execute_procedure('DeleteCourse', [param_courseNumber])
        if result: return result
        else: return list()

    def trackOverview(self, paramp_trackID):
        result = self.execute_procedure('TrackOverview', [paramp_trackID])
        if result: return result
        else: return list()

    def trackTotalCredits(self):
        result = self.execute_procedure('TrackTotalCredits')
        if result: return result
        else: return list()

    def courseRestrictorList(self):
        result = self.execute_procedure('CourseRestrictorList')
        if result: return result
        else: return list()

    def restrictorList(self):
        result = self.execute_procedure('RestrictorList')
        if result: return result
        else: return list()

    def addStudent(self, param_studentName, param_studentSSN, param_trackID):
        result = self.execute_procedure('AddStudent', [param_studentName, param_studentSSN, param_trackID])
        if result: return result
        else: return list()

    def studentCourseCreditSum(self, param_studentID):
        result = self.execute_procedure('StudentCourseCreditSum', [param_studentID])
        if result: return result
        else: return list()

    def addMandatoryCourses(self, param_studentID, param_trackID, param_currSemester, param_nextSemester):
        result = self.execute_procedure('AddMandatoryCourses', [param_studentID, param_trackID, param_currSemester, param_nextSemester])
        if result: return result
        else: return list()

    def newStudentCourses(self, param_studentID, param_trackID, param_currSemester, param_nextSemester, param_courseNumber):
        result = self.execute_procedure('AddStudentCourses', [param_studentID, param_trackID, param_currSemester, param_nextSemester, param_courseNumber])
        if result: return result
        else: return list()

    def semesterInfo(self):
        result = self.execute_procedure('SemesterInfo')
        if result: return result[0][0]
        else: return list()

    def getSchoolInfo(self, param_schoolID):
        result = self.execute_procedure('GetSchoolInfo', [param_schoolID])
        if result: return result[0][0]
        else: return list()

class GeneralSP(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def coursesAdd(self, param_courseNumber, param_courseName, param_courseCredits):
        new_id = 0
        result = self.execute_procedure('CoursesAdd', [param_courseNumber, param_courseName, param_courseCredits])
        if result: new_id = int(result[0][0])
        return new_id

    def coursesList(self):
        result = self.execute_procedure('CoursesList')
        if result: return result
        else: return list()

    def coursesSingle(self, param_courseNumber):
        result = self.execute_procedure('CoursesSingle', [param_courseNumber])
        if result: return result
        else: return list()

    def coursesUpdate(self, param_oldCourseNumber, param_newCourseNumber, param_newCourseName, param_newCourseCredits):
        rows_affected = 0
        result = self.execute_procedure('CoursesUpdate', [param_oldCourseNumber, param_newCourseNumber, param_newCourseName, param_newCourseCredits])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def coursesDelete(self):
        rows_affected = 0
        result = self.execute_procedure('CoursesDelete', [])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def divisionsAdd(self, param_divisionName, param_schoolID):
        new_id = 0
        result = self.execute_procedure('DivisionsAdd', [param_divisionName, param_schoolID])
        if result: new_id = int(result[0][0])
        return new_id

    def divisionsList(self):
        result = self.execute_procedure('DivisionsList')
        if result: return result
        else: return list()

    def divisionsSingle(self, param_divisionID):
        result = self.execute_procedure('DivisionsSingle', [param_divisionID])
        if result: return result
        else: return list()

    def divisionsUpdate(self, param_divisionID, param_divisionName, param_schoolID):
        rows_affected = 0
        result = self.execute_procedure('DivisionsUpdate', [param_divisionID, param_divisionName, param_schoolID])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def divisionsDelete(self):
        rows_affected = 0
        result = self.execute_procedure('DivisionsDelete', [])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def restrictorsAdd(self, param_courseNumber, param_restrictorID, param_restrictorType):
        new_id = 0
        result = self.execute_procedure('RestrictorsAdd', [param_courseNumber, param_restrictorID, param_restrictorType])
        if result: new_id = int(result[0][0])
        return new_id

    def restrictorsList(self):
        result = self.execute_procedure('RestrictorsList')
        if result: return result
        else: return list()

    def restrictorsSingle(self, param_courseNumber, param_restrictorID):
        result = self.execute_procedure('RestrictorsSingle', [param_courseNumber, param_restrictorID])
        if result: return result
        else: return list()

    def restrictorsUpdate(self, param_oldCourseNumber, param_oldRestrictorID, param_newCourseNumber, param_newRestrictorID, param_restrictorType):
        rows_affected = 0
        result = self.execute_procedure('RestrictorsUpdate', [param_oldCourseNumber, param_oldRestrictorID, param_newCourseNumber, param_newRestrictorID, param_restrictorType])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def restrictorsDelete(self):
        rows_affected = 0
        result = self.execute_procedure('RestrictorsDelete', [])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def schoolsAdd(self, param_schoolName, param_schoolInfo=None):
        new_id = 0
        result = self.execute_procedure('SchoolsAdd', [param_schoolName, param_schoolInfo])
        if result: new_id = int(result[0][0])
        return new_id

    def schoolsList(self):
        result = self.execute_procedure('SchoolsList')
        if result: return result
        else: return list()

    def schoolsSingle(self, param_schoolID):
        result = self.execute_procedure('SchoolsSingle', [param_schoolID])
        if result: return result
        else: return list()

    def schoolsUpdate(self, param_schoolID, param_schoolName, param_schoolInfo):
        rows_affected = 0
        result = self.execute_procedure('SchoolsUpdate', [param_schoolID, param_schoolName, param_schoolInfo])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def schoolsDelete(self):
        rows_affected = 0
        result = self.execute_procedure('SchoolsDelete', [])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def studentCoursesAdd(self, param_studentID, param_trackID, param_courseNumber, param_grade, param_semester):
        new_id = 0
        result = self.execute_procedure('StudentCoursesAdd', [param_studentID, param_trackID, param_courseNumber, param_grade, param_semester])
        if result: new_id = int(result[0][0])
        return new_id

    def studentCoursesList(self):
        result = self.execute_procedure('StudentCoursesList')
        if result: return result
        else: return list()

    def studentCoursesSingle(self, param_studentID, param_trackID, param_courseNumber, param_semester):
        result = self.execute_procedure('StudentCoursesSingle', [param_studentID, param_trackID, param_courseNumber, param_semester])
        if result: return result
        else: return list()

    def studentCoursesUpdate(self, param_oldStudentID, param_newStudentID, param_oldTrackID, param_newTrackID, param_oldCourseNumber, param_newCourseNumber, param_newGrade, param_oldSemester, param_newSemester):
        rows_affected = 0
        result = self.execute_procedure('StudentCoursesUpdate', [param_oldStudentID, param_newStudentID, param_oldTrackID, param_newTrackID, param_oldCourseNumber, param_newCourseNumber, param_newGrade, param_oldSemester, param_newSemester])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def studentCoursesDelete(self):
        rows_affected = 0
        result = self.execute_procedure('StudentCoursesDelete', [])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def studentsAdd(self, param_studentName, param_studentSSN, param_trackID):
        new_id = 0
        result = self.execute_procedure('StudentsAdd', [param_studentName, param_studentSSN, param_trackID])
        if result: new_id = int(result[0][0])
        return new_id

    def studentsList(self):
        result = self.execute_procedure('StudentsList')
        if result: return result
        else: return list()

    def studentsSingle(self, param_studentID):
        result = self.execute_procedure('StudentsSingle', [param_studentID])
        if result: return result
        else: return list()

    def studentsUpdate(self, param_studentID, param_studentName, param_studentSSN, param_trackID):
        rows_affected = 0
        result = self.execute_procedure('StudentsUpdate', [param_studentID, param_studentName, param_studentSSN, param_trackID])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def studentsDelete(self):
        rows_affected = 0
        result = self.execute_procedure('StudentsDelete', [])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def trackCoursesAdd(self, param_trackID, param_courseNumber, param_semester, param_mandatory):
        new_id = 0
        result = self.execute_procedure('TrackCoursesAdd', [param_trackID, param_courseNumber, param_semester, param_mandatory])
        if result: new_id = int(result[0][0])
        return new_id

    def trackCoursesList(self):
        result = self.execute_procedure('TrackCoursesList')
        if result: return result
        else: return list()

    def trackCoursesSingle(self, param_trackID, param_courseNumber, param_semester=None):
        result = self.execute_procedure('TrackCoursesSingle', [param_trackID, param_courseNumber, param_semester])
        if result: return result
        else: return list()

    def trackCoursesUpdate(self, param_oldTrackID, param_newTrackID, param_oldCourseNumber, param_newCourseNumber, param_oldSemester, param_newSemester, param_newMandatory):
        rows_affected = 0
        result = self.execute_procedure('TrackCoursesUpdate', [param_oldTrackID, param_newTrackID, param_oldCourseNumber, param_newCourseNumber, param_oldSemester, param_newSemester, param_newMandatory])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def trackCoursesDelete(self):
        rows_affected = 0
        result = self.execute_procedure('TrackCoursesDelete', [])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def tracksAdd(self, param_trackName, param_validFrom, param_divisionID):
        new_id = 0
        result = self.execute_procedure('TracksAdd', [param_trackName, param_validFrom, param_divisionID])
        if result: new_id = int(result[0][0])
        return new_id

    def tracksList(self):
        result = self.execute_procedure('TracksList')
        if result: return result
        else: return list()

    def tracksSingle(self, param_trackID):
        result = self.execute_procedure('TracksSingle', [param_trackID])
        if result: return result
        else: return list()

    def tracksUpdate(self, param_trackID, param_trackName, param_validFrom, param_divisionID):
        rows_affected = 0
        result = self.execute_procedure('TracksUpdate', [param_trackID, param_trackName, param_validFrom, param_divisionID])
        if result: rows_affected = int(result[0][0])
        return rows_affected

    def tracksDelete(self):
        rows_affected = 0
        result = self.execute_procedure('TracksDelete', [])
        if result: rows_affected = int(result[0][0])
        return rows_affected

class DescribeSP(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def describeCourses(self):
        result = self.execute_procedure('describeCourses')
        if result: return result
        else: return list()

    def describeDivisions(self):
        result = self.execute_procedure('describeDivisions')
        if result: return result
        else: return list()

    def describeRestrictors(self):
        result = self.execute_procedure('describeRestrictors')
        if result: return result
        else: return list()

    def describeSchools(self):
        result = self.execute_procedure('describeSchools')
        if result: return result
        else: return list()

    def describeStudentCourses(self):
        result = self.execute_procedure('describeStudentCourses')
        if result: return result
        else: return list()

    def describeStudents(self):
        result = self.execute_procedure('describeStudents')
        if result: return result
        else: return list()

    def describeTrackCourses(self):
        result = self.execute_procedure('describeTrackCourses')
        if result: return result
        else: return list()

    def describeTracks(self):
        result = self.execute_procedure('describeTracks')
        if result: return result
        else: return list()
