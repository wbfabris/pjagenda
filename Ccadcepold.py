#Class:     Cmedcep
#Obejtivo:  Acessa os correios e pega o cep
#Data:      Junho/2021
#Input:     Passa o cep
#Process:   Gera uma lista com enderço, Bairro, cidade, UF
#OutPut:    Retorna a lista
#================================================================
import  pycep_correios #import get_address_from_cep, is_valid_cep, WebService
#import pycep_correios
#from pycep_correios.exceptions import CEPNotFound, InvalidCEP

class Obterend():

    """[recebe o cep e retorna o endereço]
    """
    def __init__(self,  pcep):
        """__init__ [Recebe o str com 8 digitos]
        Args:
            pcep ([str]): [numero do cep]
        """
        self.pcep = pcep

    #_________________________________________
    def pxobterend(self):

        """pxobterend [passa o cep e recebe uma lista]
        Returns:
            [list]: [logradouro, cidade, bairro, uf e o cep]
                    ['bairro':, 'cep':, 'cidade':, 'logradouro':, 'uf':]
        """
        pass 
        # try:
        #     endereco = pycep_correios.get_address_from_cep(self.pcep)
        #     return endereco

        # except CEPNotFound as ecnf:
        #     return {'logradouro': 'CEP Não Cadastrado'}

        # except InvalidCEP as ecinv:
        #     return {'logradouro': 'CEP invalido'}

#++++++++++++++++++++++++++++++++++++++++++
#ocep = Obterend('59020-310')
#lsend = ocep.pxobterend()
# = 1
# if lsend['logradouro'] == 'CEP invalido':
#     print('Cep invalido')
# else:
#      print('Cep OK')

# a=1
ocep = Obterend('28625000')
lsend = ocep.pxobterend()
aaa=1
#pxmain('28625000')
#pxmain('37503130')
# print(endereco['cep'])
# print(endereco['logradouro'])
# print(endereco['bairro'])
# print(endereco['cidade'])
# print(endereco['uf'])
# print(endereco['cep'])

def consultar_cep(cep):
    # Valida o formato do CEP
    if is_valid_cep(cep):
        try:
            # Consulta o CEP usando o serviço 'APICEP'
            endereco = get_address_from_cep(cep, webservice=WebService.APICEP)
            print(f"Informações do CEP {cep}:")
            print(endereco)
        except Exception as e:
            print(f"Erro ao consultar o CEP {cep}: {e}")
    else:
        print(f"O CEP {cep} é inválido.")

# Exemplo de uso
cep = '01001-000'  # Insira o CEP desejado aqui
consultar_cep(cep)
