SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM Employee AS E
JOIN Department AS D
ON E.departmentId = D.id
WHERE E.salary = (
  SELECT MAX(salary)
  FROM Employee as E1
  WHERE E1.departmentId = E.departmentId
)
