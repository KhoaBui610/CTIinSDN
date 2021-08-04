curl -X PUT http://localhost:8080/firewall/module/enable/0000000000000001
curl -X PUT http://localhost:8080/firewall/module/enable/0000000000000002
curl -X PUT http://localhost:8080/firewall/module/enable/0000000000000003
curl -X POST -d '{"dl_type": "ARP"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"dl_type": "IPv4"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"dl_type": "IPv6"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"dl_type": "ARP"}' http://localhost:8080/firewall/rules/0000000000000002
curl -X POST -d '{"dl_type": "IPv4"}' http://localhost:8080/firewall/rules/0000000000000002
curl -X POST -d '{"dl_type": "IPv6"}' http://localhost:8080/firewall/rules/0000000000000002
curl -X POST -d '{"dl_type": "ARP"}' http://localhost:8080/firewall/rules/0000000000000003
curl -X POST -d '{"dl_type": "IPv4"}' http://localhost:8080/firewall/rules/0000000000000003
curl -X POST -d '{"dl_type": "IPv6"}' http://localhost:8080/firewall/rules/0000000000000003
