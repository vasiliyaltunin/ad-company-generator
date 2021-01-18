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

$ous = Import-Csv -Encoding UTF8 -Delimiter ';' -Path $PSScriptRoot"\ous.csv"

New-ADOrganizationalUnit –Name Company –Path " DC=altuninvv,DC=local" –Description "Altunin Soft"


foreach ($ou in $ous) {

New-ADOrganizationalUnit –Name $ou.name `
–Path "OU=Company,DC=altuninvv,DC=local" `
–Description $ou.descr

}


$users = Import-Csv -Encoding UTF8 -Delimiter ';' -Path $PSScriptRoot"\users.csv"

#Write-Host $users

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



 
Set-ADUser -Identity $user.login `
-Add @{otherTelephone=$user.vntel} `


}

