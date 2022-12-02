CREATE TABLE post (
                    post_id INTEGER NOT NULL UNIQUE,
                    post_entry TEXT NOT NULL,
                    post_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    post_replyability text,
                    PRIMARY KEY(post_id AUTOINCREMENT)
                );

CREATE TABLE reply (
                    reply_id INTEGER NOT NULL UNIQUE,
                    post_id INTEGER,
                    reply_entry TEXT NOT NULL,
                    reply_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY(reply_id AUTOINCREMENT),
                    FOREIGN KEY(post_id) REFERENCES post(post_id)
                );

CREATE TABLE tags (
                post_id INTEGER,
                reply_id INTEGER,
                tag INTEGER,
                FOREIGN KEY(post_id) REFERENCES post(post_id),
                FOREIGN KEY(reply_id) REFERENCES reply(reply_id)
            );
