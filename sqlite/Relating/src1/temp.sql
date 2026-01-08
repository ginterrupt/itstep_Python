SELECT "book_id", ROUND(AVG("rating"), 2) AS "average rating" FROM "ratings"
GROUP BY "book_id";