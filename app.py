"""
Во избежание циклических импортов, выносим app в отдельный файл
"""


from fastapi import FastAPI


app = FastAPI()
