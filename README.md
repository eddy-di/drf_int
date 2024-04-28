# Explanation:

To dump from existing db:

```
python manage.py dumpdata app_name.ModelName --indent 4 > fixtures/fixture_file.json
```

To load fixtures to another db:

```
python manage.py loaddata fixtures/fixture_file.json --app app_name.ModelName
```

# to dump from django.contrib.auth.models the User model:

```
python manage.py dumpdata auth.User -- indent 4 > fixtures/users.json
```

to load to the same table:

```
python manage.py loaddata fixtures/users.json --app auth.User
```
