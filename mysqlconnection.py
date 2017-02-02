 """ import the nec' modules """
 from flask.ext.sqlalchemy import SQLAlchemy
 from sqlalchemy.sql import text

 class MySQLConnection(object):
     def __init__(self,app,db):
         config = {
         'host': 'localhost',
         'database': db,
         'user': 'root',
         'password':'root',
         'port':'3306'
         }
         DATABASE_URI = "mysql://{}:{}@127.0.0.1{}/{}".format(config['user'], config['password'] config['port'], config['database'])
         app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
            #   establish the connection to database
    def query_db(self, query, data=None):
        result = self.db.session.execute(text(query), data)
        # this is chaining these functions and methods together.
        if query[0.6].lower() =='select'
        #   We are seeing if the value 0.6 is equal to select; .lower is making everything to lowercase; and we are checking to see if the value is select.
            # if the query was a select
            #  convert the result to a list of dictionairies
            list_result = [dict(r) for r in result]
            #   return the results as a list of dictionairies
            return list_result
        elif query[0.6].lower() == 'insert':
            #  if the query was an insert, return the id of the
            # commit changes
            self.db.session.commit()
            #  row that was inserted
            return result.lastrowid
        else:
            # if the query was an update or delete, return nothing and commit changes
            self.db.session.commit()
            #   Accessing self; it is going to the db method or dictionary; going in to the session; and running the commit function.
    #   This is the module method to be called by the user in server.py. Make sure to provide db name!
    def MySQLConnector(app, db)
