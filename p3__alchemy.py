from sqlalchemy import *

engine = create_engine('sqlite:///books.db')
metadata = MetaData()


authors = Table('authors', metadata, autoload_with=engine)
books = Table('books', metadata, autoload_with=engine)
print("=== ЗАДАЧА 1: Все авторы ===")

conn = engine.connect()
result = conn.execute(select(authors))

print(*result, sep='\n')

print("\n=== ЗАДАЧА 3: Найти Антона Чехова ===")
res = conn.execute(select(authors).where(authors.c.name == 'Антон Чехов'))
print(*res, sep='\n')

print("\n=== ЗАДАЧА 4: Найти 'Война и мир' ===")
res = conn.execute(select(books).where(books.c.title == 'Война и мир'))
print(*res, sep='\n')

print("\n=== ЗАДАЧА 6: Книги 1869 года ===")
res = conn.execute(select(books).where(books.c.year == '1869'))
print(*res, sep='\n')


print("\n=== ЗАДАЧА 9: Общее количество книг ===")
result = conn.execute(select(func.count()).select_from(books))
result = result.scalar()
print(result)


res = conn.execute(select(authors.c.name))
res_list = list(res)
sorted_res = sorted(res_list, key=lambda x: x.name.split()[-1])
print("\n=== Сортировка по фамилии (Питон) ===")
for row in sorted_res:
    print(row.name)



res = conn.execute(
    select(books.c.title, books.c.year, authors.c.name)
    .join(authors)
    .where(authors.c.name == 'Лев Толстой')
)
print(*res, sep='\n')

res = conn.execute(
    select(books, authors)
    .join(authors)
    .where(authors.c.name == 'Лев Толстой')
)
print(*res, sep='\n')


# print("\n=== ЗАДАЧА 10: Количество книг по авторам ===")


# ЗАДАЧА 11: Найти авторов, у которых есть книги с названием содержащим "и"
res = conn.execute(
    select(authors.c.name, books.c.title)
    .select_from(authors.join(books))
    .where(books.c.title.like('% и %'))
    .group_by(authors.c.name)
)

print(*res, sep='\n')


print("\n=== ЗАДАЧА 6: Найти самую раннюю книгу ===")
res = conn.execute(
    select(books.c.title,func.min(books.c.year))  
)
print(*res, sep='\n')

