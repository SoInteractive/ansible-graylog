from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(File):
    present = [
        "/usr/share/graylog-plugins"
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_packages(Package):
    present = [
        "python-pip"
    ]
    if present:
        for package in present:
            p = Package(package)
            assert p.is_installed


def test_socket(host):
    present = [
        "tcp://127.0.0.1:9000"
    ]
    for socket in present:
        s = host.socket(socket)
        assert s.is_listening
