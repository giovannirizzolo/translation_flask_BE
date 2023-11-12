import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

db_string = os.getenv('DB_STRING')

engine = create_engine(db_string, 
                       connect_args={
                           "ssl": {
                                "ssl_ca": "/etc/ssl/cert.pem"
                           }
                       })


    
    
    # query_res = res.all()
    # print(query_res)
    # print('type(res): ', type(res))
    # print('type(res.all()) ', type(res.all()))
    # print(type(query_res[0]))
    

    # print('FIRST LANG IS: ', first_lang)