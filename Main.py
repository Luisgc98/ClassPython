from database import User

if __name__ == '__main__':
    opc = input('1. Agregar usuario\n2. Consulta de usuario\n')
    if opc == '1':
        user = User(
            name=input(),
            email=input(),
            password=input()
        )
        result = user.AddUser(user)
        print(result)
        
    elif opc == '2':
        opc = input('1. Consultar todos los registros\n2. Consultar con ID\n')
        
        if opc == '1':
            users = User.AllUsers()
            for user in users:
                print('Nombre: '+user.name)
                print('Correo: '+user.email)
        elif opc == '2':
            user_id = input('Ingrese ID del usuario: ')
            user = User.User_by_id(user_id=user_id)
            
            if user:
                print('Nombre: '+user.name)
                print('Correo: '+user.email)
            else:
                print('ID incorrecto.')