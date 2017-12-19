from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(File):
    present = [
        "/etc/graylog/server"
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/etc/graylog/server/log4j2.xml",
        "/etc/graylog/server/node-id",
        "/etc/graylog/server/server.conf",
        "/usr/share/graylog-server/plugin/graylog-plugin-slack-2.4.0.jar",
        "/usr/share/graylog-server/plugin/metrics-reporter-prometheus-1.5.0.jar"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_service(Service):
    present = [
        "graylog-server"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_enabled
            assert s.is_running


def test_packages(Package):
    present = [
        "graylog-server"
    ]
    if present:
        for package in present:
            p = Package(package)
            assert p.is_installed


def test_socket(Socket):
    present = [
        # "unix:///run/haproxy/admin.sock",
        "tcp://127.0.0.1:9000"
    ]
    for socket in present:
        s = Socket(socket)
        assert s.is_listening
