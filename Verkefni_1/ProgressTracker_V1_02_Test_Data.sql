insert into Schools(schoolName) values('Tækniskólinn');

insert into Divisions(divisionName,schoolID)values('Byggingatækniskólinn',1);
insert into Divisions(divisionName,schoolID)values('Endurmenntunarskólinn',1);
insert into Divisions(divisionName,schoolID)values('Flugskóli Íslands',1);
insert into Divisions(divisionName,schoolID)values('Handverksskólinn',1);
insert into Divisions(divisionName,schoolID)values('Margmiðlunarskólinn',1);
insert into Divisions(divisionName,schoolID)values('Meistaraskólinn',1);
insert into Divisions(divisionName,schoolID)values('Raftækniskólinn',1);
insert into Divisions(divisionName,schoolID)values('Skipstjórnarskólinn',1);
insert into Divisions(divisionName,schoolID)values('Tækniakademían',1);
insert into Divisions(divisionName,schoolID)values('Tæknimenntaskólinn',1);
insert into Divisions(divisionName,schoolID)values('Upplýsingatækniskólinn',1);
insert into Divisions(divisionName,schoolID)values('Vefskólinn',1);
insert into Divisions(divisionName,schoolID)values('Véltækniskólinn',1);

insert into Tracks(trackName,divisionID)values('Almennt nám Upplýsingatækniskóla - AN UTN',10);
insert into Tracks(trackName,divisionID)values('Bókband',10);
insert into Tracks(trackName,divisionID)values('Grafísk miðlun',10);
insert into Tracks(trackName,divisionID)values('Grunnnám upplýsinga- og fjölmiðlagreina',10);
insert into Tracks(trackName,divisionID)values('K2 Tækni- og vísindaleiðin',10);
insert into Tracks(trackName,divisionID)values('Ljósmyndun',10);
insert into Tracks(trackName,divisionID)values('Prentun',10);
insert into Tracks(trackName,divisionID)values('Stúdentspróf',10);
insert into Tracks(trackName,validFrom,divisionID)values('Tölvubraut TBR16 - stúdentsbraut','2016-08-01',10);

insert into Courses(courseNumber,courseName,courseCredits)
values('GSF2A3U','Gagnasafnsfræði I',3),
	  ('GSF2B3U','Gagnasafnsfræði II',3),
	  ('GSF3A3U','Gagnanotkun',3),
	  ('GSF3B3U','Gagnagreining',3);
insert into Courses(courseNumber,courseName,courseCredits)
values('FOR3G3U','Inngangur að leikjaforritun',3),
	  ('FOR3L3U','Leikjaforritun',3),
	  ('FOR3D3U','3D leikjaforritun',3);
insert into Courses(courseNumber,courseName,courseCredits)
values('STÆ103','Inngangur að stærðfræði',3),
	  ('STÆ203','Algebra',3),
	  ('STÆ303','Rúmfræði',3),
      ('STÆ313','Tölfræði',3),
      ('STÆ403','Vektorar',3),
      ('STÆ503','Diffrun og Heildun',3),
      ('STÆ603','Stærðfræðigreining',3);
insert into Courses(courseNumber,courseName,courseCredits)
values('EÐL103','Eðlisfræði I',3), 
	  ('EÐL203','Eðlisfræði II',3),
	  ('EÐL303','Eðlisfræði III',3),
	  ('EÐL403','Eðlisfræði IV',3);

insert into Restrictors(courseNumber,restrictorID,restrictorType)values('GSF2B3U','GSF2A3U',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('GSF3A3U','GSF2B3U',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('GSF3A3U','GSF3B3U',2);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('GSF3B3U','GSF3A3U',3);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ203','STÆ103',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ303','STÆ203',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ303','STÆ313',2);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ313','STÆ203',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ403','STÆ303',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ503','STÆ403',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ603','STÆ503',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('EÐL103','STÆ103',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('EÐL203','EÐL103',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('EÐL303','EÐL203',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('EÐL403','EÐL303',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('FOR3G3U','STÆ403',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('FOR3L3U','FOR3G3U',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('FOR3L3U','EÐL203',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('FOR3L3U','FOR3D3U',2);





