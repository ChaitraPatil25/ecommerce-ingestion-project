
-- Top customers by spending
SELECT customer_name, SUM(amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id=o.customer_id
JOIN payments p ON o.order_id=p.order_id
GROUP BY c.customer_id
ORDER BY total_spent DESC;
