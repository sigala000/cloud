from pyVim import connect
from pyVmomi import vim
import ssl
import atexit
import json

__author__ = 'ndansi'

# Disable SSL certificate verification
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
# context.verify_mode = ssl.CERT_NONE

# Connect to the ESXi host
try:
    sig = json.load(open('iso.json'))
    print(sig)
except:
    print("error")
service_instance = connect.SmartConnect(host=sig["host"], user=sig["user"], pwd=sig["password"], disableSslCertValidation =sig["disable_ssl_verification"])
atexit.register(connect.Disconnect, service_instance)

# Get the ESXi host and datacenter objects
content = service_instance.RetrieveContent()
datacenter = content.rootFolder.childEntity[0]
host = datacenter.hostFolder.childEntity[0].host[0]

# Create a new virtual machine configuration
# vm_name = "shaba99"
vm_folder = datacenter.vmFolder
datastore = host.datastore[0]
resource_pool = host.parent.resourcePool

vmx_file = vim.vm.FileInfo(logDirectory=None, snapshotDirectory=None, suspendDirectory=None, vmPathName="[{}] {}".format(datastore.name, sig["name"] ))
config = vim.vm.ConfigSpec(name=sig["name"], memoryMB=sig["memoryMB"], numCPUs=sig["numCPUs"], files=vmx_file, guestId=sig["guestId"], version=sig["version"])
config.bootOptions  = vim.vm.BootOptions()
config.bootOptions.bootDelay = 5000
# Attach the ISO file to the VM's CD/DVD drive
cd_spec = vim.vm.device.VirtualDeviceSpec()
cd_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
cd_spec.device = vim.vm.device.VirtualCdrom()
cd_spec.device.backing = vim.vm.device.VirtualCdrom.IsoBackingInfo(fileName=sig["iso_path"])
cd_spec.device.connectable = vim.vm.device.VirtualDevice.ConnectInfo()
cd_spec.device.connectable.startConnected = True
cd_spec.device.connectable.allowGuestControl = True
config.deviceChange = [cd_spec]
# Power on the VM to start the installation
vm = vm_folder.CreateVM_Task(config=config, pool=resource_pool, host=host)
while True:
    if vm.info.state == 'poweredOn':
        break

print("VM has been powered on for the installation process.")

# Clean up the connection
atexit.unregister(connect.Disconnect)