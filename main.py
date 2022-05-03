import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

# CREATE (Crud)
# this function takes in a request body of JSON
# it then creates a record in the database using the elements of that JSON payload
# it then returns success
@app.route('/employees', methods=['POST'])
def create_employees():
    try:        
        _json = request.json
        _firstName = _json['firstName']
        _lastName = _json['lastName']
        _extension = _json['extension']
        _email = _json['email']	
        _officeCode = int(_json['officeCode'])	
        _reportsTo = int(_json['reportsTo'])
        _jobTitle = _json['jobTitle']	
        
        if _json:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)	

            # construct the SQL query
            sqlQuery = "INSERT INTO employees(firstName, lastName, extension, email, officeCode, reportsTo, jobTitle) VALUES(%s, %s, %s, %s, %s, %s, %s)"            
            bindData = (_firstName, _lastName, _extension, _email, _officeCode, _reportsTo, _jobTitle)
            cursor.execute(sqlQuery, bindData)
            
            # commit the sql transaction
            conn.commit()
            
            # response to send
            respone = jsonify('employee added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()          

# READ (cRud)
# this function uses the route /employees to get all employees
@app.route('/employees')
def employees():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select employeeNumber, firstName, lastName, extension, email, officeCode, reportsTo, jobTitle FROM employees")
        employeesRows = cursor.fetchall()
        respone = jsonify(employeesRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

# READ (cRud)
# this function uses the route /employees/<employeeId> to get a specific employee
@app.route('/employees/<employees_id>')
def employees_details(employees_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select employeeNumber, firstName, lastName, extension, email, officeCode, reportsTo, jobTitle FROM employees WHERE employeeNumber =%s", employees_id)
        employeesRow = cursor.fetchone()
        respone = jsonify(employeesRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

# Update (crUd)
# this function uses the route /employees/<employeeId> to update a specific employee
@app.route('/employees/<employee_id>', methods=['PUT'])
def update_employees(employee_id):
    try:
        _json = request.json
        _firstName = _json['firstName']
        _lastName = _json['lastName']
        _extension = _json['extension']
        _email = _json['email']	
        _officeCode = int(_json['officeCode'])	
        _reportsTo = int(_json['reportsTo'])
        _jobTitle = _json['jobTitle']	
        
        if _json:			
            sqlQuery = "UPDATE employees SET firstName=%s, lastName=%s, extension=%s, email=%s, officeCode=%s, reportsTo=%s, jobTitle=%s WHERE employeeNumber=%s"
            bindData = (_firstName, _lastName, _extension, _email, _officeCode, _reportsTo, _jobTitle, employee_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('employee updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/employees/<employee_id>', methods=['DELETE'])
def delete_employees(employee_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM employees WHERE employeeNumber =%s", (employee_id,))
		conn.commit()
		respone = jsonify('employees deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
        
# this method handles a 404 error returned from this service 
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run()