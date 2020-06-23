@echo off
SET IP=tarterm01 
SET USERNAME=sarasinpur
SET PASSWORD=P0nd!46616
SET DOMAIN=7Eleven
cmd /c cmdkey /add:TERMSRV/server.%IP% /user:%DOMAIN%\%USERNAME% /pass:%PASSWORD%
cmd /c "cmdkey /generic:TERMSRV/%IP% /user:%USERNAME% /pass:%PASSWORD%"
cmd /c "mstsc /f /v:%IP%"
cmd /c "timeout /t 0 /nobreak"
cmd /c "cmdkey /delete:TERMSRV/%IP%"