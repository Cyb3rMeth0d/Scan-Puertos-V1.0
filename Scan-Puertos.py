#!/usr/bin/env python
#!Developer Osama Mahmood
#!Email : osama.mahmood40@gmail.com
#!Website : http://securitytraning.com

from socket import * 
import os

if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')


print "*******************************************"
print "************Scaner de Puertos  ************"
print "***********************Cyb3rMeth0d v1.0****"

if __name__ == '__main__':
    targetserver = raw_input('Establecer Host o IP: ')
    targetIP = gethostbyname(targetserver)
    print 'Listo para el Escaneo :3 ', targetIP

    #scan reserved ports
    for i in range(1, 1025):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print 'Puerto %d: ABIERTO' % (i,)
        s.close()

print '***********************************************'
print "Escaneo Finalizado"
print '**********************Cyb3rMeth0d V1.0*********'