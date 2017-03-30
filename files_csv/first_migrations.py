    ##### genre.csv
    with open('/projects/cinema/files_csv/genre.csv', 'rb') as file_text:
        char_type = chardet.detect(file_text.read())['encoding']
    with codecs.open('/projects/cinema/files_csv/genre.csv', 'rb', encoding=char_type) as file_text:
        text = file_text.read()
    l = text.split('\r\n')
    #print(l,'это l')
    for i in l:
        new_genre = Genre(i.split(';')[1].strip())
        #print(i.split(';'), 'это i.split', i.split(';')[1], '___', new_genre.id, new_genre.title)
        db.session.add(new_genre)   
    for instance in db.session.query(Genre): 
        print(instance.id, instance.title)
    #db.session.commit()
    
    ##### director.csv
    with open('/projects/cinema/files_csv/director.csv', 'rb') as file_text:
        char_type = chardet.detect(file_text.read())['encoding']
    with codecs.open('/projects/cinema/files_csv/director.csv', 'rb', encoding=char_type) as file_text:
        text = file_text.read()
    l = text.split('\r\n')
    #print(l,'это l')
    for i in l:
        new_director = Director(i.split(';')[1].strip())
        #print(i.split(';'), 'это i.split', i.split(';')[1], '___', new_director.id, new_director.name)
        db.session.add(new_director)   
    for instance in db.session.query(Director): 
        print(instance.id, instance.name)
    #db.session.commit()

    ##### country.csv
    with open('/projects/cinema/files_csv/country.csv', 'rb') as file_text:
        char_type = chardet.detect(file_text.read())['encoding']
    with codecs.open('/projects/cinema/files_csv/country.csv', 'rb', encoding=char_type) as file_text:
        text = file_text.read()
    l = text.split('\r\n')
    #print(l,'это l')
    for i in l:
        new_country = Country(i.split(';')[1].strip())
        #print(i.split(';'), 'это i.split', i.split(';')[1], '___', new_country.id, new_country.title)
        db.session.add(new_country)   
    for instance in db.session.query(Country): 
        print(instance.id, instance.title)
    #db.session.commit()
    
    ##### cinemaID.csv
    with open('/projects/cinema/files_csv/cinemaID.csv', 'rb') as file_text:
        char_type = chardet.detect(file_text.read())['encoding']
    with codecs.open('/projects/cinema/files_csv/cinemaID.csv', 'rb', encoding=char_type) as file_text:
        text = file_text.read()
    l = text.split('\r\n')
    #print(l,'это l')
    for i in l:
        new_cinema = Cinema(i.split(';')[2].strip(), i.split(';')[1].strip(), i.split(';')[3].strip(), i.split(';')[6].strip(), i.split(';')[5].strip())
        #print(i.split(';'), 'это i.split', i.split(';')[2], '___', new_cinema.id, new_cinema.title)
        db.session.add(new_cinema)   
    for instance in db.session.query(Cinema): 
        print(instance.id, instance.title, instance.director_id, instance.country_id)
    #db.session.commit()
    #id;genre_id;title;year;is_looked;country_id;director_id
    #self, title, genre, year_of_issue, director, country)