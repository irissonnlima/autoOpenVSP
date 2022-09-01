import os
import sys

my_os = sys.platform
assert (
    my_os == 'linux'
), 'FatalERROR: This library only works on linux systems!'

vsp_on = os.system('which vsp >> foo')
assert vsp_on == 0, 'FatalERROR: OpenVSP is not installed!'
