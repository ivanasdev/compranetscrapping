from scrapping import *
#from scarpp2 import *

#parametros 

#Proceso 
op1="PROYECTO DE CONVOCATORIA"
op2="PROCEDIMIENTO DE CONTRATACIÓN"
#Ley que rige la contratacion
ol1="LEY DE ADQUISICIONES, ARRENDAMIENTOS Y SERVICIOS DEL SECTOR PÚBLICO"
ol2="LEY DE OBRAS PÚBLICAS Y SERVICIOS RELACIONADOS CON LAS MISMAS"
#Tipo de contratacion
oa1="OBRA PÚBLICA"
oa2="SERVICIOS RELACIONADOS CON LA OBRA"

#Tipo de procedimiento de contratacion 
ot1="ADJUDICACIÓN DIRECTA"
ot2="INVITACIÓN A CUANDO MENOS TRES PERSONAS"
ot3="LICITACIÓN PUBLICA"

#1era cnfuguracion
proceso=op1
ley=ol2
tipocontrata=oa1
tipoproc=ot3
dias=2         #Coloque un entero


iniciar(proceso,ley,tipocontrata,tipoproc,dias) 