from typing import Dict
import os

class PeopleFinderView:
    def finder_person_view(self) -> Dict:
        os.system("cls||clear")

        print('Busca de pessoa \n\n')
        name = input("Determine o nome da pessoa para busca: ")

        person_find_informations =  {
            "name": name
        }

        return person_find_informations
    
    def find_person_success(self, message: Dict) -> None:
        os.system("cls||clear")

        success_message = f'''
            Usuário encontrado com Sucesso!

            Tipo: { message['type'] }
            Registros { message['count'] }
            Infos: 
                Nome: { message['infos']['name'] }
                Idade: { message['infos']['age'] }
                Altura: { message['infos']['height'] }
        '''
        print(success_message)

    def find_person_fail(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao encontrar o Usuário!

            Erro: { error }
        '''
        print(fail_message)