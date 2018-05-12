from django.conf import settings
from django.db.models.query import QuerySet, GET_ITERATOR_CHUNK_SIZE, EmptyResultSet
from django.db.models.manager import Manager
from django.db.models import Model
from django.db import connections, connection, transaction

__all__ = ['StoredProcedureManager']

class PreparedStatementError(Exception):
    pass

class InvalidSQLProcedure(PreparedStatementError):
    pass

class StoredProcedureManager(Manager):
    database = ""
    prepared_command = ""
    name = "StoredProcedure"

    def __init__(self, database):
        if database == "":
            if 'mysql' in settings.DATABASE_ENGINE.lower():
                self.prepared_command = 'CALL'
            else:
                self.prepared_command = 'SELECT * FROM'
        else:
            if not database in settings.DATABASES:
                raise ValueError('Database not found in settings')

            if 'mysql' in settings.DATABASES[database]['ENGINE']:
                self.prepared_command = 'CALL'
            elif 'mssql' in settings.DATABASES[database]['ENGINE']:
                self.prepared_command = 'EXEC'

            self.database = database


    """ ``ProcedureManager`` allows Django Models to easily call
    procedures from the database. This manager exposes two
    additional functions to ``Model.objects``::

      - ``values_from_procedure``: Returns a list of tuples that were
                                   returned from the call.

      - ``filter_by_procedure``: Returns a ``QuerySetPrepared`` that represents
                                 the list of objects returned by that procedure.

    USAGE
    =====

    To use, simply add the objects statement in your model. For example::

        class Article(models.Model):
            objects = ProcedureManager()

    Then just call it like any filter::

        Article.objects.filter_by_procedure('articles_with_author', request.user)
    """
    def exec_sp(self, proc_name, *proc_params):
        """ Return whatever a result of a procedure is.

        The proc_name is the name of a stored procedure or function.

        This will return a list of dictionaries representing the
        rows and columns of the result.
        """
        new_params = None

        if proc_params and isinstance(proc_params[0], list):
                new_params = proc_params[0]
        else:
            new_params = [clean_param(param) for param in proc_params]
        

        cursor = None
        retVal = 0

        if not self.database == "":
            cursor = connections[self.database].cursor()
            retVal = cursor.execute("%s %s(%s)" % (self.prepared_command,
                                        proc_name,
                                        ', '.join('%s' for x in new_params)),
                        new_params)
        else:
            cursor = connection.cursor()
            retVal = cursor.execute("%s %s(%s)" % (self.prepared_command,
                                        proc_name,
                                        ', '.join('%s' for x in new_params)),
                        new_params)

        connections[self.database].close()
        return retVal

    def exec_sp_tosingle(self, proc_name, *proc_params):
        """ Return whatever a result of a procedure is.

        The proc_name is the name of a stored procedure or function.

        This will return a list of dictionaries representing the
        rows and columns of the result.
        """
        new_params = None

        if proc_params and isinstance(proc_params[0], list):
                new_params = proc_params[0]
        else:
            new_params = [clean_param(param) for param in proc_params]
        
        cursor = None

        if not self.database == "":
            cursor = connections[self.database].cursor()
            cursor.execute("%s %s(%s)" % (self.prepared_command,
                                        proc_name,
                                        ', '.join('%s' for x in new_params)),
                        new_params)
        else:
            cursor = connection.cursor()
            cursor.execute("%s %s(%s)" % (self.prepared_command,
                                        proc_name,
                                        ', '.join('%s' for x in new_params)),
                        new_params)

        retVal = cursor.fetchone()

        connections[self.database].close()
        return retVal

    def exec_sp_tolist(self, proc_name, *proc_params):
        """ Return whatever a result of a procedure is.

        The proc_name is the name of a stored procedure or function.

        This will return a list of dictionaries representing the
        rows and columns of the result.
        """
        new_params = None

        if proc_params and isinstance(proc_params[0], list):
                new_params = proc_params[0]
        else:
            new_params = [clean_param(param) for param in proc_params]

        cursor = None

        if not self.database == "":
            cursor = connections[self.database].cursor()
            cursor.execute("%s %s(%s)" % (self.prepared_command,
                                        proc_name,
                                        ', '.join('%s' for x in new_params)),
                        new_params)
        else:
            cursor = connection.cursor()
            cursor.execute("%s %s(%s)" % (self.prepared_command,
                                        proc_name,
                                        ', '.join('%s' for x in new_params)),
                        new_params)

        retVal = cursor.fetchall()

        connections[self.database].close()
        return retVal

    def exec_sp_todict(self, proc_name, *proc_params):
        """ Return whatever a result of a procedure is.

        The proc_name is the name of a stored procedure or function.

        This will return a list of dictionaries representing the
        rows and columns of the result.
        """
        new_params = None

        if proc_params and isinstance(proc_params[0], list):
                new_params = proc_params[0]
        else:
            new_params = [clean_param(param) for param in proc_params]

        cursor = None

        if not self.database == "":
            cursor = connections[self.database].cursor()
            cursor.execute("%s %s(%s)" % (self.prepared_command,
                                        proc_name,
                                        ', '.join('%s' for x in new_params)),
                        new_params)
        else:
            cursor = connection.cursor()
            cursor.execute("%s %s(%s)" % (self.prepared_command,
                                        proc_name,
                                        ', '.join('%s' for x in new_params)),
                        new_params)

        rows = cursor.dictfetchmany(GET_ITERATOR_CHUNK_SIZE)

        retVal = []

        while rows:
            for row in rows:
                retVal.append(row)
            rows = cursor.dictfetchmany(GET_ITERATOR_CHUNK_SIZE)

        return retVal


def clean_param(param):
    if hasattr(param, '_get_pk_val'):
        # has a pk value -- must be a model
        return str(param._get_pk_val())
    
    if callable(param):
        # it's callable, should call it.
        return str(param())

    return str(param)