import unittest
import testinfra


class Test(unittest.TestCase):

    def setUp(self):
        self.host = testinfra.get_host("local://")

    def test_vim_is_installed(self):
        service = self.host.package("vim")
        self.assertTrue(service.is_installed)

    def test_dnsutils_is_installed(self):
        service = self.host.package("dnsutils")
        self.assertTrue(service.is_installed)

    def test_mtr_tiny_is_installed(self):
        service = self.host.package("mtr-tiny")
        self.assertTrue(service.is_installed)

    def test_whois_is_installed(self):
        service = self.host.package("whois")
        self.assertTrue(service.is_installed)

    def test_net_tools_is_installed(self):
        service = self.host.package("net-tools")
        self.assertTrue(service.is_installed)

    def test_htop_is_installed(self):
        service = self.host.package("htop")
        self.assertTrue(service.is_installed)

    def test_sudo_is_installed(self):
        service = self.host.package("sudo")
        self.assertTrue(service.is_installed)

    def test_telnet_is_installed(self):
        service = self.host.package("telnet")
        self.assertTrue(service.is_installed)

    def test_python_pip_is_installed(self):
        service = self.host.package("python-pip")
        self.assertTrue(service.is_installed)
        
    def test_python_boto_is_installed(self):
        service = self.host.package("python-boto")
        self.assertTrue(service.is_installed)

    def test_mlocate_is_installed(self):
        service = self.host.package("mlocate")
        self.assertTrue(service.is_installed)

    def test_ntp_is_installed(self):
        service = self.host.package("ntp")
        self.assertTrue(service.is_installed)

    def test_tcpdump_is_installed(self):
        service = self.host.package("tcpdump")
        self.assertTrue(service.is_installed)

    def test_nmap_is_installed(self):
        service = self.host.package("nmap")
        self.assertTrue(service.is_installed)

    def test_git_is_installed(self):
        service = self.host.package("git")
        self.assertTrue(service.is_installed)

    def test_less_is_installed(self):
        service = self.host.package("less")
        self.assertTrue(service.is_installed)

    def test_curl_is_installed(self):
        service = self.host.package("curl")
        self.assertTrue(service.is_installed)

    def test_tzdata_is_installed(self):
        service = self.host.package("tzdata")
        self.assertTrue(service.is_installed)

    def test_nginx_is_installed(self):
        service = self.host.package("nginx")
        self.assertTrue(service.is_installed)

if __name__ == "__main__":
    unittest.main()

