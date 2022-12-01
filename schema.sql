CREATE TABLE users (
                    id INTEGER NOT NULL UNIQUE,
                    username TEXT NOT NULL,
                    password text NOT NULL,
                    PRIMARY KEY(id AUTOINCREMENT)
                );

CREATE TABLE post (
                    post_id INTEGER NOT NULL UNIQUE,
                    post_author TEXT NOT NULL,
                    post_entry TEXT NOT NULL,
                    post_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    post_replyability text,
                    PRIMARY KEY(post_id AUTOINCREMENT),
                    FOREIGN KEY(post_author) REFERENCES users(id)
                );

CREATE TABLE reply (
                    reply_id INTEGER NOT NULL UNIQUE,
                    reply_author TEXT NOT NULL,
                    reply_entry TEXT NOT NULL,
                    reply_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    post_id INTEGER,
                    PRIMARY KEY(reply_id AUTOINCREMENT),
                    FOREIGN KEY(post_id) REFERENCES post(post_id),
                    FOREIGN KEY(reply_author) REFERENCES users(id)
                );

CREATE TABLE tags (
                post_id INTEGER,
                reply_id INTEGER,
                tag INTEGER NOT NULL,
                FOREIGN KEY(post_id) REFERENCES post(post_id),
                FOREIGN KEY(reply_id) REFERENCES reply(reply_id)
            );
