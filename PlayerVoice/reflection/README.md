All Games related API calls
=====================

This view is responsible for all the games related API calls required by the platform. All API calls should start with `/reflection/{route}/`

My Game APIs are listed below:
- [Get Journals By List](#get-journal-list)
- [Get Journal By ID](#get-journal-by-id)
- [Create Journal](#create-journal)
-----------------------

### Get Journal List

To get a list of all journals

* Route: `journal/`
* Method: GET

* Return:
```
    [
        {
            id: uuid,
            public: bool,
            player: uuid,
            title: str,
            get_up: str,
            feelings: str,
            entry: str,
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
        post: {
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
        },
        likes: int,
        comments: [
            {
                id: uuid (comment id),
                comment: str,
                post: uuid (post id),
                author: {
                    id: uuid, (player id)
                    username: str,
                    birth_year: int,
                    club: str,
                    role: str
                },
                created_at: datetime
            }
        ]
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
        post: {
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
        },
        likes: int,
        comments: [
            {
                id: uuid (comment id),
                comment: str,
                post: uuid (post id),
                author: {
                    id: uuid, (player id)
                    username: str,
                    birth_year: int,
                    club: str,
                    role: str
                },
                created_at: datetime
            }
        ]
    }
```