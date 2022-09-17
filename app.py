# '''Урок 14. SQL. Домашнее задание'''

# import sqlite3
# import prettytable
# from movie import Movie


# def main():
#     '''Main function'''
#     with sqlite3.connect("./netflix.db") as con:
#         cur = con.cursor()
#         sqlite_query = """
#                         SELECT country FROM netflix
#                         LIMIT 10
#                         """
#         result = cur.execute(sqlite_query)

#         my_table = prettytable.from_db_cursor(result)
#         my_table.max_width = 50
#         print(my_table)

# TODO extract to DAO

# def search_by_title(title: str) -> list[Movie]:
#     '''
#     Search movies by title. Return list of Movie
#     '''

#     return []


# # ---
# if __name__ == "__main__":
#     main()
