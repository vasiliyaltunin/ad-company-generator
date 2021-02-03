#***************************************************************************
#*
#* Copyright 2021 Vasiliy Altunin <skyr@altuninvv.ru>. All rights reserved.
#*
#* Use of this source code is governed by a BSD-style
#* license that can be found in the LICENSE file.
#*
#* Created for articles of site https://blog.altuninvv.ru
#*
#* Script to add users and OU from generated CSV files
#*
#***************************************************************************

Import-Module ActiveDirectory

cls

Write-Host "Importing ou"

$ous = Import-Csv -Encoding UTF8 -Delimiter ';' -Path $PSScriptRoot"\ous.csv"

Write-Host "Creating Company OU"

New-ADOrganizationalUnit –Name Company –Path " DC=altuninvv,DC=local" –Description "Altunin Soft"

Write-Host "Creating Groups"

New-ADGroup -Name gg-ruk -GroupScope Global –Path "OU=Company,DC=altuninvv,DC=local"
New-ADGroup -Name gg-buh -GroupScope Global –Path "OU=Company,DC=altuninvv,DC=local"
New-ADGroup -Name gg-it -GroupScope Global –Path "OU=Company,DC=altuninvv,DC=local"
New-ADGroup -Name gg-otdel1 -GroupScope Global –Path "OU=Company,DC=altuninvv,DC=local"
New-ADGroup -Name gg-otdel2 -GroupScope Global –Path "OU=Company,DC=altuninvv,DC=local"
New-ADGroup -Name gg-otdel3 -GroupScope Global –Path "OU=Company,DC=altuninvv,DC=local"
New-ADGroup -Name gg-otdel4 -GroupScope Global –Path "OU=Company,DC=altuninvv,DC=local"

Write-Host "Creating OUs"

foreach ($ou in $ous) {

New-ADOrganizationalUnit –Name $ou.name `
–Path "OU=Company,DC=altuninvv,DC=local" `
–Description $ou.descr

}

Write-Host "Importing users"

$users = Import-Csv -Encoding UTF8 -Delimiter ';' -Path $PSScriptRoot"\users.csv"

#Write-Host $users

$i=0;
Write-Host "Creating users"

foreach ($user in $users) {

New-ADUser -Name $user.login `
-DisplayName $user.fio `
-GivenName $user.fname `
-Surname $user.lname `
-Initials $user.initials `
-OfficePhone $user.workphone `
-Department $user.department `
-Title $user.jobtitle `
-UserPrincipalName $user.login `
-MobilePhone $user.cellphone `
-SamAccountName $user.samaccname `
-Path $user.ou `
-EmailAddress $user.email `
-StreetAddress $user.addr `
-Office $user.kab `
-Company $user.company `
-Fax $user.fax `
-AccountPassword (ConvertTo-SecureString $user.passwd -AsPlainText -force) -Enabled $true


if (($i -gt -1) -and ($i -lt 4)) {
    $group = 'CN=gg-ruk,OU=Company,DC=altuninvv,DC=local'
    Add-ADGroupMember -Identity $group -Members $user.login
}
if (($i -gt 3) -and ($i -lt 8)) {
    $group = 'CN=gg-buh,OU=Company,DC=altuninvv,DC=local'
    Add-ADGroupMember -Identity $group -Members $user.login
}
if (($i -gt 7) -and ($i -lt 10)) {
    $group = 'CN=gg-it,OU=Company,DC=altuninvv,DC=local'
    Add-ADGroupMember -Identity $group -Members $user.login
}
if (($i -gt 9) -and ($i -lt 32)) {
    $group = 'CN=gg-otdel1,OU=Company,DC=altuninvv,DC=local'
    Add-ADGroupMember -Identity $group -Members $user.login
}
if (($i -gt 31) -and ($i -lt 54)) {
    $group = 'CN=gg-otdel2,OU=Company,DC=altuninvv,DC=local'
    Add-ADGroupMember -Identity $group -Members $user.login
}
if (($i -gt 53) -and ($i -lt 76)) {
    $group = 'CN=gg-otdel3,OU=Company,DC=altuninvv,DC=local'
    Add-ADGroupMember -Identity $group -Members $user.login
}
if ($i -gt 75) {
    $group = 'CN=gg-otdel4,OU=Company,DC=altuninvv,DC=local'
    Add-ADGroupMember -Identity $group -Members $user.login
}

 $i = $i + 1

Set-ADUser -Identity $user.login `
-Add @{otherTelephone=$user.vntel} `
}

Write-Host "Done!"