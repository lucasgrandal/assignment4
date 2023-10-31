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

def save_costumer(name, id, age, address):
    costumers = _get_connection().execute_query("MERGE (a:Costumer{name:$name, id:$id, age:$age, address:$address, booked:$booked}) RETURN a;", name=name, id=id, age=age, address=address, booked="null")
    nodes_json = [node_to_json(record["a"]) for record in costumers] 
    print(nodes_json)
    return nodes_json

def update_costumer(name, id, age, address, booked): 
    with _get_connection().session() as session:
        costumers = session.run("MATCH (a:Costumer{id:$id}) set a.name=$name, a.age=$age, a.address = $address, a.booked = $booked RETURN a;", id=id, name=name, age=age, address=address, booked=booked)

    print(costumers )
    nodes_json = [node_to_json(record["a"]) for record in costumers] 
    print(nodes_json)
    return nodes_json

def read_costumer(id):
    costumers = _get_connection().execute_query("MATCH (a:Costumer{id: $id}) RETURN a;", id = id)
    nodes_json = [node_to_json(record["a"]) for record in costumers] 
    print(nodes_json)
    return nodes_json

def delete_costumer(id):
    _get_connection().execute_query("MATCH (a:Costumer{id: $id}) delete a;", id = id)

