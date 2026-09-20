SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5
);




#SELECT m.name
#FROM Employee m
#JOIN Employee e
#    ON m.id = e.managerId
#GROUP BY m.id, m.name
#HAVING COUNT(e.id) >= 5;    