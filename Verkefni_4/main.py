import sys, datetime
from lib.ProgressTrackerConnect import *
from Frames.mainWindow import Ui_ProgressTracker
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtGui import QPixmap

def getCurrSemester():
    currDate = datetime.datetime.now()
    if currDate.month > 6: return "{}H".format(currDate.year)
    else: return "{}V".format(currDate.year)

def getNextSemester(sem):
    if sem[-1] == "H": return "{}V".format(int(sem[:-1]) + 1)
    else: return "{}H".format(sem[:-1])

def generateSemesters():
    start = "2015V"
    end = "{}{}".format(datetime.datetime.now().year + 3, start[-1])
    semesters = [start]
    semester = start

    while(semester != end):
        semester = getNextSemester(semester)
        semesters.append(semester)
    return semesters

class MainWindow(QtWidgets.QMainWindow, Ui_ProgressTracker):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # General navigation
        self.createItem.clicked.connect(lambda: self.display(self.createPage, self.createTabWidget))
        self.readItem.clicked.connect(lambda: self.display(self.readPage, self.readTabWidget))
        self.updateItem.clicked.connect(lambda: self.display(self.updatePage, self.updateTabWidget))
        self.deleteItem.clicked.connect(lambda: self.display(self.deletePage, self.deleteTabWidget))
        self.extra.clicked.connect(lambda: self.display(self.extraPage, self.extraTabWidget))

        # CreatePage
        self.pushButton.clicked.connect(self.handleCreateCourse)
        self.pushButton_2.clicked.connect(self.handleCreateDivision)
        self.pushButton_3.clicked.connect(self.handleCreateRestrictor)
        self.pushButton_4.clicked.connect(self.handleCreateSchool)
        self.pushButton_5.clicked.connect(self.handleCreateStudentCourses)
        self.pushButton_6.clicked.connect(self.handleCreateStudent)
        self.pushButton_7.clicked.connect(self.handleCreateTrackCourse)
        self.pushButton_8.clicked.connect(self.handleCreateTrack)

        # ReadPage
        self.pushButton_10.clicked.connect(self.handleReadCourse)
        self.pushButton_11.clicked.connect(self.handleReadDivision)
        self.pushButton_12.clicked.connect(self.handleReadRestrictor)
        self.pushButton_13.clicked.connect(self.handleReadSchool)
        self.pushButton_14.clicked.connect(self.handleReadStudentCourses)
        self.pushButton_20.clicked.connect(self.handleReadStudent)
        self.pushButton_27.clicked.connect(self.handleReadTrackCourse)
        self.pushButton_28.clicked.connect(self.handleReadTrack)

        # UpdatePage
        self.pushButton_9.clicked.connect(self.handleUpdateCourse)
        self.pushButton_29.clicked.connect(self.handleUpdateDivision)
        self.pushButton_30.clicked.connect(self.handleUpdateRestrictor)
        self.pushButton_31.clicked.connect(self.handleUpdateSchool)
        self.pushButton_32.clicked.connect(self.handleUpdateStudentCourses)
        self.pushButton_33.clicked.connect(self.handleUpdateStudent)
        self.pushButton_34.clicked.connect(self.handleUpdateTrackCourse)
        self.pushButton_35.clicked.connect(self.handleUpdateTrack)

        self.pushButton_44.clicked.connect(self.handleUpdateClearCourses)
        self.pushButton_45.clicked.connect(self.handleUpdateClearDivision)
        self.pushButton_46.clicked.connect(self.handleUpdateClearRestrictor)
        self.pushButton_47.clicked.connect(self.handleUpdateClearSchool)
        self.pushButton_48.clicked.connect(self.handleUpdateClearStudentCourses)
        self.pushButton_49.clicked.connect(self.handleUpdateClearStudent)
        self.pushButton_50.clicked.connect(self.handleUpdateClearTrackCourse)
        self.pushButton_51.clicked.connect(self.handleUpdateClearTrack)

        self.pushButton_36.clicked.connect(self.handleUpdateSearchCourse)
        self.pushButton_37.clicked.connect(self.handleUpdateSearchDivision)
        self.pushButton_38.clicked.connect(self.handleUpdateSearchRestrictor)
        self.pushButton_39.clicked.connect(self.handleUpdateSearchSchool)
        self.pushButton_40.clicked.connect(self.handleUpdateSearchStudentCourses)
        self.pushButton_41.clicked.connect(self.handleUpdateSearchStudent)
        self.pushButton_42.clicked.connect(self.handleUpdateSearchTrackCourse)
        self.pushButton_43.clicked.connect(self.handleUpdateSearchTrack)

        # DeletePage
        self.pushButton_15.clicked.connect(self.handleDeleteCourse)
        self.pushButton_16.clicked.connect(self.handleDeleteDivisions)
        self.pushButton_17.clicked.connect(self.handleDeleteRestrictors)
        self.pushButton_18.clicked.connect(self.handleDeleteSchools)
        self.pushButton_19.clicked.connect(self.handleDeleteStudentCourses)
        self.pushButton_21.clicked.connect(self.handleDeleteStudents)
        self.pushButton_22.clicked.connect(self.handleDeleteTrackCourses)
        self.pushButton_23.clicked.connect(self.handleDeleteTracks)

        self.pushButton_52.clicked.connect(self.handleDeleteClearCourse)
        self.pushButton_54.clicked.connect(self.handleDeleteClearDivisions)
        self.pushButton_56.clicked.connect(self.handleDeleteClearRestrictors)
        self.pushButton_58.clicked.connect(self.handleDeleteClearSchools)
        self.pushButton_60.clicked.connect(self.handleDeleteClearStudentCourses)
        self.pushButton_62.clicked.connect(self.handleDeleteClearStudents)
        self.pushButton_64.clicked.connect(self.handleDeleteClearTrackCourses)
        self.pushButton_66.clicked.connect(self.handleDeleteClearTracks)

        self.pushButton_53.clicked.connect(self.handleDeleteSearchCourse)
        self.pushButton_55.clicked.connect(self.handleDeleteSearchDivisions)
        self.pushButton_57.clicked.connect(self.handleDeleteSearchRestrictors)
        self.pushButton_59.clicked.connect(self.handleDeleteSearchSchools)
        self.pushButton_61.clicked.connect(self.handleDeleteSearchStudentCourses)
        self.pushButton_63.clicked.connect(self.handleDeleteSearchStudents)
        self.pushButton_65.clicked.connect(self.handleDeleteSearchTrackCourses)
        self.pushButton_67.clicked.connect(self.handleDeleteSearchTracks)

        # ExtraPage

        self.pushButton_70.clicked.connect(self.handleExtraValSearchStud)
        self.pushButton_69.clicked.connect(self.handleExtraValClear)
        self.pushButton_68.clicked.connect(self.handleExtraValSearchStudentCourses)

        self.pushButton_71.clicked.connect(self.handleExtraValNextSemSearchStud)
        self.pushButton_72.clicked.connect(self.handleExtraValNextSemClear)
        self.pushButton_73.clicked.connect(self.handleExtraValNextSemSearchNextSem)

        self.pushButton_24.clicked.connect(self.handleExtraValBtn)

        # Tabs
        self.createTabWidget.currentChanged['int'].connect(lambda: self.onTab(self.createTabWidget, self.createTabWidget.currentIndex()))
        self.readTabWidget.currentChanged['int'].connect(lambda: self.onTab(self.readTabWidget, self.readTabWidget.currentIndex()))
        self.updateTabWidget.currentChanged['int'].connect(lambda: self.onTab(self.updateTabWidget, self.updateTabWidget.currentIndex()))
        self.deleteTabWidget.currentChanged['int'].connect(lambda: self.onTab(self.deleteTabWidget, self.deleteTabWidget.currentIndex()))
        self.extraTabWidget.currentChanged['int'].connect(lambda: self.onTab(self.extraTabWidget, self.extraTabWidget.currentIndex()))

        self.onTab(self.createTabWidget, self.createTabWidget.currentIndex())
        self.show()

    def onTab(self, currWidg, currInd):
        print("CurrentWidget: {} | CurrentIndex: {}".format(currWidg.objectName(), currInd))
        general = GeneralSP()
        describe = DescribeSP()

        if currWidg.objectName() == "readTabWidget":
            if currInd == 0:
                self.treeWidget.setHeaderLabels([i[0] for i in describe.describeCourses()])     # List
                self.treeWidget_2.setHeaderLabels([i[0] for i in describe.describeCourses()])   # Search
                self.treeWidget.clear()
                for i in general.coursesList(): QtWidgets.QTreeWidgetItem(self.treeWidget, list(map(str, i)))

            elif currInd == 1:
                self.treeWidget_4.setHeaderLabels([i[0] for i in describe.describeDivisions()]) # List
                self.treeWidget_3.setHeaderLabels([i[0] for i in describe.describeDivisions()]) # Search
                self.treeWidget_4.clear()
                for i in general.divisionsList(): QtWidgets.QTreeWidgetItem(self.treeWidget_4, list(map(str, i)))

            elif currInd == 2:
                self.treeWidget_6.setHeaderLabels([i[0] for i in describe.describeRestrictors()]) # List
                self.treeWidget_5.setHeaderLabels([i[0] for i in describe.describeRestrictors()]) # Search
                self.treeWidget_6.clear()
                for i in general.restrictorsList(): QtWidgets.QTreeWidgetItem(self.treeWidget_6, list(map(str, i)))

            elif currInd == 3:
                self.treeWidget_8.setHeaderLabels([i[0] for i in describe.describeSchools()]) # List
                self.treeWidget_7.setHeaderLabels([i[0] for i in describe.describeSchools()]) # Search
                self.treeWidget_8.clear()
                for i in general.schoolsList(): QtWidgets.QTreeWidgetItem(self.treeWidget_8, list(map(str, i)))

            elif currInd == 4:
                self.treeWidget_10.setHeaderLabels([i[0] for i in describe.describeStudentCourses()]) # List
                self.treeWidget_9.setHeaderLabels([i[0] for i in describe.describeStudentCourses()]) # Search
                self.treeWidget_10.clear()
                for i in general.studentCoursesList(): QtWidgets.QTreeWidgetItem(self.treeWidget_10, list(map(str, i)))

            elif currInd == 5:
                self.treeWidget_21.setHeaderLabels([i[0] for i in describe.describeStudents()]) # List
                self.treeWidget_22.setHeaderLabels([i[0] for i in describe.describeStudents()]) # Search
                self.treeWidget_21.clear()
                for i in general.studentsList(): QtWidgets.QTreeWidgetItem(self.treeWidget_21, list(map(str, i)))

            elif currInd == 6:
                self.treeWidget_35.setHeaderLabels([i[0] for i in describe.describeTrackCourses()]) # List
                self.treeWidget_36.setHeaderLabels([i[0] for i in describe.describeTrackCourses()]) # Search
                self.treeWidget_35.clear()
                for i in general.trackCoursesList(): QtWidgets.QTreeWidgetItem(self.treeWidget_35, list(map(str, i)))

            elif currInd == 7:
                self.treeWidget_38.setHeaderLabels([i[0] for i in describe.describeTracks()]) # List
                self.treeWidget_37.setHeaderLabels([i[0] for i in describe.describeTracks()]) # Search
                self.treeWidget_38.clear()
                for i in general.tracksList(): QtWidgets.QTreeWidgetItem(self.treeWidget_38, list(map(str, i)))

        elif currWidg.objectName() == "deleteTabWidget":
            if currInd == 0: self.treeWidget_39.setHeaderLabels([i[0] for i in describe.describeCourses()])   # Search
            elif currInd == 1: self.treeWidget_40.setHeaderLabels([i[0] for i in describe.describeDivisions()]) # Search
            elif currInd == 2: self.treeWidget_41.setHeaderLabels([i[0] for i in describe.describeRestrictors()]) # Search
            elif currInd == 3: self.treeWidget_42.setHeaderLabels([i[0] for i in describe.describeSchools()]) # Search
            elif currInd == 4: self.treeWidget_43.setHeaderLabels([i[0] for i in describe.describeStudentCourses()]) # Search
            elif currInd == 5: self.treeWidget_44.setHeaderLabels([i[0] for i in describe.describeStudents()]) # Search
            elif currInd == 6: self.treeWidget_45.setHeaderLabels([i[0] for i in describe.describeTrackCourses()]) # Search
            elif currInd == 7: self.treeWidget_46.setHeaderLabels([i[0] for i in describe.describeTracks()]) # Search

        elif currWidg.objectName() == "extraTabWidget":
            customFunc = CustomF()
            if currInd == 0:
                stats = customFunc.statistics()
                self.label_70.setText("Áfangar: {}".format(stats['coursesCount']))
                self.label_71.setText("Greinar: {}".format(stats['divisionsCount']))
                self.label_72.setText("Takmarkanir: {}".format(stats['restrictorsCount']))
                self.label_73.setText("Skólar: {}".format(stats['schoolsCount']))
                self.label_74.setText("Brautir: {}".format(stats['tracksCount']))
                self.label_75.setText("Áfangar á brautum: {}".format(stats['trackCoursesCount']))
                self.label_76.setText("Nemendur: {}".format(stats['studentsCount']))
                self.label_77.setText("Áfangar á nemendum: {}".format(stats['studentCoursesCount']))

            if currInd == 1:
                self.treeWidget_12.setHeaderLabels(['Áfangi', 'Undanfari', 'Önn', 'restrictorType'])

                self.comboBox_16.clear()
                self.comboBox_16.addItems(generateSemesters())
                index = self.comboBox_16.findText(getCurrSemester(), QtCore.Qt.MatchFixedString)
                if index >= 0: self.comboBox_16.setCurrentIndex(index)

            elif currInd == 2:
                self.treeWidget_11.setHeaderLabels([i[0] for i in describe.describeStudentCourses()])

    def display(self, i, currWidg):
        self.stackedWidget.setCurrentWidget(i)
        self.onTab(currWidg, currWidg.currentIndex())

    # Create handlers
    def handleCreateCourse(self):
        print("Pressed Skrá áfanga")
        general = GeneralSP()
        general.coursesAdd(self.lineEdit_10.text(), self.lineEdit_11.text(), self.spinBox.value())

    def handleCreateDivision(self):
        print("Pressed Skrá grein")
        general = GeneralSP()
        general.divisionsAdd(self.lineEdit_12.text(), self.lineEdit_8.text())

    def handleCreateRestrictor(self):
         print("Pressed Skrá takmörk")
         general = GeneralSP()
         general.restrictorsAdd(self.lineEdit_20.text(), self.lineEdit_21.text(), self.comboBox_3.currentText())

    def handleCreateSchool(self):
        print("Pressed Skrá skóla")
        json = self.lineEdit_14.text()
        if not json: json = None
        general = GeneralSP()
        general.schoolsAdd(self.lineEdit_13.text(), json)

    def handleCreateStudentCourses(self):
        print("Pressed Skrá áfanga á nemanda")
        general = GeneralSP()
        general.studentCoursesAdd(self.lineEdit_24.text(), self.lineEdit_23.text(), self.lineEdit_22.text(), self.doubleSpinBox.value(), self.comboBox_7.currentText())

    def handleCreateStudent(self):
        print("Pressed Skrá nemanda")
        general = GeneralSP()
        general.studentsAdd(self.lineEdit_16.text(), self.lineEdit_18.text(), self.lineEdit_25.text())

    def handleCreateTrackCourse(self):
        print("Pressed Skrá áfanga á braut")
        sem = self.comboBox_8.currentText()
        if self.comboBox_8.currentText() == "None": sem = None # Vesen
        general = GeneralSP()
        general.trackCoursesAdd(self.lineEdit_26.text(), self.lineEdit_30.text(), sem, self.comboBox_12.currentText())

    def handleCreateTrack(self):
        print("Pressed Skrá braut")
        general = GeneralSP()
        print(self.lineEdit_19.text(), self.dateEdit.date().toPyDate(), self.lineEdit_31.text())
        general.tracksAdd(self.lineEdit_19.text(), self.dateEdit.date().toPyDate(), self.lineEdit_31.text())

    # Read handlers
    def handleReadCourse(self):
        print("Pressed Leita (Áfangar)")
        general = GeneralSP()
        self.treeWidget_2.clear()
        for i in general.coursesSingle(self.lineEdit.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_2, list(map(str, i)))

    def handleReadDivision(self):
        print("Pressed Leita (Greinar)")
        general = GeneralSP()
        self.treeWidget_3.clear()
        for i in general.divisionsSingle(self.lineEdit_2.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_3, list(map(str, i)))

    def handleReadRestrictor(self):
        print("Pressed Leita (Takmörk)")
        general = GeneralSP()
        self.treeWidget_5.clear()
        for i in general.restrictorsSingle(self.lineEdit_3.text(), self.lineEdit_4.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_5, list(map(str, i)))

    def handleReadSchool(self):
        print("Pressed Leita (Skólar)")
        general = GeneralSP()
        self.treeWidget_7.clear()
        for i in general.schoolsSingle(self.lineEdit_6.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_7, list(map(str, i)))

    def handleReadStudentCourses(self):
        print("Pressed Leita (Áfangi á nemanda)")
        general = GeneralSP()
        self.treeWidget_9.clear()
        for i in general.studentCoursesSingle(self.lineEdit_7.text(), self.lineEdit_5.text(), self.lineEdit_9.text(), self.comboBox_14.currentText()): QtWidgets.QTreeWidgetItem(self.treeWidget_9, list(map(str, i)))

    def handleReadStudent(self):
        print("Pressed Leita (Nemendur)")
        general = GeneralSP()
        self.treeWidget_22.clear()
        for i in general.studentsSingle(self.lineEdit_17.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_22, list(map(str, i)))

    def handleReadTrackCourse(self):
        print("Pressed Leita (Áfangi á braut)")
        general = GeneralSP()
        self.treeWidget_36.clear()
        for i in general.trackCoursesSingle(self.lineEdit_28.text(), self.lineEdit_27.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_36, list(map(str, i)))

    def handleReadTrack(self):
        print("Pressed Leita (Braut)")
        general = GeneralSP()
        self.treeWidget_37.clear()
        for i in general.tracksSingle(self.lineEdit_29.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_37, list(map(str, i)))

    # Update handlers
    def handleUpdateCourse(self):
        print("Pressed Update (Áfangar)")
        general = GeneralSP()
        results = general.coursesUpdate(self.lineEdit_40.text(), self.lineEdit_41.text(), self.lineEdit_42.text(), self.spinBox_2.value())
        print(results)

    def handleUpdateDivision(self):
        print("Pressed Update (Greinar)")
        general = GeneralSP()
        results = general.divisionsUpdate(self.lineEdit_43.text(), self.lineEdit_45.text(), self.lineEdit_44.text())
        print(results)

    def handleUpdateRestrictor(self):
        print("Pressed Update (Takmörk)")
        general = GeneralSP()
        results = general.restrictorsUpdate(self.lineEdit_48.text(), self.lineEdit_49.text(), self.lineEdit_46.text(), self.lineEdit_47.text(), self.comboBox_19.currentText())
        print(results)

    def handleUpdateSchool(self):
        print("Pressed Update (Skólar)")
        general = GeneralSP()
        json = self.lineEdit_15.text()
        if not json: json = None
        results = general.schoolsUpdate(self.lineEdit_39.text(), self.lineEdit_38.text(), json)
        print(results)

    def handleUpdateStudentCourses(self):
        print("Pressed Update (Áfangi á nemanda)")
        general = GeneralSP()
        results = general.studentCoursesUpdate(self.lineEdit_53.text(), self.lineEdit_50.text(), self.lineEdit_37.text(), self.lineEdit_36.text(), self.lineEdit_52.text(), self.lineEdit_51.text(), self.doubleSpinBox_2.value(), self.comboBox_31.currentText(), self.comboBox_23.currentText())
        print(results)

    def handleUpdateStudent(self):
        print("Pressed Update (Nemendur)")
        general = GeneralSP()
        results = general.studentsUpdate(self.lineEdit_56.text(), self.lineEdit_54.text(), self.lineEdit_55.text(), self.lineEdit_35.text())
        print(results)

    def handleUpdateTrackCourse(self):
        print("Pressed Update (Áfangi á braut)")
        general = GeneralSP()
        results = general.trackCoursesUpdate(self.lineEdit_34.text(), self.lineEdit_33.text(), self.lineEdit_57.text(), self.lineEdit_58.text(), self.comboBox_29.currentText(), self.comboBox_27.currentText())
        print(results)

    def handleUpdateTrack(self):
        print("Pressed Update (Braut)")
        general = GeneralSP()
        results = general.tracksUpdate(self.lineEdit_60.text(), self.lineEdit_59.text(), self.dateEdit_2.date().toPyDate(), self.lineEdit_32.text())
        print(results)

    def handleUpdateClearCourses(self):
        print("Pressed Update Hreinsa (Áfangar)")
        self.spinBox_2.setEnabled(False)
        self.spinBox_2.setValue(5)
        self.lineEdit_41.setEnabled(False)
        self.lineEdit_41.clear()
        self.lineEdit_42.setEnabled(False)
        self.lineEdit_42.clear()
        self.lineEdit_40.setEnabled(True)
        self.lineEdit_40.clear()
        self.pushButton_9.setEnabled(False)
        self.pushButton_36.setEnabled(True)

    def handleUpdateClearDivision(self):
        print("Pressed Update Hreinsa (Greinar)")
        self.lineEdit_43.setEnabled(True)
        self.lineEdit_43.clear()
        self.lineEdit_44.setEnabled(False)
        self.lineEdit_44.clear()
        self.lineEdit_45.setEnabled(False)
        self.lineEdit_45.clear()
        self.pushButton_29.setEnabled(False)
        self.pushButton_37.setEnabled(True)

    def handleUpdateClearRestrictor(self):
        print("Pressed Update Hreinsa (Takmörk)")
        self.comboBox_19.setEnabled(False)
        self.comboBox_19.setCurrentIndex(0)
        self.lineEdit_46.setEnabled(False)
        self.lineEdit_46.clear()
        self.lineEdit_47.setEnabled(False)
        self.lineEdit_47.clear()
        self.lineEdit_48.setEnabled(True)
        self.lineEdit_48.clear()
        self.lineEdit_49.setEnabled(True)
        self.lineEdit_49.clear()
        self.pushButton_30.setEnabled(False)
        self.pushButton_38.setEnabled(True)

    def handleUpdateClearSchool(self):
        print("Pressed Update Hreinsa (Skólar)")
        self.lineEdit_38.clear()
        self.lineEdit_38.setEnabled(False)
        self.lineEdit_15.clear()
        # self.lineEdit_15.setEnabled(True)
        self.lineEdit_39.clear()
        self.lineEdit_39.setEnabled(True)
        self.pushButton_31.setEnabled(False)
        self.pushButton_39.setEnabled(True)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setChecked(False)

    def handleUpdateClearStudentCourses(self):
        print("Pressed Update Hreinsa (Áfangi á nemanda)")
        self.lineEdit_50.clear()
        self.lineEdit_50.setEnabled(False)
        self.comboBox_23.setCurrentIndex(0)
        self.comboBox_23.setEnabled(False)
        self.lineEdit_36.clear()
        self.lineEdit_36.setEnabled(False)
        self.doubleSpinBox_2.setValue(0)
        self.doubleSpinBox_2.setEnabled(False)
        self.lineEdit_51.clear()
        self.lineEdit_51.setEnabled(False)
        self.lineEdit_53.clear()
        self.lineEdit_53.setEnabled(True)
        self.lineEdit_37.clear()
        self.lineEdit_37.setEnabled(True)
        self.lineEdit_52.clear()
        self.lineEdit_52.setEnabled(True)
        self.comboBox_31.setCurrentIndex(0)
        self.comboBox_31.setEnabled(True)
        self.pushButton_32.setEnabled(False)
        self.pushButton_40.setEnabled(True)

    def handleUpdateClearStudent(self):
        print("Pressed Update Hreinsa (Nemendur)")
        self.lineEdit_35.clear()
        self.lineEdit_35.setEnabled(False)
        self.lineEdit_54.clear()
        self.lineEdit_54.setEnabled(False)
        self.lineEdit_55.clear()
        self.lineEdit_55.setEnabled(False)
        self.lineEdit_56.clear()
        self.lineEdit_56.setEnabled(True)
        self.pushButton_41.setEnabled(True)
        self.pushButton_33.setEnabled(False)

    def handleUpdateClearTrackCourse(self):
        print("Pressed Update Hreinsa (Áfangi á braut)")
        self.lineEdit_33.clear()
        self.lineEdit_33.setEnabled(False)
        self.lineEdit_58.clear()
        self.lineEdit_58.setEnabled(False)
        self.comboBox_27.setCurrentIndex(0)
        self.comboBox_27.setEnabled(False)
        self.comboBox_29.setCurrentIndex(0)
        self.comboBox_29.setEnabled(False)
        self.lineEdit_34.clear()
        self.lineEdit_34.setEnabled(True)
        self.lineEdit_57.clear()
        self.lineEdit_57.setEnabled(True)
        self.pushButton_42.setEnabled(True)
        self.pushButton_34.setEnabled(False)

    def handleUpdateClearTrack(self):
        print("Pressed Update Hreinsa (Braut)")
        self.lineEdit_60.clear()
        self.lineEdit_59.clear()
        self.lineEdit_59.setEnabled(False)
        self.lineEdit_32.clear()
        self.lineEdit_32.setEnabled(False)
        self.dateEdit_2.clear()
        self.dateEdit_2.setEnabled(False)
        self.pushButton_43.setEnabled(True)
        self.pushButton_35.setEnabled(False)

    def handleUpdateSearchCourse(self):
        print("Pressed Update Leit (Áfangar)")
        general = GeneralSP()
        if not general.coursesSingle(self.lineEdit_40.text()): return
        self.spinBox_2.setEnabled(True)
        self.lineEdit_40.setEnabled(False)
        self.lineEdit_41.setEnabled(True)
        self.lineEdit_42.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_36.setEnabled(False)

    def handleUpdateSearchDivision(self):
        print("Pressed Update Leit (Greinar)")
        general = GeneralSP()
        if not general.divisionsSingle(self.lineEdit_43.text()): return
        self.lineEdit_43.setEnabled(False)
        self.lineEdit_44.setEnabled(True)
        self.lineEdit_45.setEnabled(True)
        self.pushButton_29.setEnabled(True)
        self.pushButton_37.setEnabled(False)

    def handleUpdateSearchRestrictor(self):
        print("Pressed Update Leit (Takmörk)")
        general = GeneralSP()
        if not general.restrictorsSingle(self.lineEdit_48.text(), self.lineEdit_49.text()): return
        self.comboBox_19.setEnabled(True)
        self.lineEdit_46.setEnabled(True)
        self.lineEdit_47.setEnabled(True)
        self.lineEdit_48.setEnabled(False)
        self.lineEdit_49.setEnabled(False)
        self.pushButton_30.setEnabled(True)
        self.pushButton_38.setEnabled(False)

    def handleUpdateSearchSchool(self):
        print("Pressed Update Leit (Skólar)")
        general = GeneralSP()
        if not general.schoolsSingle(self.lineEdit_39.text()): return
        self.lineEdit_38.setEnabled(True)
        self.lineEdit_39.setEnabled(False)
        self.checkBox_2.setEnabled(True)
        self.pushButton_31.setEnabled(True)
        self.pushButton_39.setEnabled(False)

    def handleUpdateSearchStudentCourses(self):
        print("Pressed Update Leit (Áfangi á nemanda)")
        general = GeneralSP()
        if not general.studentCoursesSingle(self.lineEdit_53.text(), self.lineEdit_37.text(), self.lineEdit_52.text(), self.comboBox_31.currentText()): return
        self.lineEdit_50.setEnabled(True)
        self.comboBox_23.setEnabled(True)
        self.lineEdit_36.setEnabled(True)
        self.doubleSpinBox_2.setEnabled(True)
        self.lineEdit_51.setEnabled(True)
        self.lineEdit_53.setEnabled(False)
        self.lineEdit_37.setEnabled(False)
        self.lineEdit_52.setEnabled(False)
        self.comboBox_31.setEnabled(False)
        self.pushButton_32.setEnabled(True)
        self.pushButton_40.setEnabled(False)

    def handleUpdateSearchStudent(self):
        print("Pressed Update Leit (Nemendur)")
        general = GeneralSP()
        if not general.studentsSingle(self.lineEdit_56.text()): return
        self.lineEdit_56.setEnabled(False)
        self.pushButton_41.setEnabled(False)
        self.pushButton_33.setEnabled(True)
        self.lineEdit_35.setEnabled(True)
        self.lineEdit_54.setEnabled(True)
        self.lineEdit_55.setEnabled(True)

    def handleUpdateSearchTrackCourse(self):
        print("Pressed Update Leit (Áfangi á braut)")
        general = GeneralSP()
        if not general.trackCoursesSingle(self.lineEdit_34.text(), self.lineEdit_57.text()): return
        self.lineEdit_33.setEnabled(True)
        self.lineEdit_58.setEnabled(True)
        self.comboBox_27.setEnabled(True)
        self.comboBox_29.setEnabled(True)
        self.lineEdit_34.setEnabled(False)
        self.lineEdit_57.setEnabled(False)
        self.pushButton_42.setEnabled(False)
        self.pushButton_34.setEnabled(True)

    def handleUpdateSearchTrack(self):
        print("Pressed Update Leit (Braut)")
        general = GeneralSP()
        if not general.tracksSingle(self.lineEdit_60.text()): return
        self.lineEdit_59.setEnabled(True)
        self.lineEdit_32.setEnabled(True)
        self.dateEdit_2.setEnabled(True)
        self.lineEdit_60.setEnabled(False)
        self.pushButton_43.setEnabled(False)
        self.pushButton_35.setEnabled(True)

    def handleDeleteCourse(self):
        print("Pressed Delete (Áfangi)")
        general = GeneralSP()
        general.coursesDelete(self.lineEdit_61.text())

    def handleDeleteDivisions(self):
        print("Pressed Delete (Grein)")
        general = GeneralSP()
        general.divisionsDelete(self.lineEdit_62.text())

    def handleDeleteRestrictors(self):
        print("Pressed Delete (Takmarka)")
        general = GeneralSP()
        general.restrictorsDelete(self.lineEdit_69.text(), self.lineEdit_63.text())

    def handleDeleteSchools(self):
        print("Pressed Delete (Skóli)")
        general = GeneralSP()
        general.schoolsDelete(self.lineEdit_64.text())

    def handleDeleteStudentCourses(self):
        print("Pressed Delete (Áfangi á nemanda)")
        general = GeneralSP()
        general.studentCoursesDelete(self.lineEdit_71.text(), self.lineEdit_65.text(), self.lineEdit_70.text(), self.comboBox_32.currentText())

    def handleDeleteStudents(self):
        print("Pressed Delete (Nemandi)")
        general = GeneralSP()
        general.studentsDelete(self.lineEdit_66.text())

    def handleDeleteTrackCourses(self):
        print("Pressed Delete (Áfangi á braut)")
        general = GeneralSP()
        general.trackCoursesDelete(self.lineEdit_67.text(), self.lineEdit_72.text())

    def handleDeleteTracks(self):
        print("Pressed Delete (Braut)")
        general = GeneralSP()
        general.tracksDelete(self.lineEdit_68.text())

    def handleDeleteClearCourse(self):
        print("Pressed Delete Hreinsa (Áfanga)")
        self.lineEdit_61.clear()
        self.lineEdit_61.setEnabled(True)
        self.pushButton_53.setEnabled(True)
        self.pushButton_15.setEnabled(False)
        self.treeWidget_39.clear()

    def handleDeleteClearDivisions(self):
        print("Pressed Delete Hreinsa (Grein)")
        self.lineEdit_62.clear()
        self.lineEdit_62.setEnabled(True)
        self.pushButton_55.setEnabled(True)
        self.pushButton_16.setEnabled(False)
        self.treeWidget_40.clear()

    def handleDeleteClearRestrictors(self):
        print("Pressed Delete Hreinsa (Takmörk)")
        self.lineEdit_69.clear()
        self.lineEdit_63.clear()
        self.lineEdit_69.setEnabled(True)
        self.lineEdit_63.setEnabled(True)
        self.pushButton_57.setEnabled(True)
        self.pushButton_17.setEnabled(False)
        self.treeWidget_41.clear()

    def handleDeleteClearSchools(self):
        print("Pressed Delete Hreinsa (Skóli)")
        self.lineEdit_64.clear()
        self.lineEdit_64.setEnabled(True)
        self.pushButton_59.setEnabled(True)
        self.pushButton_18.setEnabled(False)
        self.treeWidget_42.clear()

    def handleDeleteClearStudentCourses(self):
        print("Pressed Delete Hreinsa (Áfangi á nemanda)")
        self.lineEdit_71.clear()
        self.lineEdit_65.clear()
        self.lineEdit_70.clear()
        self.comboBox_32.setCurrentIndex(0)
        self.lineEdit_71.setEnabled(True)
        self.lineEdit_65.setEnabled(True)
        self.lineEdit_70.setEnabled(True)
        self.comboBox_32.setEnabled(True)
        self.pushButton_61.setEnabled(True)
        self.pushButton_19.setEnabled(False)
        self.treeWidget_43.clear()

    def handleDeleteClearStudents(self):
        print("Pressed Delete Hreinsa (Nemanda)")
        self.lineEdit_66.clear()
        self.lineEdit_66.setEnabled(True)
        self.pushButton_63.setEnabled(True)
        self.pushButton_21.setEnabled(False)
        self.treeWidget_44.clear()

    def handleDeleteClearTrackCourses(self):
        print("Pressed Delete Hreinsa (Áfangi á braut)")
        self.lineEdit_67.clear()
        self.lineEdit_72.clear()
        self.lineEdit_67.setEnabled(True)
        self.lineEdit_72.setEnabled(True)
        self.pushButton_65.setEnabled(True)
        self.pushButton_22.setEnabled(False)
        self.treeWidget_45.clear()

    def handleDeleteClearTracks(self):
        print("Pressed Delete Hreinsa (Braut)")
        self.lineEdit_68.clear()
        self.lineEdit_68.setEnabled(True)
        self.pushButton_67.setEnabled(True)
        self.pushButton_23.setEnabled(False)
        self.treeWidget_46.clear()

    def handleDeleteSearchCourse(self):
        print("Pressed Delete Leita (Áfanga)")
        general = GeneralSP()
        if not general.coursesSingle(self.lineEdit_61.text()): return
        self.lineEdit_61.setEnabled(False)
        self.pushButton_15.setEnabled(True)
        self.pushButton_53.setEnabled(False)
        print(self.lineEdit_61.text())
        self.treeWidget_39.clear()
        for i in general.coursesSingle(self.lineEdit_61.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_39, list(map(str, i)))


    def handleDeleteSearchDivisions(self):
        print("Pressed Delete Leita (Grein)")
        general = GeneralSP()
        if not general.divisionsSingle(self.lineEdit_62.text()): return
        self.lineEdit_62.setEnabled(False)
        self.pushButton_16.setEnabled(True)
        self.pushButton_55.setEnabled(False)
        for i in general.divisionsSingle(self.lineEdit_62.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_40, list(map(str, i)))

    def handleDeleteSearchRestrictors(self):
        print("Pressed Delete Leita (Takmörk)")
        general = GeneralSP()
        if not general.restrictorsSingle(self.lineEdit_69.text(), self.lineEdit_63.text()): return
        self.lineEdit_69.setEnabled(False)
        self.lineEdit_63.setEnabled(False)
        self.pushButton_17.setEnabled(True)
        self.pushButton_57.setEnabled(False)
        for i in general.restrictorsSingle(self.lineEdit_69.text(), self.lineEdit_63.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_41, list(map(str, i)))

    def handleDeleteSearchSchools(self):
        print("Pressed Delete Leita (Skóli)")
        general = GeneralSP()
        if not general.schoolsSingle(self.lineEdit_64.text()): return
        self.lineEdit_64.setEnabled(False)
        self.pushButton_18.setEnabled(True)
        self.pushButton_59.setEnabled(False)
        for i in general.schoolsSingle(self.lineEdit_64.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_42, list(map(str, i)))

    def handleDeleteSearchStudentCourses(self):
        print("Pressed Delete Leita (Áfangi á nemanda)")
        general = GeneralSP()
        if not general.studentCoursesSingle(self.lineEdit_71.text(), self.lineEdit_65.text(), self.lineEdit_70.text(), self.comboBox_32.currentText()): return
        self.lineEdit_71.setEnabled(False)
        self.lineEdit_65.setEnabled(False)
        self.lineEdit_70.setEnabled(False)
        self.comboBox_32.setEnabled(False)
        self.pushButton_19.setEnabled(True)
        self.pushButton_61.setEnabled(False)
        for i in general.studentCoursesSingle(self.lineEdit_71.text(), self.lineEdit_65.text(), self.lineEdit_70.text(), self.comboBox_32.currentText()): QtWidgets.QTreeWidgetItem(self.treeWidget_43, list(map(str, i)))

    def handleDeleteSearchStudents(self):
        print("Pressed Delete Leita (Nemanda)")
        general = GeneralSP()
        if not general.studentsSingle(self.lineEdit_66.text()): return
        self.lineEdit_66.setEnabled(False)
        self.pushButton_21.setEnabled(True)
        self.pushButton_63.setEnabled(False)
        for i in general.studentsSingle(self.lineEdit_66.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_44, list(map(str, i)))

    def handleDeleteSearchTrackCourses(self):
        print("Pressed Delete Leita (Áfangi á braut)")
        general = GeneralSP()
        if not general.trackCoursesSingle(self.lineEdit_67.text(), self.lineEdit_72.text()): return
        self.lineEdit_67.setEnabled(False)
        self.lineEdit_72.setEnabled(False)
        self.pushButton_22.setEnabled(True)
        self.pushButton_65.setEnabled(False)
        for i in general.trackCoursesSingle(self.lineEdit_67.text(), self.lineEdit_72.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_45, list(map(str, i)))

    def handleDeleteSearchTracks(self):
        print("Pressed Delete Leita (Braut)")
        general = GeneralSP()
        if not general.tracksSingle(self.lineEdit_68.text()): return
        self.lineEdit_68.setEnabled(False)
        self.pushButton_23.setEnabled(True)
        self.pushButton_67.setEnabled(False)
        for i in general.tracksSingle(self.lineEdit_68.text()): QtWidgets.QTreeWidgetItem(self.treeWidget_46, list(map(str, i)))

    # Custom functions

    def handleExtraValBtn(self): # SELECT NEXT COURSES
        customFunc = CustomF()
        print("Clicked Extra Val")
        print(customFunc.selectNextCourses())
        # return customFunc.selectNextCourses()

    def handleExtraValSearchStud(self):
        print("Clicked Extra Val leit Search Student")

        general = GeneralSP()
        if not general.studentsSingle(self.lineEdit_75.text()): return
        self.lineEdit_73.setEnabled(True)
        self.comboBox_15.setEnabled(True)
        self.pushButton_68.setEnabled(True)
        self.lineEdit_75.setEnabled(False)
        self.pushButton_70.setEnabled(False)

        semestersComboBox = set()
        for i in general.studentCoursesList():
            if str(i[0]) == self.lineEdit_75.text():
                semestersComboBox.add(i[4])

        self.comboBox_15.clear()
        self.comboBox_15.addItem("Allar annir")
        self.comboBox_15.addItems(semestersComboBox)

    def handleExtraValClear(self):
        print("Clicked Extra Val leit Clear")

        self.lineEdit_75.setEnabled(True)
        self.lineEdit_75.clear()
        self.lineEdit_73.setEnabled(False)
        self.lineEdit_73.clear()
        self.comboBox_15.setEnabled(False)
        self.comboBox_15.setCurrentIndex(0)
        self.pushButton_68.setEnabled(False)
        self.pushButton_70.setEnabled(True)
        self.treeWidget_11.clear()

    def handleExtraValSearchStudentCourses(self):
        print("Clicked Extra Val leit Search StudentCourses")
        general = GeneralSP()
        allClasses = general.studentCoursesList()

        if self.comboBox_15.currentText() == "Allar annir":
            if self.lineEdit_73.text():
                print("Allar annir & Braut ID")
                semClasses = [i for i in allClasses if str(i[0]) == self.lineEdit_75.text() and str(i[1]) == self.lineEdit_73.text()]
            else:
                print("Allar annir")
                semClasses = [i for i in allClasses if str(i[0]) == self.lineEdit_75.text()]
        else:
            if self.lineEdit_73.text():
                print("Ákveðin önn & Braut ID")
                semClasses = [i for i in allClasses if str(i[0]) == self.lineEdit_75.text() and i[4] == self.comboBox_15.currentText() and str(i[1]) == self.lineEdit_73.text()]
            else:
                print("Ákveðin önn")
                semClasses = [i for i in allClasses if str(i[0]) == self.lineEdit_75.text() and i[4] == self.comboBox_15.currentText()]

        print("Nemanda ID: {}".format(self.lineEdit_75.text()))
        print("Braut ID: {}".format(self.lineEdit_73.text()))
        print("Önn: {}".format(self.comboBox_15.currentText()))
        print("Niðurstaða: {}".format(semClasses))
        print()

        self.treeWidget_11.clear()
        for i in semClasses: QtWidgets.QTreeWidgetItem(self.treeWidget_11, list(map(str, i)))

    def handleExtraValNextSemSearchStud(self):
        print("Pressed Extra Val Search")

        general = GeneralSP()
        if not general.studentsSingle(self.lineEdit_76.text()): return
        self.lineEdit_74.setEnabled(True)
        self.comboBox_16.setEnabled(True)
        self.pushButton_73.setEnabled(True)
        self.lineEdit_76.setEnabled(False)
        self.pushButton_71.setEnabled(False)

    def handleExtraValNextSemClear(self):
        print("Pressed Extra Val Clear")

        self.lineEdit_76.setEnabled(True)
        self.lineEdit_76.clear()
        self.lineEdit_74.setEnabled(False)
        self.lineEdit_74.clear()
        self.comboBox_16.setEnabled(False)
        self.pushButton_73.setEnabled(False)
        self.pushButton_71.setEnabled(True)
        self.treeWidget_12.clear()

    def handleExtraValNextSemSearchNextSem(self):
        print("Pressed Extra Val NextSem")

        custom = CustomSP()
        print("StudentID: {}".format(self.lineEdit_76.text()))
        print("TrackID: {}".format(self.lineEdit_74.text()))
        print("CurrentSem: {}".format(self.comboBox_16.currentText()))
        print("NextSem: {}".format(getNextSemester(self.comboBox_16.currentText())))

        self.treeWidget_12.clear()
        for i in custom.getNextClasses(self.lineEdit_76.text(), self.lineEdit_74.text(), self.comboBox_16.currentText()): QtWidgets.QTreeWidgetItem(self.treeWidget_12, list(map(str, i)))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
