-- 2.1
SELECT * FROM tokens 
WHERE expires > NOW();

-- 2.2
SELECT * FROM tokens 
ORDER BY created DESC LIMIT 100;

-- 2.3
SELECT * FROM tokens 
WHERE application_id = 1001
ORDER BY created DESC LIMIT 5;

-- 2.4
SELECT u.first_name FROM user u
INNER JOIN tokens t ON u.user_id = t.user_id
WHERE t.token = 'x';

-- 2.5
SELECT u.first_name FROM user u
INNER JOIN tokens t ON u.user_id = t.user_id
WHERE t.created >= NOW() - INTERVAL 1 DAY
GROUP BY u.user_id HAVING COUNT(t.id) >= 3;