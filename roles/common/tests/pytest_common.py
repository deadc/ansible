
def test_vim_is_installed(host):
        vim = host.package("vim")
        assert vim.is_installed

def test_dnsutils_is_installed(host):
        dnsutils = host.package("dnsutils")
        assert dnsutils.is_installed

def test_mtr_tiny_is_installed(host):
        mtr_tiny = host.package("mtr-tiny")
        assert mtr_tiny.is_installed

def test_whois_is_installed(host):
        whois = host.package("whois")
        assert whois.is_installed

def test_net_tools_is_installed(host):
        net_tools = host.package("net-tools")
        assert net_tools.is_installed

def test_htop_is_installed(host):
        htop = host.package("htop")
        assert htop.is_installed

def test_sudo_is_installed(host):
        sudo = host.package("sudo")
        assert sudo.is_installed

def test_telnet_is_installed(host):
        telnet = host.package("telnet")
        assert telnet.is_installed

def test_python_pip_is_installed(host):
        python_pip = host.package("python-pip")
        assert python_pip.is_installed
        
def test_python_boto_is_installed(host):
        python_boto = host.package("python-boto")
        assert python_boto.is_installed

def test_mlocate_is_installed(host):
        mlocate = host.package("mlocate")
        assert mlocate.is_installed

def test_ntp_is_installed(host):
        ntp = host.package("ntp")
        assert ntp.is_installed

def test_tcpdump_is_installed(host):
        tcpdump = host.package("tcpdump")
        assert tcpdump.is_installed

def test_nmap_is_installed(host):
        nmap = host.package("nmap")
        assert nmap.is_installed

def test_git_is_installed(host):
        git = host.package("git")
        assert git.is_installed

def test_less_is_installed(host):
        less = host.package("less")
        assert less.is_installed

def test_curl_is_installed(host):
        curl = host.package("curl")
        assert curl.is_installed

def test_tzdata_is_installed(host):
        tzdata = host.package("tzdata")
        assert tzdata.is_installed

def test_nginx_is_installed(host):
        nginx = host.package("nginx")
        assert nginx.is_installed

