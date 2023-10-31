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

def save_employee(name, empid, address, branch):
    employees = _get_connection().execute_query("MERGE (a:Employee{name:$name, empid:$empid, address:$address, branch:$branch}) RETURN a;", name=name, empid=empid, address=address, branch=branch)
    nodes_json = [node_to_json(record["a"]) for record in employees] 
    print(nodes_json)
    return nodes_json

def update_employee(name, empid, address, branch): 
    with _get_connection().session() as session:
        employees = session.run("MATCH (a:Employee{empid:$empid}) set a.name=$name, a.address = $address, a.branch = $branch RETURN a;", empid=empid, name=name, address=address, branch=branch)

    print(employees )
    nodes_json = [node_to_json(record["a"]) for record in employees] 
    print(nodes_json)
    return nodes_json

def read_employee(empid):
    employees = _get_connection().execute_query("MATCH (a:Employee{empid: $empid}) RETURN a;", empid = empid)
    nodes_json = [node_to_json(record["a"]) for record in employees] 
    print(nodes_json)
    return nodes_json

def delete_employee(empid):
    _get_connection().execute_query("MATCH (a:Employee{empid: $empid}) delete a;", empid = empid)

