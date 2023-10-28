All Games related API calls
=====================

This view is responsible for all the games related API calls required by the platform. All API calls should start with `/reflection/{route}/`

My Game APIs are listed below:
- [Get Journals By List](#get-journal-list)
- [Get Journal By ID](#get-journal-by-id)
- [Create Journal](#create-journal)
- [Get Reflections By List](#get-reflection-list)
- [Get Reflection By ID](#get-reflection-by-id)
- [Create Reflection](#create-reflection)  
-----------------------

### Get Journal List

To get a list of all journals

* Route: `journal/`
* Method: GET

* Return:
```
    [
        {
            id: uuid, (journal id)
            player: {
                id: uuid, (player id)
                username: str,
                birth_year: int,
                club: str,
                role: str
            }
            rating: int,
            match_description: str,
            comment: str,
            created_at: datetime
        }
    ]
```

### Get Journal By ID

To get a specific journal using ID

* Route: `journal/{journal_id}`
* Method: GET

* Return:
```
    {
        id: uuid, (journal id)
        player: {
            id: uuid, (player id)
            username: str,
            birth_year: int,
            club: str,
            role: str
        }
        rating: int,
        match_description: str,
        comment: str,
        created_at: datetime
    }
```


### Create Journal

To create journal

* Route: `journal/`
* Method: POST
* Body (form data):
    * player: uuid (player id)
    * rating: int
    * match_description: str
    * comment: str

* Return:
```
    {
        id: uuid, (journal id)
        player: uuid, (player id)
        rating: int,
        match_description: str,
        comment: str,
        created_at: datetime
    }
```


### Get Reflection List

To get a list of all reflections of your own

* Route: `reflection/`
* Method: GET

* Return:
```
    [
        {
            id: uuid, (reflection id)
            player: {
                id: uuid, (player id)
                username: str,
                birth_year: int,
                club: str,
                role: str
            }
            rating: int,
            match_description: str,
            comment: str,
            created_at: datetime
        }
    ]
```

### Get Reflection By ID

To get a specific journal using ID

* Route: `reflection/{reflection_id}`
* Method: GET

* Return:
```
    {
        id: uuid, (reflection id)
        player: {
            id: uuid, (player id)
            username: str,
            birth_year: int,
            club: str,
            role: str
        }
        rating: int,
        match_description: str,
        comment: str,
        created_at: datetime
    }
```


### Create Reflection

To create reflection

* Route: `reflection/`
* Method: POST
* Body (form data):
    * player: uuid (player id)
    * rating: int
    * match_description: str
    * comment: str

* Return:
```
    {
        id: uuid, (reflection id)
        player: {
            id: uuid, (player id)
            username: str,
            birth_year: int,
            club: str,
            role: str
        }
        rating: int,
        match_description: str,
        comment: str,
        created_at: datetime
    }
```