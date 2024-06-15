import mysql.connector

conexao = mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='BD_Projeto',
)

cursor = conexao.cursor()

#CREATE

nome = "MARIA ALVES"
cpf = "854.953.418-10"
email = "maria21@gmail.com"
login = "******"
senha = "******"
comando = f'INSERT INTO USUARIO (NOME, CPF, EMAIL, LOGIN, SENHA) VALUES ("{nome}", "{cpf}", "{email}", "{login}", "{senha}")'
cursor.execute(comando)
conexao.commit()

#READ

comando = f'SELECT * FROM USUARIO'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#UPDATE

nome = "MARIA ALVES"
email = "mariaalves@gmail.com"
comando = f'UPDATE USUARIO SET EMAIL = "{email}" WHERE NOME = "{nome}" '
cursor.execute(comando)
conexao.commit()

#DELETE

nome = "MARIA ALVES"
comando = f'DELETE FROM USUARIO WHERE NOME = "{nome}" '
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()

