from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
URI = "URI"
AUTH = ("neo4j", "auth key")
def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH) 
    driver.verify_connectivity()
    return driver

def node_to_json(node): 
    node_properties = dict(node.items()) 
    return node_properties

def save_car(make, model, reg, year, location, status):
    cars = _get_connection().execute_query("MERGE (a:Car{make: $make, model: $model, reg: $reg, year: $year, location:$location, status:$status}) RETURN a;", make = make, model = model, reg = reg, year = year, location = location, status = status)
    nodes_json = [node_to_json(record["a"]) for record in cars] 
    print(nodes_json)
    return nodes_json

def update_car(make, model, reg, year, location, status): 
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car{reg:$reg}) set a.make=$make, a.model=$model, a.year = $year, a.location = $location, a.status = $status RETURN a;", reg=reg, make=make, model=model, year=year, location=location, status=status)

    print(cars )
    nodes_json = [node_to_json(record["a"]) for record in cars] 
    print(nodes_json)
    return nodes_json

def read_car(reg):
    cars = _get_connection().execute_query("MATCH (a:Car{reg: $reg}) RETURN a;", reg = reg)
    nodes_json = [node_to_json(record["a"]) for record in cars] 
    print(nodes_json)
    return nodes_json

def delete_car(reg):
    _get_connection().execute_query("MATCH (a:Car{reg: $reg}) delete a;", reg = reg)


