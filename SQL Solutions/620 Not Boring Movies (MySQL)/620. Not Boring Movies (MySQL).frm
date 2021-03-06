# Write your MySQL query statement below
Select * from cinema 
Where description!='boring' 
AND (id%2)>0 
ORDER BY rating DESC
