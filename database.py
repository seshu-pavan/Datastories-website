import os
from sqlalchemy import create_engine, text
import pymysql
from dotenv import load_dotenv

load_dotenv("C:/Users/tanuj/PycharmProjects/Datastories-website/templates/.env")

DB_CONNECTION = os.environ["database_key"]

engine = create_engine(DB_CONNECTION,
connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)


def add_comments_to_db(data):
    with engine.connect() as conn:
        query = text("INSERT INTO comments (postid, username, usercomment) "
                     "VALUES (:postid, :username, :usercomment);")
        conn.execute(query,
        {
            "postid": 1,
            "username": data["username"],
            "usercomment": data["usercomment"]
        }

    )


def load_comments_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from comments order by user_id desc;"))
        coloum_name = result.keys()
        result_dict = []
        for row in result.all():
            result_dict.append(dict(zip(coloum_name, row)))
        return result_dict


def add_contact_to_db(data):
    with engine.connect() as conn:
        query = text("INSERT INTO contacts (username, useremail, usermessage) "
                     "VALUES (:username, :useremail, :usermessage);")
        conn.execute(query,
        {
            "username": data["username"],
            "useremail": data["useremail"],
            "usermessage": data["usermessage"]
        }

    )