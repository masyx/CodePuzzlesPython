CREATE TABLE transactions(
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    shares_qty INTEGER NOT NULL,
    share_name TEXT NOT NULL,
    share_symbol TEXT NOT NULL,
    share_price NUMERIC NOT NULL,
    transaction_date TEXT NOT NULL UNIQUE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id ) REFERENCES users(id)
);



INSERT INTO transactions(user_id, shares_qty, share_price, transaction_date)
VALUES (1, 888, 999.99, "2021-10-26 16:05:49.803045")


UPDATE users
SET cash =
WHERE id = ;


SELECT *
FROM users
JOIN transactions ON users.id = transactions.user_id


SELECT share_symbol, share_name, shares_qty, share_price
FROM transactions WHERE user_id = 1;

SELECT cash FROM users WHERE id = ;




#######
SELECT DISTINCT share_symbol FROM transactions