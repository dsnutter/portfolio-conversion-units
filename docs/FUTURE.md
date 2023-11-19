Ideas for the Future

* get the program fully working as a python module executable
* integrate a relational db as module with the data layer already written. SQLite may be appropriate for a command line program, could use a library like SQLAlchemy so that the project is not dependent on one type of SQL db
    * we could also do graph and statistics more easily if it was relational db based
* graphs and statistics could be built with numpy / pandas with dataframe integration
    * maybe store response data in dataframe instead of the dictionary structure currently using
* jinja2 templates for HTML output that the teacher could more easily modify
    * could I do this with LaTex also, which would be a really nice formatted PDF?
    * open HTML generated automagically in firefox/chrome
* export data to a file the teach can use
* offer command line argument CSV import/export by the teacher so the teacher can integrate with excel or any other possible grading system they may use
    * My opinion is that excel is a better UI interface for data entry than the interactive console UI I built for the teacher since the teachers have command line experience and can run commands from a console. It would definately be faster, and the grade of the question could be determined after import
* Implement the rest of the CRUD operations for repsonses. All I have right now is add/create. Would need update/delete
    * Would have to implement in the UI also
    * have all CRUD methods accept an list or dict of lists instead of one item so can operate CRUD for all records passed
* Tool for the teachers to enter the conversions along with the equations to use
* For the equations, add some operations from the math library, so math and sciences teachers in higher grades could use the software

