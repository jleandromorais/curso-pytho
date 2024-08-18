

velocidade = 61
local_carro = 80

RADAR_1 = 60 
LOCAL_1 = 100
RADAR_RANGE = 20

velocidade_carro_pass_radar_1 = velocidade >RADAR_1
Local_do_carro= local_carro >= ( LOCAL_1 - RADAR_RANGE) and\
local_carro <= (  LOCAL_1 + RADAR_RANGE)
carro_passou_do_local =  local_carro-LOCAL_1
carro_multado = velocidade_carro_pass_radar_1 and Local_do_carro

if carro_passou_do_local>0:
    print(f'O carro passou do radar e esta a :{carro_passou_do_local}de distancia ')
elif carro_passou_do_local<0:
    print(f'O carro ainda n passou do local falta:{carro_passou_do_local}')

if velocidade_carro_pass_radar_1 and Local_do_carro:
    print(f'A velocidade foi maior no radar1 com essa velocidade:{velocidade}')


if carro_multado and \
velocidade_carro_pass_radar_1:
    print('carro foi multado')
   