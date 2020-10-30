datacenter = "localhost",
data_dir = "/consul/data"
log_level = "err"

server = true
bootstrap_expect = 1
ui = true

bind_addr = "0.0.0.0"
client_addr = "0.0.0.0"

ports {
  dns = 53
}