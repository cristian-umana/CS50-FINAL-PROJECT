CREATE TABLE users (
                    id INTEGER,
                    username TEXT NOT NULL,
                    PRIMARY KEY(id)
                );

CREATE TABLE post (
                    post_id INTEGER,
                    user_id TEXT NOT NULL,
                    post_entry TEXT NOT NULL,
                    post_time NUMERIC,
                    post_replyability text,
                    PRIMARY KEY(post_id),
                    FOREIGN KEY(user_id) REFERENCES users(id)
                );

CREATE TABLE advice (
                    reply_id INTEGER,
                    user_id TEXT NOT NULL,
                    reply_entry TEXT NOT NULL,
                    reply_time NUMERIC,
                    post_id INTEGER,
                    PRIMARY KEY(reply_id),
                    FOREIGN KEY(post_id) REFERENCES post(post_id),
                    FOREIGN KEY(user_id) REFERENCES users(id)
                );

CREATE TABLE tags (
                post_id INTEGER,
                reply_id INTEGER,
                tag INTEGER NOT NULL,
                FOREIGN KEY(post_id) REFERENCES post(post_id),
                FOREIGN KEY(reply_id) REFERENCES reply(reply_id)
            );
