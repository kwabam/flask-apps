drop table if exists Assignments;
CREATE TABLE Assignments(
    AID varchar(50) PRIMARY KEY,
    weight float,
    description varchar(255),
    dueDate date,
    assignedDate date,
    title varchar(50)
);

drop table if exists Professors;
CREATE Table Professors(
	ProfessorRNumber serial PRIMARY KEY,
	Name varchar(50),
	OfficeHoursBegin time,
	OfficeHoursEnd time,
	OfficeNumber integer,
	Email varchar(50),
	Password varchar(255)
);

drop table if exists Students;
CREATE TABLE Students(
	StudentRNumber serial PRIMARY KEY,
	Name varchar(50), 
	Email varchar(50),
	Password varchar(255)
);

drop table if exists Grades;
CREATE TABLE Grades(
	Points float,
	MaxPoints float,
	Category varchar(50),
	AssignmentID serial REFERENCES Assignments(AssignmentID),
	StudentRNumber serial REFERENCES Students(StudentRNumber),
	PRIMARY KEY(Points, MaxPoints, AssignmentID, StudentRNumber)
);

drop table if exists Courses;
CREATE TABLE Courses(
	CRN serial PRIMARY KEY,
	RoomNumber int,
	Name varchar(50),
	SyllabusLink varchar(255),
	CoursePageLink varchar(255),
	Days integer [],
	startTime time,
	endTime time
);

drop table if exists Lecture;
CREATE TABLE Lecture(
	LectureDate date,
	Description varchar(255),
	Topic varchar(50),
	Type varchar(50),
	MaterialsLink varchar(255),
	CRN serial REFERENCES Courses(CRN),
	PRIMARY KEY(LectureDate, CRN)
);

