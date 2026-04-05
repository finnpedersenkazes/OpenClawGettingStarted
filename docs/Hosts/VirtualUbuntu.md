# Virtual Ubuntu

A virtual machine can work, but it adds another layer of complexity. Use a VM only if you specifically want isolation from your daily machine.

## VM on Windows 11

- Install VMware Workstation Pro 25
- Download Ubuntu 25 ISO
- Standard configuration
- Install updates after creation

| Setting    | Recommended       |
| ---------- | ----------------- |
| CPU        | 4+ vCPU           |
| RAM        | 16 GB             |
| Disk       | 40 GB             |
| Processors | 1 socket, 8 cores |

## VM on macOS

- Install VMware Fusion Pro 25
- Download Ubuntu 25 ISO
- Standard configuration
- Install updates after creation

## Shared folders between host and guest

Sharing a folder lets you move files between your Windows or macOS host and the Ubuntu guest without using the network.

### VMware Workstation (Windows host)

1. Create a folder on Windows to use as the share (e.g. `D:\VMshare`).
2. Power down the virtual machine.
3. Select the VM and open **Edit virtual machine settings**.
4. Go to **Options** > **Shared Folders**.
5. Select **Always enabled**, click **Add**, and browse to the folder you created.
6. Enable the share, click **Finish** and **OK**.
7. Boot the VM.

Inside Ubuntu, the shared folder should appear at:

```bash
ls /mnt/hgfs/
```

If `/mnt/hgfs` is empty, mount it manually:

```bash
sudo vmhgfs-fuse .host:/ /mnt/hgfs/ -o allow_other -o uid=1000
```

If `/mnt/hgfs` does not exist at all:

```bash
sudo mkdir -p /mnt/hgfs
sudo vmhgfs-fuse .host:/ /mnt/hgfs/ -o allow_other -o uid=1000
```

To list available shared folders:

```bash
vmware-hgfsclient
```

To make the mount persist across reboots, add this line to `/etc/fstab`:

```text
.host:/  /mnt/hgfs  fuse.vmhgfs-fuse  allow_other,uid=1000  0  0
```

### VMware Fusion (macOS host)

The same **Shared Folders** setting is available under the VM's **Settings** > **Sharing**. The guest-side mount path and commands are identical.

Reference: [Share folders between Windows host and Ubuntu guest](https://ascheng.medium.com/how-vmware-to-share-folders-between-windows-host-and-ubuntu-guest-4bc4b48e2f0)

## Things to watch out for

- Networking between host and guest can be tricky
- Docker inside a VM adds an extra layer
- USB and GPU passthrough may not work as expected

Once the VM is running with Ubuntu, follow the same installation path as a dedicated Ubuntu machine.

## Next steps

- **OpenClaw path:** [AI Models](../Models.md) then [OpenClaw Prerequisites](../OpenClaw/PreInstallation.md)
- **NemoClaw path:** [NemoClaw Prerequisites](../NemoClaw/PreInstallation.md)
