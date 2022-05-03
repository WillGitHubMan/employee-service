ALTER TABLE employees AUTO_INCREMENT=2000;

ALTER TABLE customers DROP FOREIGN KEY customers_ibfk_1;
ALTER TABLE employees DROP FOREIGN KEY employees_ibfk_1;

ALTER TABLE employees modify employeeNumber INT NOT NULL AUTO_INCREMENT;

ALTER TABLE customers ADD CONSTRAINT customers_ibfk_1 FOREIGN KEY (`salesRepEmployeeNumber`) REFERENCES `employees` (`employeeNumber`);
ALTER TABLE employees ADD CONSTRAINT employees_ibfk_1 FOREIGN KEY (`reportsTo`) REFERENCES `employees` (`employeeNumber`);