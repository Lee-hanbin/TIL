CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);

ALTER TABLE contacts RENAME To new_contracts;

ALTER TABLE new_contract RENAME COLUMN name TO last_name;

ALTER TABLE new_contract ADD COLUMN address TEXT NOT NULL;

ALTER TABLE new_contract DROP COLUMN address;

DROP TABLE new_contract;
