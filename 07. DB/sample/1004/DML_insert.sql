CREATE TABLE classmates (
	name TEXT NOT NULL,
	age INTEGER NOT NULL,
	address TEXT NOT NULL
);


INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');

INSERT INTO classmates 
VALUES ('이한빈', 30, '서울'),
			 ('김효미', 28, '건입'),
			 ('정유정', 27, '인천'),
			 ('김경림', 27, '구디'),
			 ('이창준', 30, '강남');

UPDATE classmates
SET name = '김철수한무두루미',
		address = '제주도'
WHERE rowid = 2;

DELETE FROM classmates WHERE rowid = 5;

SELECT rowid, * FROM classmates;

DELETE FROM classmates WHERE name LIKE '%길%';

DELETE FROM classmates;