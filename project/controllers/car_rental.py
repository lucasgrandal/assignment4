from project import app
from flask import request
from project.models.car import *
from project.models.costumer import *
from project.models.employee import *

@app.route('/order-car', methods=['GET']) 
def order_car(id, reg):
    costumer = read_costumer(id)
    car = read_car(reg)
    if(costumer['booked'] == "null" and car['status'] == "available"):
        car['status']="booked"

    return update_car(car['make'], car['model'], car['year'], car['reg'], car['location'], car['status'])

@app.route('/cancel-order-car', methods=['POST']) 
def cancel_order_car(id, reg):
    costumer = read_costumer(id)
    car = read_car(reg)
    if(costumer['booked'] == car['reg'] and car['status'] == "booked"):
        car['status']="available"
        update_costumer(costumer['name'], costumer['id'], costumer['age'], costumer['address'], "null")

    return update_car(car['make'], car['model'], car['year'], car['reg'], car['location'], car['status'])

@app.route('/rent-car', methods=['GET']) 
def rent_car(id, reg):
    costumer = read_costumer(id)
    car = read_car(reg)
    if(costumer['booked'] == car['reg'] and car['status'] == "booked"):
        car['status']="rented"

    return update_car(car['make'], car['model'], car['year'], car['reg'], car['location'], car['status'])

@app.route('/return-car', methods=['POST']) 
def return_car(id, reg, status):
    costumer = read_costumer(id)
    car = read_car(reg)
    if(costumer['booked'] == car['reg'] and car['status'] == "rented"):
        update_costumer(costumer['name'], costumer['id'], costumer['age'], costumer['address'], "null")
        if(status == "ok"):
            car['status'] = "available"
        else:
            car['status'] = "damaged"

    return update_car(car['make'], car['model'], car['year'], car['reg'], car['location'], car['status'])



