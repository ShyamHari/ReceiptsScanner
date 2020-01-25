from flask import Flask, render_template
from app import app

receipts = [
    {
        'total': '32.50',
        'date': '01/15/20',
        'img' : 'temp'
    }
    ,
    {
        'total': '25.00',
        'date': '01/17/20',
        'img' : 'temp2'
    }
]