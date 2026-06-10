from jinja2 import Environment, FileSystemLoader, StrictUndefined
 
# Load templates from ./templates/ directory
env = Environment(
    loader=FileSystemLoader("labs/02-device/templates"),
    undefined=StrictUndefined,
)
template = env.get_template("router.j2")
 
variables = {
    "hostname": "BRANCH-RTR-01",
    "interfaces": [
        {"name": "GigabitEthernet0/0", "ip": "10.0.0.1", "mask": "255.255.255.0"},
        {"name": "GigabitEthernet0/1", "ip": "10.0.1.1", "mask": "255.255.255.0"},
    ]
}
 
config = template.render(variables)
print(config)