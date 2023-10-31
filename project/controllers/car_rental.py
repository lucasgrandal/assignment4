from project import app
from flask import render_template, request, redirect, url_for 
from project.models.car import *
from project.models.costumer import *
from project.models.employee import *

@app.route('/order-car', methods=['GET']) 
def order_car(id, reg):
    costumer = read_costumer(id)
    car = read_car(reg)
    if(costumer[4] == "null" & car[5] == "available"):
        car[5]="booked"

    return update_car(car[0], car[1], car[2], car[3], car[4], car[5])

@app.route('/cancel-order-car', methods=['GET']) 
def cancel_order_car(id, reg):
    costumer = read_costumer(id)
    car = read_car(reg)
    if(costumer[4] == car[2] & car[5] == "booked"):
        car[5]="available"
        update_costumer(costumer[0], costumer[1], costumer[2], costumer[3], "null")

    return update_car(car[0], car[1], car[2], car[3], car[4], car[5])

@app.route('/rent-car', methods=['GET']) 
def rent_car(id, reg):
    costumer = read_costumer(id)
    car = read_car(reg)
    if(costumer[4] == car[2] & car[5] == "booked"):
        car[5]="rented"

    return update_car(car[0], car[1], car[2], car[3], car[4], car[5])

@app.route('/return-car', methods=['GET']) 
def rent_car(id, reg, status):
    costumer = read_costumer(id)
    car = read_car(reg)
    if(costumer[4] == car[2] & car[5] == "rented"):
        update_costumer(costumer[0], costumer[1], costumer[2], costumer[3], "null")
        if(status == "ok"):
            car[5] = "available"
        else:
            car[5] = "damaged"

    return update_car(car[0], car[1], car[2], car[3], car[4], car[5])



