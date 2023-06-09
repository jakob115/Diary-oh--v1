-- These SQL commands are for SQLite database engine
-- For MySQL, PostgreSQL etc. they might be different 

CREATE TABLE IF NOT EXISTS 'blogpost' (
  'id' INTEGER NOT NULL PRIMARY KEY,
  'created' DATETIME NOT NULL,
  'updated' DATETIME NOT NULL,
  'title' VARCHAR NOT NULL,
  'summary' VARCHAR NOT NULL,
  'content' VARCHAR NOT NULL
);
