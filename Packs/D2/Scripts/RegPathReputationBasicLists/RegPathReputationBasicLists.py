import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401

WHITELIST = [r'HKEY_LOCAL_MACHINE\Software\wow6432node\Microsoft\Windows\CurrentVersion\Run\vmware-tray.exe']
BLACKLIST = [r'HKEY_CURRENT_USER\Software\Locky',
             r'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run\Locky']  # guardrails-disable-line
SUSPICIOUS = [r"HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\UrlSearchHooks",
              r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Htmlfile\Shell\Open\Command",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Htmlfile\Shell\Open\Command\(Default)",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Protocols\Filter",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Protocols\Handler",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Active Setup\Installed Components",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dlls",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\VmApplet",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider Filters",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential Providers",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\PLAP Providers",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ShellServiceObjects",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Active Setup\Installed Components",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dlls",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\ShellServiceObjects",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run",
              r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Authentication Packages",
              r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Notification Packages",
              r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig\Security Packages",
              r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Security Packages",
              r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order",
              r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print\Monitors",
              r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot",
              r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot\AlternateShell",
              r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders",
              r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SecurityProviders",
              r"HKEY_LOCAL_MACHINE\Software\Classes\AllFileSystemObjects\ShellEx\ContextMenuHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Classes\AllFileSystemObjects\ShellEx\PropertySheetHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{083863F1-70DE-11d0-BD40-00A0C911CE86}\Instance",
              r"HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{7ED96837-96F0-4812-B211-F13C24117ED3}\Instance",
              r"HKEY_LOCAL_MACHINE\Software\Classes\Directory\Background\ShellEx\ContextMenuHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Classes\Directory\ShellEx\ContextMenuHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Classes\Directory\Shellex\CopyHookHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Classes\Directory\Shellex\DragDropHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Classes\Directory\Shellex\PropertySheetHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Classes\Drive\ShellEx\ContextMenuHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Classes\Folder\ShellEx\ContextMenuHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Classes\Folder\ShellEx\DragDropHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Classes\Folder\ShellEx\PropertySheetHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Classes\Folder\Shellex\ColumnHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Drivers32",
              r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Windows",
              r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Windows\IconServiceLib",
              r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects",
              r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers",
              r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\AllFileSystemObjects\ShellEx\ContextMenuHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\AllFileSystemObjects\ShellEx\PropertySheetHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\CLSID\{083863F1-70DE-11d0-BD40-00A0C911CE86}\Instance",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\CLSID\{7ED96837-96F0-4812-B211-F13C24117ED3}\Instance",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\Directory\Background\ShellEx\ContextMenuHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\Directory\ShellEx\ContextMenuHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\Directory\Shellex\CopyHookHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\Directory\Shellex\DragDropHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\Directory\Shellex\PropertySheetHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\Drive\ShellEx\ContextMenuHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\Folder\ShellEx\ContextMenuHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\Folder\ShellEx\DragDropHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\Folder\ShellEx\PropertySheetHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Classes\Folder\Shellex\ColumnHandlers",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects",
              r"HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers",
              r"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control",
              r"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ServiceControlManagerExtension",
              r"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\BootExecute",
              r"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\KnownDlls",
              r"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\Wds\rdpwd",
              r"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\Wds\rdpwd\StartupPrograms",
              r"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services",
              r"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\WinSock2\Parameters\NameSpace_Catalog5\Catalog_Entries",
              r"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\WinSock2\Parameters\NameSpace_Catalog5\Catalog_Entries64",
              r"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\WinSock2\Parameters\Protocol_Catalog9\Catalog_Entries",
              r"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\WinSock2\Parameters\Protocol_Catalog9\Catalog_Entries64",
              r"HKEY_LOCAL_MACHINE\software\microsoft\windows\currentversion\policies\explorer\run",
              r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices",
              r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices",
              r"HKEY_LOCAL_MACHINE\software\microsoft\wbem\ess\//./root/cimv2\win32clockprovider",
              r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce",
              r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify",
              r"HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad",
              r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnceEx",
              r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run",
              r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce",
              r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run",
              r"HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows\load",
              r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\SharedTaskScheduler"]


def check_reg_in_list(path, list_to_check):
    for key in list_to_check:
        if path.startswith(key.upper()):
            return True
    return False


def main():
    # registry keys are case insensative: https://docs.microsoft.com/en-us/windows/desktop/sysinfo/structure-of-the
    # -registry
    reg_path = NormalizeRegistryPath(demisto.args()['input'].upper())

    if check_reg_in_list(reg_path, WHITELIST):
        score = 1
    elif check_reg_in_list(reg_path, BLACKLIST):
        score = 3
    elif check_reg_in_list(reg_path, SUSPICIOUS):
        score = 2
    else:
        score = 0

    outputs = {
        'Path': reg_path,
        'Score': score
    }

    demisto.results({
        'Type': entryTypes['note'],
        'ContentsFormat': formats['json'],
        'Contents': score,
        'ReadableContentsFormat': formats['text'],
        'HumanReadable': "The Registry Path reputation for: {} is: {}".format(reg_path, score),
        'EntryContext': {
            'RegistryKey(val.Path == obj.Path)': outputs
        }
    })


if __name__ in ['__main__', 'builtin', 'builtins']:
    main()
