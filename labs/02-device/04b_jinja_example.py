from jinja2 import Environment, FileSystemLoader, StrictUndefined
 
env = Environment(
    loader=FileSystemLoader("labs/02-device/templates"),
    undefined=StrictUndefined,
)
template = env.get_template("ntp_config.j2")
 
# Render with custom servers
print(template.render(ntp_servers=["172.16.0.1", "172.16.0.2"]))
 
# Render with defaults (no variables passed)
print(template.render())