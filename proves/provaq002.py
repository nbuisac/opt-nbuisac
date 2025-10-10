select last_name, 
       CONCAT(lower(LEFT(LAST_NAME, 1)), UPPER(SUBSTRING(LAST_NAME, 2)))
from employees;