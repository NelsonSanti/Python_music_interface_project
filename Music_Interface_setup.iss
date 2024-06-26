; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Music_Interface_Nelson_Santiago"
#define MyAppVersion "1.01_V2"
#define MyAppPublisher "NelsonSantiago"
#define MyAppExeName "ProjetoFinalLogin_Nelson_Santiago.exe"
#define MyAppAssocName MyAppName + "_Setup"
#define MyAppAssocExt ".myp"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{E148B0F4-4358-4CA2-9DDD-54288F5F3023}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
ChangesAssociations=yes
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=C:\Users\Nelso\Downloads\GNU open source license.rtf
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=C:\Users\Nelso\Documents\CNN\Desempregado\Forma��o Python IEFP\Python\Projeto UFCD 10795
OutputBaseFilename=Music_Interface_NelsonSantiago_Setup_1.01_V2
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "portuguese"; MessagesFile: "compiler:Languages\Portuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\build\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\closed_eye.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\loginStepbyStep.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\music_interface"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\musicalnote1_83800.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\musicinterface.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\musicinterface.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\opened_eye.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\projeto_base_de_dados_musica_nelson.sql"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\Projeto_final_Nelson_santiago_sem_login.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\ProjetoFinalLogin_Nelson_Santiago.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nelso\PycharmProjects\pythonProject1\Projeto1_final_Nelson_santiago_com_login\ProjetoFinalLogin_Nelson_Santiago.spec"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

