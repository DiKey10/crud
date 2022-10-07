conn = create_connection("database.db")
projekt = ("Powtórka z angielskiego", "2020-05-11 00:00:00", "2020-05-13 00:00:00")
pr_id = add_project(conn, project)