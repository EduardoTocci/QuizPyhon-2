import sqlite3


con = sqlite3.connect("quiz.db")

cursor = con.cursor()

# cursor.execute("""
# Create table respostas(
#     id Integer primary key autoincrement,
#     nome varchar(100) not null,
#     pergunta text,
#     resposta text
#     );

# """)

# ids_para_deletar = (1,2)
# cursor.execute(f"delete from respostas where rowid in ({','.join(['?']*len(ids_para_deletar))})", ids_para_deletar)
# print(cursor.fetchall())
# cursor.execute(f"delete from respostas where id = (5)")

# cursor.execute("delete from respostas")
con.commit()


