from subprocess import call
call("rm -rf app.db")
call("rm -rf db_repository/")
call("./db_create.py")
call("./db_migrate.py")
