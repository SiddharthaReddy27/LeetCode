# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (
    SELECT MAX(salary)
    FROM Employee
);














#SELECT DISTINCT MAX(e.salary) as SecondHighestSalary
#FROM Employee e
#JOIN Employee e1
#   ON e.id = e1.id 
#WHERE e.salary BETWEEN 1 AND 3
