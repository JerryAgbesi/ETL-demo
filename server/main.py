import os
from fastapi import FastAPI,HTTPException
import pandas as pd
import uvicorn


BASE_DIR = '/media/jerry/463A06993A068661/data_science_arena/data'
CACHE_DIR = os.path.join(BASE_DIR,'cached_data')

dataset = os.path.join(CACHE_DIR,'movies-box-office-dataset-cleaned.csv')


app = FastAPI()


@app.get('/')
async def get_root():
    return {"msg":"responsive"}

@app.get('/box_office_number')
async def get_box_office_number(rank: int):
    df = pd.read_csv(dataset)
    # df.iloc[rank]
    # try:
    return df.to_dict(df.loc[rank])
    # except:
    #     raise HTTPException(400,"Something went wrong try again")


